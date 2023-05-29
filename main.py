import customtkinter as ctk
from PIL import Image
from classes.widgets import AnimatedButton, SlidePanel
from views.views import ViewContainer
from views.graphics import GraphicView
from views.graphics import EulerView
from views.history import HistoryView
from views.login import LoginView
from views.register import RegisterView

#window
window = ctk.CTk()
window.title('Grapher')
window.geometry('1024x720')
ctk.set_appearance_mode('dark')

#Animated widget
animated_panel = SlidePanel(window, -0.2, 0)

#Main view container and frames
view_manager = ViewContainer(window)

#Views
graphic_view = GraphicView(view_manager)
euler_view = EulerView(view_manager)
history_view = HistoryView(view_manager)
login_view = LoginView(view_manager)
register_view = RegisterView(view_manager)

#Stablish the view dict
view_manager.set_view_dict({'graphic': graphic_view, 'euler': euler_view, 'history': history_view, 'login': login_view, 'register': register_view})
view_manager.change_view('graphic')

#Top menu bar
top_menu = ctk.CTkFrame(master = window, height=50)
top_menu.place(x=0, y=0, relwidth = 1)

#Menu content images
user_icon = ctk.CTkImage(Image.open("./assets/user.png"))
menu_icon = ctk.CTkImage(Image.open("./assets/menu-burger.png"))
cross_icon = ctk.CTkImage(Image.open("./assets/cross.png"))

#Menu buttons
menu_button = AnimatedButton(top_menu, menu_icon, cross_icon, 100, 30, 30)
menu_button.place(x=20, y=10)

def menu_button_command():
    animated_panel.raise_view()
    top_menu.tkraise()
    animated_panel.animate()
    menu_button.animate()

menu_button.configure(command=menu_button_command)

user_button = ctk.CTkButton(top_menu, text="", image=user_icon, corner_radius=100, width=30, height=30)
user_button.place(relx=0.95, y=25, anchor="e")

#Function for menu buttons
def change_view(name):
    view_manager.change_view(name)
    animated_panel.animate()
    menu_button.animate()

#Menu content
graph_button = ctk.CTkButton(animated_panel, text="Graph Function", command=lambda: change_view("graphic"))
euler_button = ctk.CTkButton(animated_panel, text="Graph Euler's Method", command=lambda: change_view("euler"))
history_button = ctk.CTkButton(animated_panel, text="My Graphs", command=lambda: change_view("history"))

graph_button.pack(pady=(55, 0), padx=20, fill="x")
euler_button.pack(pady=(10, 0), padx=20, fill="x")
history_button.pack(pady=10, padx=20, fill="x")


#Main loop
window.mainloop() 
