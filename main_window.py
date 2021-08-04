from belezena_scraper import Scraper
from tkinter import Tk, Label, Button, ttk
    

class MyFirstGUI:
    def __init__(self, master):
        self.count = 0
        self.scrape = Scraper(self.get_count)

        self.master = master
        master.title("Beleza na bot")

        self.label = Label(master, text="Click download button to run the bot!")
        self.label.pack()

        self.download_button = Button(master, text="download", command=self.download)
        self.download_button.pack()

        self.count_label = Label(master, text="Downloaded data: 0")
        self.count_label.pack()

        self.pb = ttk.Progressbar(
            master,
            orient='horizontal',
            mode='indeterminate',
            length=280
        )
    
    def get_count(self, count):
        self.count_label['text'] = f"Downloaded data: {str(count)}"
        self.master.update()

    def download(self):
        print("downloading!")
        self.pb.pack()
        self.pb.start()
        self.scrape.main()
        self.pb.stop()
        

root = Tk()
root.geometry("300x150")
my_gui = MyFirstGUI(root)
root.mainloop()
