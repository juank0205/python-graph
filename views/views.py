import customtkinter as ctk

class View(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
    
    def raise_view(self):
        self.tkraise()

class ViewContainer(ctk.CTkFrame):
    def __init__(self, parent, view_dict={}):
        super().__init__(master=parent)
        self.__active_view = ""
        self.view_dict = view_dict
        self.place(relwidth=1, relheight=1, y=50)

    #Setters
    def get_active_view(self):
        return self.__active_view

    #Getters
    def set_view_dict(self, view_dict):
        self.view_dict = view_dict
    
    def change_view(self, name):
        if self.__active_view is not name:
            self.view_dict[name].tkraise()
            self.__active_view = name
