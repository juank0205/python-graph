from views.views import View
import customtkinter as ctk

        #Background color = 242424
class LoginView(View):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relwidth=1, relheight=1)
        self.__username = ctk.StringVar(parent, value='')
        self.__password = ctk.StringVar(parent, value='')

        #Content
        ctk.CTkLabel(master=self, text="LOGIN", font=("", 40)).pack(pady=(20, 50))
        ctk.CTkLabel(master=self, text="Username", font=("", 16)).pack()

        username_entry = ctk.CTkEntry(master=self, textvariable=self.__username)
        username_entry.pack()

        ctk.CTkLabel(master=self, text="Password", font=("", 16)).pack()

        password_entry = ctk.CTkEntry(master=self, textvariable=self.__password, show="*")
        password_entry.pack(pady=(0, 10))

        ctk.CTkButton(master=self, text='Submit', command=self.submit).pack(pady=10)
    
        password_entry.bind('<Return>', lambda a: self.submit())

    def submit(self):
        print(self.__username.get(), self.__password.get())
