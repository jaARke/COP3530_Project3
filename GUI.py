from tkinter import *
from tkcalendar import Calendar
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import time


class ApplicationWindow:
    fromDate = ""
    toDate = ""
    dataStruct = ""
    currencies = []

    def __init__(self, master):
        self.master = master
        master.title("CryptoGraph")
        master.geometry("1200x750+0+0")
        master["background"] = "#484a4d"
        self.applicationLabel = Label(self.master, text="CryptoGraph: A Way of Interfacing with Cryptocurrency "
                                                        "Data", font="Consolas 20 bold", fg="white", bg="#484a4d",
                                      pady=10)
        self.applicationLabel.pack(side=TOP)

        # Initialize the GUI frames
        self.dateFrame = LabelFrame(self.master, text="Time Span of Interest", font="Arial 12 bold", fg="white",
                                    bg="#484a4d", pady=5)
        self.structFrame = LabelFrame(self.master, text="Data Structure", font="Arial 12 bold", fg="white",
                                      bg="#484a4d", pady=5)
        self.currFrame = LabelFrame(self.master, text="Currencies of Interest", font="Arial 12 bold", fg="white",
                                    bg="#484a4d", pady=5)
        self.graphFrame = LabelFrame(self.master, text="Currency Chart", font="Arial 12 bold", fg="white", bg="#484a4d",
                                     pady=5)

        # Initialize frame members
        self.create_date_frame()
        self.create_struct_frame()
        self.create_curr_frame()

        # Display the beginning state (time selection)
        self.dateFrame.pack()

    def create_date_frame(self):
        instruct = Label(self.dateFrame, text="Select the start and end dates", font="Arial 10 italic", fg="white",
                         bg="#484a4d", pady=5)
        instruct.pack()
        from_calendar = Calendar(self.dateFrame)
        from_calendar.pack()
        to_label = Label(self.dateFrame, text="To", font="Arial 12 bold", fg="white",
                         bg="#484a4d", pady=5)
        to_label.pack()
        to_calendar = Calendar(self.dateFrame)
        to_calendar.pack()
        select_button = Button(self.dateFrame, text="OK", font="Arial 10 bold",
                               command=lambda: self.date_entry(from_calendar.get_date(), to_calendar.get_date()))
        select_button.pack()

    def create_struct_frame(self):
        instruct = Label(self.structFrame, text="Select a data structure", font="Arial 10 italic", fg="white",
                         bg="#484a4d", pady=5)
        instruct.pack()
        map_button = Button(self.structFrame, text="Map", font="Arial 10 bold", command=lambda: self.struct_entry
                            ("Map"), height=10, width=20)
        map_button.pack(side=LEFT)
        tree_button = Button(self.structFrame, text="Tree", font="Arial 10 bold",
                             command=lambda: self.struct_entry("Tree"), height=10, width=20)
        tree_button.pack(side=RIGHT)

    def create_curr_frame(self):
        instruct = Label(self.currFrame, text="Enter the abbreviated names of up to 3 cryptocurrencies (ex: for "
                                              "Bitcoin, enter BTC)", font="Arial 10 italic", fg="white", bg="#484a4d",
                         pady=5, padx=5)
        instruct.pack()
        entry1 = Entry(self.currFrame, text="Currency #1")
        entry1.pack()
        entry2 = Entry(self.currFrame, text="Currency #2")
        entry2.pack()
        entry3 = Entry(self.currFrame, text="Currency #3")
        entry3.pack()
        select_button = Button(self.currFrame, text="OK", font="Arial 10 bold",
                               command=lambda: self.curr_entry([entry1.get(), entry2.get(), entry3.get()]))
        select_button.pack()

    def date_entry(self, from_date, to_date):
        self.fromDate = from_date
        self.toDate = to_date
        self.display_struct_frame()

    def struct_entry(self, struct):
        self.dataStruct = struct
        self.display_curr_frame()

    def curr_entry(self, currencies):
        self.currencies = currencies
        self.build_graph()

    def display_struct_frame(self):
        self.dateFrame.destroy()
        self.structFrame.pack()

    def display_curr_frame(self):
        self.structFrame.destroy()
        self.currFrame.pack()

    def build_graph(self):
        self.currFrame.destroy()

        # Construct the graph:
        start_time = time.time()
        # (these settings might need changing)
        figure = Figure(figsize=(10, 5), dpi=100)
        plot = figure.add_subplot(111)
        # Load in data points:

        # Place data points on the graph:

        # Draw the completed graph to the screen:
        canvas = FigureCanvasTkAgg(figure, master=self.graphFrame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, self.graphFrame)
        toolbar.update()
        canvas.get_tk_widget().pack()
        end_time = time.time()
        graph_time = round(end_time - start_time, 4)
        graph_time_label = Label(self.graphFrame, text="Graph constructed in %s seconds" % graph_time,
                                 font="Arial 10 italic", fg="white", bg="#484a4d", pady=5, padx=5)
        graph_time_label.pack()

        # Access lowest, average, and highest price values for each currency
        counter = 1
        for i in self.currencies:
            stat_frame = Frame(self.graphFrame, bg="#484a4d")
            # Find lowest price:
            start_time = time.time()
            # (call a function to return the lowest price of this currency)
            lowest_price = 0
            end_time = time.time()
            lowest_time = round(end_time - start_time, 2)
            lowest_label = Label(stat_frame, text="Lowest price (%s): %s (%s seconds)" % (i, lowest_price, lowest_time),
                                 font="Arial 10 italic", fg="white", bg="#484a4d")
            lowest_label.pack()

            # Find the average price:
            start_time = time.time()
            # (call a function to return the average price of this currency)
            average_price = 0
            end_time = time.time()
            average_time = round(end_time - start_time, 2)
            average_label = Label(stat_frame, text="Average price (%s): %s (%s seconds)" % (i, average_price,
                                                                                            average_time),
                                  font="Arial 10 italic", fg="white", bg="#484a4d")
            average_label.pack()

            # Find the highest price:
            start_time = time.time()
            # (call a function to return the highest price of this currency)
            highest_price = 0
            end_time = time.time()
            highest_time = round(end_time - start_time, 2)
            highest_label = Label(stat_frame, text="Highest price (%s): %s (%s seconds)" % (i, highest_price,
                                                                                            highest_time),
                                  font="Arial 10 italic", fg="white", bg="#484a4d")
            highest_label.pack(pady=(0, 10))

            if counter == 1:
                stat_frame.pack(side=LEFT)
                counter += 1
            elif counter == 2:
                stat_frame.config(padx=190)  # Roundabout way of aligning each stat_frame
                stat_frame.pack(side=LEFT)
                counter += 1
            else:
                stat_frame.pack(side=RIGHT)
                counter += 1

        # Build the other parts of the graphFrame:
        reset_button = Button(toolbar, text="RESET", font="Arial 15 bold", bg="red", fg="white", command=lambda:
                              self.reset())
        reset_button.pack(side=LEFT, padx=20)

        self.graphFrame.pack()

    def reset(self):
        self.graphFrame.destroy()
        self.applicationLabel.destroy()
        self.__init__(self.master)


root = Tk()
gui = ApplicationWindow(root)
root.mainloop()
