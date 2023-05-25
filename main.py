import customtkinter as ctk
from widgets import SlidePanel

#window
window = ctk.CTk()
window.title('Grapher')
window.geometry('600x400')
ctk.set_appearance_mode('dark')

#Animated widget
animated_panel = SlidePanel(window, -0.3, 0)

#Menu button
isToggled = False
button_x = 0.15
button = ctk.CTkButton(window, text='Menu', command = animated_panel.animate)
button.place(relx = button_x, rely = 0.1, anchor = 'center')

#Main loop
window.mainloop()
