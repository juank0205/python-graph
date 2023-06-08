import customtkinter as ctk

class AnimatedWidget(object):
    def __init__(self):
        self.is_running = False
        self.is_toggled = False

    def animate(self):
        if self.is_running:
            return
        self.is_running = True
        if self.is_toggled:
            self.animate_backwards()
        else:
            self.animate_forward()
        self.is_toggled = not self.is_toggled

    def animate_forward(self):
        pass

    def animate_backwards(self):
        pass

class SlidePanel(ctk.CTkFrame, AnimatedWidget):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)
        AnimatedWidget.__init__(self)

        #Properties
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos-end_pos)

        #Animation status
        self.pos = self.start_pos
        self.__speed = 0.008
        self.__delay = 5

        #Layout
        self.place(relx = self.start_pos, y=0, relwidth = self.width, relheight = 1)

    def animate_forward(self):
        if self.pos < self.end_pos:
            self.pos += self.__speed
            self.place(relx = self.pos, y=0, relwidth = self.width, relheight = 1)
            self.after(self.__delay, self.animate_forward)
        else:
            self.is_running = False

    def animate_backwards(self):
        if self.pos > self.start_pos:
            self.pos -= self.__speed
            self.place(relx = self.pos, y=0, relwidth = self.width, relheight = 1)
            self.after(self.__delay, self.animate_backwards)
        else:
            self.is_running = False

    def raise_view(self):
        self.tkraise()

class AnimatedButton(ctk.CTkButton, AnimatedWidget):
    def __init__(self, parent, initial_image, final_image, corner_radius, width, height):
        super().__init__(master=parent, text="", image=initial_image, corner_radius=corner_radius, width=width, height=height)
        AnimatedWidget.__init__(self)

        #Image definition
        self.initial_image = initial_image
        self.final_image = final_image

    def animate_forward(self):
        self.configure(image=self.final_image)
        self.is_running = False

    def animate_backwards(self):
        self.configure(image=self.initial_image)
        self.is_running = False

class DropdownMenu(ctk.CTkFrame, AnimatedWidget):
    def __init__(self, parent, start_pos, end_pos, view_manager, user):
        #Properties
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.height = abs(start_pos-end_pos)
        self.view_manager = view_manager
        self.user = user

        #Colors
        self.__color1 = '#2b2b2b'
        self.__color2 = '#333333'
        
        super().__init__(master = parent, height=self.height, cursor="hand2")
        AnimatedWidget.__init__(self)

        #Animation status
        self.pos = self.start_pos
        self.__speed = 2
        self.__delay = 5

        #Layout
        self.place(y=self.start_pos, relx=0.8, relwidth=0.2)

        #Content
        self.login_button = ctk.CTkLabel(master=self, text="Login", height=50, cursor="hand2")
        self.register_button = ctk.CTkLabel(master=self, text="Register", height=50, cursor="hand2")

        self.logout_button = ctk.CTkLabel(master=self, text="Logout", height=50, cursor="hand2")
        self.username = ctk.CTkLabel(master=self, text="", height=50)

        self.active_state = [self.login_button, self.register_button]

        self.login_button.bind("<Button-1>", lambda e: self.change_view("login"))
        self.logout_button.bind("<Button-1>", lambda e: self.logout())
        self.register_button.bind("<Button-1>", lambda e: self.change_view("register"))

        #Hover
        self.login_button.bind("<Enter>", lambda e: self.login_button.configure(fg_color=self.__color2))
        self.login_button.bind("<Leave>", lambda e: self.login_button.configure(fg_color=self.__color1))
        self.logout_button.bind("<Enter>", lambda e: self.login_button.configure(fg_color=self.__color2))
        self.logout_button.bind("<Leave>", lambda e: self.login_button.configure(fg_color=self.__color1))
        self.register_button.bind("<Enter>", lambda e: self.register_button.configure(fg_color=self.__color2))
        self.register_button.bind("<Leave>", lambda e: self.register_button.configure(fg_color=self.__color1))

        self.change_content()

    def animate_forward(self):
        if self.pos < self.end_pos:
            self.pos += self.__speed
            self.place(y=self.pos, relx=0.8)
            self.after(self.__delay, self.animate_forward)
        else:
            self.is_running = False

    def animate_backwards(self):
        if self.pos > self.start_pos:
            self.pos -= self.__speed
            self.place(y=self.pos, relx=0.8)
            self.after(self.__delay, self.animate_backwards)
        else:
            self.is_running = False

    def raise_view(self):
        self.tkraise()

    def change_content(self):
        self.username.configure(text=self.user.username)
        self.active_state = [self.username, self.logout_button] if self.user.loggedIn else [self.login_button, self.register_button]
        for (index, button) in enumerate(self.active_state):
            button.place(relwidth=1, y=50*index+50)

    def logout(self):
        self.change_view("login")
        self.user.logout()

    def change_view(self, name):
        self.view_manager.change_view(name)
        self.animate()
