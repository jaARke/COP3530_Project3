from tkinter import *
from tkcalendar import Calendar
import tkinter.font


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
        self.applicationLabel = Label(self.master, text="Cryptograph: A Way of Interfacing with Cryptocurrency "
                                                        "Data", font="Consolas 20 bold", fg="white", bg="#484a4d",
                                      pady=10)
        self.applicationLabel.pack(side=TOP)

        # Initialize the GUI frames
        self.dateFrame = LabelFrame(self.master, text="Time Span of Interest:", font="Arial 12 bold", fg="white",
                                    bg="#484a4d", pady=5)
        self.structFrame = LabelFrame(self.master, text="Data Structure:", font="Arial 12 bold", fg="white",
                                      bg="#484a4d", pady=5)
        self.currFrame = LabelFrame(self.master, text="Currencies of Interest:", font="Arial 12 bold", fg="white",
                                    bg="#484a4d", pady=5)

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


root = Tk()
gui = ApplicationWindow(root)
root.mainloop()
