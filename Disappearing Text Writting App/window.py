from tkinter import Tk, StringVar, OptionMenu, Text, ttk, Button, Label, END
from tkinter.messagebox import showinfo


class App(Tk):

    def __init__(self):
        super().__init__()
        self.solve = None
        self.time = 0
        self.counter = 0
        self.timer = 0
        self.progress = 0
        self.text_len = 0
        self.text_len_check = 0
        self.geometry("1000x800")
        self.title("Disappearing Text Writing App")

        # Create Time Option Menu for Session Length
        self.variables = StringVar()
        self.variables.set("5 min")

        self.option = OptionMenu(self, self.variables, "1 min", "5 min", "10 min", "15 min")
        self.option.pack(pady=25)

        # Create Start Button
        self.start_button = Button(width=20, text="Start Session", command=self.start_session)
        self.start_button.pack(pady=10)

        # Create horizontal progress bar
        self.progress_bar = ttk.Progressbar(orient="horizontal", mode="determinate", length=950)
        self.progress_bar.pack()

        # Create Text Box
        self.text_box = Text(width=800, height=45, highlightcolor="green")
        self.text_box.pack(padx=15)

        # Create word counter
        self.word_counter = Label(text=f"{self.counter} Words", fg="gray")
        self.word_counter.pack(pady=5)

        # Export Button
        self.export_button = Button(text="Export", width=10)

    # Initialize the parameters for the session
    def start_session(self):
        self.text_box.delete("1.0", END)
        self.export_button.pack_forget()
        self.counter = 0
        self.start_button.configure(text="Start Session")
        self.text_box.configure(highlightcolor="green", highlightthickness=1)
        self.progress_bar["value"] = 0
        self.text_box.focus()
        self.timer = int(self.variables.get().split(" ")[0])
        self.timer *= 60
        self.progress = (100 / self.timer)
        self.time = 0
        self.text_box.bind("<Key>", self.timer_count)
        self.text_box.bind("<space>", self.word_count)

    # Check the progress
    def timer_count(self, _event):

        self.text_box.unbind("<Key>")
        text = self.text_box.get("1.0", END)
        self.text_len = int(len(text))

        if self.time >= 5:
            showinfo(message=f"Time is over!\n You got:{round(self.progress_bar['value'], 2)}% from this session")
            self.text_box.delete("1.0", END)
            self.start_button.configure(text="Start Session Again")

        else:
            if self.progress_bar["value"] < 100:
                self.solve = self.text_box.after(ms=1000, func=self.timer_sub)
            elif self.progress_bar["value"] >= 100:
                showinfo(message="You got it!\n If you want, you can go on.")
                self.start_button.configure(text="Start Session Again")
                self.export_button.pack()

    # Subtract the time from session
    def timer_sub(self):
        self.timer -= 1
        self.progress_bar["value"] += self.progress

        if self.text_len <= self.text_len_check:
            self.time += 1
            if self.time == 2:
                self.text_box.configure(highlightcolor="orangered", highlightthickness=2)
            elif self.time == 3:
                self.text_box.configure(highlightcolor="red", highlightthickness=4)
            elif self.time == 5:
                self.text_box.configure(highlightthickness=6)

        else:
            self.text_box.configure(highlightcolor="green", highlightthickness=1)
            self.time = 0

        self.text_len_check = self.text_len
        self.timer_count(None)

    # Count the words
    def word_count(self, _event):
        self.counter = int(len(self.text_box.get("1.0", END).split(" ")))
        self.word_counter.configure(text=f"{self.counter} Words")