import customtkinter as ctk

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)

        #Properties
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos-end_pos)

        #Layout
        self.place(relx = self.start_pos, rely = 0, relwidth = self.width, relheight = 1)
