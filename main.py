import customtkinter as ctk
import classes.sql as sql
import classes.user 
from PIL import Image
from classes.widgets import AnimatedButton, SlidePanel, DropdownMenu
from views.views import ViewContainer
from views.graphics import GraphicView
from views.graphics import EulerView
from views.history import HistoryView
from views.login import LoginView
from views.register import RegisterView

#Connection to database

#Use when connecting from db4free 
print("Connecting to database...")
print("This may take a minute to complete, im using a free domain")
connector = sql.SqlConnector("db4free.net", "remotest123", "test123456789", "pythongraph")

#Define user
user = classes.user.User()

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
graphic_view = GraphicView(view_manager, connector, user)
euler_view = EulerView(view_manager, connector, user)
history_view = HistoryView(view_manager, connector, user, graphic_view, euler_view)
login_view = LoginView(view_manager, connector, user)
register_view = RegisterView(view_manager, connector, user)

graphic_view.set_refresh_callback(history_view.get_graphs)
euler_view.set_refresh_callback(history_view.get_graphs_DE)

#Stablish the view dict
view_manager.set_view_dict({'graphic': graphic_view, 'euler': euler_view, 'history': history_view, 'login': login_view, 'register': register_view})
view_manager.change_view('graphic')

#Top menu bar
top_menu = ctk.CTkFrame(master = window, height=50)
top_menu.place(x=0, y=0, relwidth = 1)

#Dropdown menu
dropdown_menu = DropdownMenu(window, -150, 0, view_manager, user)

def login_callback():
    dropdown_menu.change_content()
    view_manager.change_view('history')
    history_view.get_graphs()
    history_view.get_graphs_DE()

def logout_callback():
    dropdown_menu.change_content()
    history_view.delete_graphs()
    history_view.delete_graphs_DE()
    view_manager.change_view('graphic')

user.set_callback(login_callback, logout_callback)

#Menu content images
user_icon = ctk.CTkImage(Image.open("./assets/user.png"))
menu_icon = ctk.CTkImage(Image.open("./assets/menu-burger.png"))
cross_icon = ctk.CTkImage(Image.open("./assets/cross.png"))

#Menu buttons
menu_button = AnimatedButton(top_menu, menu_icon, cross_icon, 100, 30, 30)
menu_button.place(x=20, y=10)

#Function for menu buttons
def menu_button_command():
    animated_panel.raise_view()
    top_menu.tkraise()
    animated_panel.animate()
    menu_button.animate()

def change_view(name):
    view_manager.change_view(name)
    animated_panel.animate()
    menu_button.animate()

def dropdown():
    dropdown_menu.raise_view()
    top_menu.tkraise()
    dropdown_menu.animate()

menu_button.configure(command=menu_button_command)

user_button = ctk.CTkButton(top_menu, text="", image=user_icon, corner_radius=100, width=30, height=30, command=dropdown)
user_button.place(relx=0.95, y=25, anchor="e")

#Menu content
graph_button = ctk.CTkButton(animated_panel, text="Graph Function", command=lambda: change_view("graphic"))
euler_button = ctk.CTkButton(animated_panel, text="Graph Euler's Method", command=lambda: change_view("euler"))
history_button = ctk.CTkButton(animated_panel, text="My Graphs", command=lambda: change_view("history"))

graph_button.pack(pady=(55, 0), padx=20, fill="x")
euler_button.pack(pady=(10, 0), padx=20, fill="x")
history_button.pack(pady=10, padx=20, fill="x")

#Main loop
window.mainloop() 
