from tkinter.ttk import Progressbar
from belezena_scraper import Scraper
from tkinter import *

# First create application class
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.scrape = Scraper(self.get_count)
        self.categories = self.scrape.get_categories()

        self.pack()
        self.create_widgets()

    def CurSelet(self, evt):
        self.selected = self.lbox.curselection()[0]

    def select(self):
        selected_category = next(
            item
            for item in self.categories
            if item["title"] == self.lbox.get(first=self.selected)
        )
        if selected_category:
            self.count_label = Label(self, text="Downloaded data: 0")
            self.count_label.grid(row=4, column=0, padx=10, pady=3)
            self.pb = Progressbar(
                self, orient="horizontal", mode="indeterminate", length=280
            )
            self.pb.grid(row=5, column=0, padx=10, pady=3)
            self.pb.start()
            self.scrape.get_items(selected_category)
            self.pb.stop()
            self.pb.destroy()

    # Create main GUI window
    def create_widgets(self):
        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_list())
        self.entry = Entry(self, textvariable=self.search_var, width=13)
        self.lbox = Listbox(self, selectmode=SINGLE, width=45, height=15)
        self.lbox.bind("<<ListboxSelect>>", self.CurSelet)

        self.entry.grid(row=0, column=0, padx=10, pady=3)
        self.lbox.grid(row=1, column=0, padx=10, pady=3)

        self.btn = Button(self, text="Download!!", command=self.select, width=20)
        self.btn.grid(row=2, column=0, padx=10, pady=3)

        self.cursel = StringVar()
        self.lb1 = Label(self, textvariable=self.cursel)
        self.lb1.grid(row=3, column=0, padx=10, pady=3)

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self):
        search_term = self.search_var.get()

        self.lbox.delete(0, END)

        for item in self.categories:
            if search_term.lower() in item["title"].lower():
                self.lbox.insert(END, item["title"])

        allitems = list()
        for i in range(self.lbox.size()):
            allitems.append(self.lbox.get(i))

    def get_count(self, count):
        self.count_label["text"] = f"Downloaded data: {str(count)}"
        self.master.update()


root = Tk()
root.title("Beleza na bot")
Label(root, text="Enter text to Search brands/categories.").pack()
app = Application(master=root)
print("Starting mainloop()")
app.mainloop()
