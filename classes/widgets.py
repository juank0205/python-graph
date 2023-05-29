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

