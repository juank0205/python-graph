import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter.windows.widgets.image import CTkImage
from widgets import SlidePanel

#window
window = ctk.CTk()
window.title('Grapher')
window.geometry('600x400')
ctk.set_appearance_mode('dark')

#Animated widget
animated_panel = SlidePanel(window, -0.3, 0)

#Top menu bar
top_menu = ctk.CTkFrame(master = window, height=50)
top_menu.place(x=0, y=0, relwidth = 1)

#Menu button
button = ctk.CTkButton(top_menu, width=100, height=30, text='Menu', command = animated_panel.animate)
button.place(x=5, y=10)

#Menu content images
user_icon = ctk.CTkImage(Image.open("./assets/user.png"))
menu_icon = ctk.CTkImage(Image.open("./assets/menu-burger.png"))
cross_icon = ctk.CTkImage(Image.open("./assets/cross.png"))

#Menu content
graph_button = ctk.CTkButton(animated_panel, text="Graph Function")
euler_button = ctk.CTkButton(animated_panel, text="Graph Euler's Method")
history_button = ctk.CTkButton(animated_panel, text="My Graphs")
user_button = ctk.CTkButton(animated_panel, text="", image=user_icon)

graph_button.pack(pady=(55, 0))
euler_button.pack(pady=(10, 0))
history_button.pack(pady=10)
user_button.place(relx=0.9, rely=0.99, anchor='se')

#Main loop
window.mainloop() 
