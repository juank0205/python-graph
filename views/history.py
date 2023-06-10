from views.views import View
import customtkinter as ctk

#This class represents a single entry inside the scrollable frame
#When clicked, excecutes a callback meant to change the view and plot the string that it holds
class ChartFrame(ctk.CTkFrame):
    def __init__(self, parent, id, string, index, graphic_view):
        super().__init__(master=parent, height=40, width=parent.winfo_width(), cursor="hand2")
        self.graphic_view = graphic_view

        #Colors
        self.__color1 = '#2b2b2b'
        self.__color2 = '#333333'

        self.id = id
        self.string=string

        label_index = ctk.CTkLabel(master=self, text=index)
        string = ctk.CTkLabel(master=self, text=string)
        delete = ctk.CTkButton(master=self, text="Delete", command=self.delete)

        label_index.place(relx=0.05, relwidth=0.1)
        string.place(relx=0.15, relwidth=0.7)
        delete.place(relx=0.85, relwidth=0.1)

        #Excecutes the callback
        self.bind("<Button-1>", lambda e: self.graph())
        label_index.bind("<Button-1>", lambda e: self.graph())
        string.bind("<Button-1>", lambda e: self.graph())

        #Binding the hover event to every widget inside the frame but the button
        self.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        self.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))
        label_index.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        label_index.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))
        string.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        string.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))

        self.pack()

    def graph(self):
        self.graphic_view.change_graph_history(self.string)
        
    #Deleting a graph from the database is not yet supported
    def delete(self):
        print("Luego")

#Differential equations need some extra labels to show the initial coordinates of the graph
class ChartFrame_DE(ChartFrame):
    def __init__(self, parent, id, string, index, initial_x, initial_y, graphic_view):
        ctk.CTkFrame.__init__(self, master=parent, height=40, width=parent.winfo_width(), cursor="hand2")
        self.graphic_view = graphic_view

        #Colors
        self.__color1 = '#2b2b2b'
        self.__color2 = '#333333'

        self.id = id
        self.string = string
        self.initial_x = initial_x
        self.initial_y = initial_y

        label_index = ctk.CTkLabel(master=self, text=index)
        string = ctk.CTkLabel(master=self, text=string)
        initial_x = ctk.CTkLabel(master=self, text=initial_x)
        initial_y = ctk.CTkLabel(master=self, text=initial_y)
        delete = ctk.CTkButton(master=self, text="Delete", command=self.delete)

        label_index.place(relx=0.05, relwidth=0.1)
        string.place(relx=0.15, relwidth=0.5)
        initial_x.place(relx=0.65, relwidth=0.1)
        initial_y.place(relx=0.75, relwidth=0.1)
        delete.place(relx=0.85, relwidth=0.1)

        self.bind("<Button-1>", lambda e: self.graph())
        label_index.bind("<Button-1>", lambda e: self.graph())
        string.bind("<Button-1>", lambda e: self.graph())
        initial_x.bind("<Button-1>", lambda e: self.graph())
        initial_y.bind("<Button-1>", lambda e: self.graph())

        self.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        self.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))
        label_index.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        label_index.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))
        string.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        string.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))
        initial_x.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        initial_x.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))
        initial_y.bind("<Enter>", lambda e: self.configure(fg_color=self.__color2))
        initial_y.bind("<Leave>", lambda e: self.configure(fg_color=self.__color1))

        self.pack()

    def graph(self):
        self.graphic_view.change_graph_history(self.string, self.initial_x, self.initial_y)


class HistoryView(View):
    def __init__(self, parent, sql_connector, user, graphic_view, euler_view):
        super().__init__(parent)
        self.place(relwidth=1, relheight=1)

        self.sql_connector = sql_connector
        self.user = user
        self.graphic_view = graphic_view
        self.euler_view = euler_view

        self.scrollable_frame_graphs = ctk.CTkScrollableFrame(master=self, label_text="My Graphs")
        self.scrollable_frame_graphs.place(relwidth=0.9, relheight=0.4, relx=0.05, y=10)
        self.scrollable_frame_DE = ctk.CTkScrollableFrame(master=self, label_text="Differential Equations")
        self.scrollable_frame_DE.place(relwidth=0.9, relheight=0.4, relx=0.05, rely=0.45)

        #Lists that store the entries retrieved from the database
        self.graphs = []
        self.differential_equations = []
        self.get_graphs()

    def get_graphs(self):
        #Iterates the list to create each clickable entry
        for frame in self.scrollable_frame_graphs.winfo_children():
            frame.destroy()
        self.graphs = self.sql_connector.get_user_graphs(self.user.get_id())
        for (index, graph) in enumerate(self.graphs):
            ChartFrame(self.scrollable_frame_graphs, graph[0], graph[1], index+1, self.graphic_view)
        
    #Clears the scrollable view
    def delete_graphs(self):
        self.graphs = []
        for frame in self.scrollable_frame_graphs.winfo_children():
            frame.destroy()

    def get_graphs_DE(self):
        for frame in self.scrollable_frame_DE.winfo_children():
            frame.destroy()
        self.graphs = self.sql_connector.get_user_differential_equations(self.user.get_id())
        for (index, graph) in enumerate(self.graphs):
            ChartFrame_DE(self.scrollable_frame_DE, graph[0], graph[1], index+1, graph[3], graph[4], self.euler_view)

    def delete_graphs_DE(self):
        self.graphs = []
        for frame in self.scrollable_frame_DE.winfo_children():
            frame.destroy()

