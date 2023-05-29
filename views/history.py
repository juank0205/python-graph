from views.views import View
import customtkinter as ctk

        #Background color = 242424
class HistoryView(View):
    def __init__(self, parent):
        super().__init__(parent )
        self.place(relwidth=1, relheight=1)

        #Content to be defined
        Title = ctk.CTkLabel(master=self, text="History view")
        Title.place(relx=0.5, rely=0.5)
