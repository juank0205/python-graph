from views.views import View
import customtkinter as ctk

class ChartFrame(ctk.CTkFrame):
    def __init__(self, parent, id, string, index):
        super().__init__(master=parent, height=40, width=parent.winfo_width())

        self.id = id
        label_index = ctk.CTkLabel(master=self, text=index)
        string = ctk.CTkLabel(master=self, text=string)
        delete = ctk.CTkButton(master=self, text="Delete", command=self.delete)

        label_index.place(relx=0.05, relwidth=0.1)
        string.place(relx=0.15, relwidth=0.7)
        delete.place(relx=0.85, relwidth=0.1)

        self.pack()


    def delete(self):
        print("Luego")


class HistoryView(View):
    def __init__(self, parent, sql_connector, user):
        super().__init__(parent)
        self.place(relwidth=1, relheight=1)

        self.sql_connector = sql_connector
        self.user = user

        self.scrollable_frame = ctk.CTkScrollableFrame(master=self, label_text="My Graphs")
        self.scrollable_frame.place(relwidth=0.9, relx=0.05, y=10)
        self.graphs = []
        self.get_graphs()

    def get_graphs(self):
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
        self.graphs = self.sql_connector.get_user_graphs(self.user.get_id())
        for (index, graph) in enumerate(self.graphs):
            ChartFrame(self.scrollable_frame, graph[0], graph[1], index+1)
        
    def delete_graphs(self):
        self.graphs = []
        for frame in self.scrollable_frame.winfo_children():
            frame.destroy()
