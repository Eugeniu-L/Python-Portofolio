from tkinter import Tk, PhotoImage, Label, Frame, END, DISABLED, Text, WORD, FLAT, messagebox, Button
from tkmacosx import Button
from words import get_random_words


class App(Tk):

    def __init__(self):
        super().__init__()

        # Main window attributes
        self.geometry("800x600")
        self.title("Typing Speed Test")
        self.words = get_random_words("files/words")
        self.configure(background="#F2DEBA")

        # Button Images
        self.button_image = PhotoImage(file="images/start.png").subsample(2, 2)
        self.button_image2 = PhotoImage(file="images/writing.png").subsample(8, 8)

        with open("files/best_score", "r") as data:
            best_score = data.readline().strip()

        # Initialisation of score variable
        self.timer = 60
        self.best_score = int(best_score)
        self.corrected_cpm = 0
        self.cpm = 0
        self.wpm = 0
        self.missed_words = 0
        self.typed_wrong = ""
        self.counter = 0

        # Frame for score detail
        self.frame_score = Frame(background="#FFEFD6", highlightthickness=0, highlightcolor="black")
        self.frame_score.pack(side="top", fill="x")

        # Label for Best Score
        self.label_best_score = Label(self.frame_score, text=f"Your best: {self.best_score}",
                                      background="#FFEFD6", foreground="#0E5E6F")
        self.label_best_score.pack()

        # Label for Correct Character Per Minute score
        self.label_correct_cpm = Label(self.frame_score, text=f"Corrected CPM: {self.corrected_cpm}", padx=10,
                                       background="#FFEFD6", foreground="#0E5E6F")
        self.label_correct_cpm.pack()

        # Label for Word Per Minute score
        self.label_wpm = Label(self.frame_score, text=f"WPM: {self.wpm}", padx=10,
                               background="#FFEFD6", foreground="#0E5E6F")
        self.label_wpm.pack()

        # Frame for Text Box with range words
        self.frame_words = Frame(background="#F2DEBA", pady=30, highlightthickness=0)
        self.frame_words.pack(fill="x")

        # Text Box
        self.text_box = Text(self.frame_words, wrap=WORD, background="#F2DEBA", height=9,
                             font="Arial 18 normal", foreground="#0E5E6F", relief=FLAT, highlightthickness=0)
        self.text_box.insert(END, self.words)
        self.text_box.configure(state=DISABLED)
        self.text_box.pack(fill="x", padx=25)
        self.text_box.tag_configure("right", background="#FFEFD6")
        self.text_box.tag_configure("wrong", background="red")

        # Frame for Insert text box and Button
        self.frame_insert = Frame(background="#F2DEBA", pady=5)
        self.frame_insert.pack(fill="x")

        # Start Button
        self.button = Button(self.frame_insert, image=self.button_image2, bg="#FFEFD6", borderless=1,
                             command=self.click_button)
        self.button.pack(pady=2)

        # Timer Label
        self.label_timer = Label(self.frame_insert, text=str(self.timer), font="Arial 20 bold", background="#F2DEBA",
                                 foreground="#0E5E6F")
        self.label_timer.pack(pady=5)

        # Text widget for text insert
        self.text_insert = Text(self.frame_insert, background="#F2DEBA", height=1, font="Arial 20 bold",
                                foreground="#3A8891", relief=FLAT, insertbackground="black", width=20,
                                highlightthickness=1, borderwidth=0, highlightcolor="#3A8891",
                                highlightbackground="#3A8891")
        self.text_insert.pack()
        self.text_insert.focus()
        self.text_insert.bind("<space>", self.get_start_event)
        self.text_insert.bind("<Return>", self.get_start_event)
        self.text_insert.bind("<Key>", self.timer_sub)

    def get_start_event(self, _event):
        text = self.text_insert.get("1.0", END).strip()
        text_len = len(text)
        self.cpm += text_len
        self.counter += 1
        if text in self.words:
            self.corrected_cpm += text_len
            pos_start = self.text_box.search(pattern=text, index="1.0", stopindex=END)
            pos_end = pos_start.split(".")[0] + "." + str(int(pos_start.split(".")[1]) + text_len)
            self.text_box.tag_add("right", pos_start, pos_end)
            self.wpm += 1
        else:
            self.typed_wrong += self.words[self.counter-1] + " "
            self.missed_words += 1
        self.text_insert.delete("1.0", END)

    def timer_sub(self, _event):
        if self.timer == 60:
            self.text_insert.unbind("<Key>")
            self.label_timer.after(1000, self.timer_count)
        elif self.timer == 0:
            self.text_insert.configure(state=DISABLED)
            self.button.configure(image=self.button_image)
            self.button.image = self.button_image
            self.label_timer.after(500, self.calculate_result)
        else:
            self.label_timer.after(1000, self.timer_count)

    def timer_count(self):
        self.timer -= 1
        self.label_timer.configure(text=str(self.timer))
        self.label_timer.text = str(self.timer)
        self.timer_sub(None)

    def calculate_result(self):
        self.label_correct_cpm.configure(text=f"The Correct CPM: {self.corrected_cpm}")
        self.label_wpm.configure(text=f"WPM: {self.wpm}")

        if self.best_score < self.corrected_cpm:
            self.best_score = self.corrected_cpm
            self.label_best_score.configure(text=f"Your best: {self.best_score}")
            self.show_message_box("best")
            with open("files/best_score", 'w') as data:
                data.write(str(self.best_score))
        else:
            self.show_message_box("normal")

    def show_message_box(self, mode):

        if mode == "best":
            messagebox.showinfo(title="New Record", message=f"Congratulations! You scored a new record!\n"
                                f"CPM: {self.corrected_cpm}\n"
                                f"WPM: {self.wpm}\n "
                                f"Missed No.Words: {self.missed_words}\n"
                                f"Missed Words: {self.typed_wrong}")

        else:
            messagebox.showinfo(title="Score", message=f"CPM: {self.corrected_cpm}\n"
                                f"WPM: {self.wpm}\n "
                                f"Missed No Words: {self.missed_words}\n"
                                f"Missed Words: {self.typed_wrong}")

    def click_button(self):
        self.destroy()
        self.__init__()
