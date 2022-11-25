import PIL.Image
from PIL import ImageTk
from tkinter import Tk, Label, LabelFrame, Toplevel, PhotoImage, BooleanVar, Menu, FLAT
from tkinter.filedialog import askopenfilename, asksaveasfilename


class App(Tk):
    # Create the Main Window
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.title("WaterMark")
        self.configure(pady=20, padx=20)
        self.image = PhotoImage(file="images/bg_photo.png")
        self.name = ""
        self.label_frame = LabelFrame(relief=FLAT)
        self.label_frame.pack(fill="both", expand=1)
        self.label = Label(self.label_frame, image=self.image)
        self.label.pack(fill="both", expand=1)
        self.check = BooleanVar()

    # Open the file from local machine and return the path
    def open_file(self, mode):
        filepath = askopenfilename(
            filetypes=[("All Files", "*.*")]
        )
        if mode == "primary":
            self.name = filepath.split(".")[0].split("/")[-1]
        return str(filepath)

    # Open and add a new waterMark image on primary image
    def add_water_mark(self, file_path):
        image = ImageTk.getimage(self.image)
        water_mark = PIL.Image.open(file_path).resize((100, 100))
        x, y = image.size
        image.paste(water_mark, (x-140, y-140))
        new_image = ImageTk.PhotoImage(image)
        self.label.configure(image=new_image)
        self.label.image = new_image
        self.image = new_image

    # Open the primary Image and upload on screen
    def add_image(self, file_path):
        new_image = PIL.Image.open(file_path)

        if new_image.width > self.winfo_screenwidth():
            new_image = new_image.resize((self.winfo_screenwidth()-20, int(new_image.height)))

        if new_image.height > self.winfo_screenheight():
            new_image = new_image.resize((int(new_image.width), self.winfo_screenheight()-20))

        new_image = ImageTk.PhotoImage(new_image)
        self.label.configure(image=new_image)
        self.label.image = new_image
        self.image = new_image

    # Save the Image from the screen
    def save_image(self):
        image = ImageTk.getimage(self.image)
        save_path = asksaveasfilename(defaultextension="png")
        image.save(save_path)
        if self.check.get():
            self.destroy()

    # Get a new window with both Version and Copyright Info
    def version(self):
        top = Toplevel(self.label_frame)
        top.title("Version")
        Label(top, text="Version: 1.0.0", font='Arial 18 bold').pack()
        Label(top, text='Copyright © EUGENIU Lupascu', font='Arial 18 bold').pack()

    # Create the bar for main window
    def create_bar(self):
        menubar = Menu()
        self.configure(menu=menubar)
        menu_items = Menu(menubar)
        menu_items_wm = Menu(menubar)
        menu_items_hp = Menu(menubar)

        menubar.add_cascade(
            label="File",
            menu=menu_items)

        menu_items.add_command(
            label="Open",
            command=lambda: self.add_image(file_path=self.open_file("primary"))
        )

        menu_items.add_command(
            label="Save",
            command=self.save_image
        )

        menu_items.add_checkbutton(
            label="Exit After Save", onvalue=1, offvalue=0, variable=self.check
        )

        menu_items.add_separator()

        menu_items.add_command(
            label="Exit",
            command=self.destroy
        )

        menubar.add_cascade(
            label="WaterMark",
            menu=menu_items_wm
        )

        menu_items_wm.add_command(
            label="Add WaterMark",
            command=lambda: self.add_water_mark(file_path=self.open_file("secondary"))
        )

        menubar.add_cascade(
            label="Help",
            menu=menu_items_hp
        )

        menu_items_hp.add_cascade(
            label="Version",
            command=self.version
        )
