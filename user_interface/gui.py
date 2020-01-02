from tkinter import *
from tkinter import messagebox
from algorithm import get_plate_temperature


class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title('Course work')
        master.geometry("640x700")
        master.resizable(False, False)

        canvas = Canvas(master=master)
        canvas.create_rectangle(0, 450, 450, 50, outline="#fb0", fill="#fb0")
        canvas.pack()

        self.__temperatures = ['right', 'left', 'top', 'bottom']

        # String variables for entries
        self._s_temps = {temp: StringVar() for temp in self.__temperatures}
        self._s_size = (StringVar(), StringVar())

        # Entries and labels grid
        self._create_entries()

        # Buttons
        self.get_result_btn = Button(master, text='get result', pady=10,
                                     command=lambda: self.command_get_temperature(self._s_size, **self._s_temps)).pack()

    def _create_entries(self):
        # right, left
        right_label = Label(text=self.__temperatures[0])
        right_label.place(relx=0.85, rely=0.2)

        right_entry = Entry(master=self.master, textvariable=self._s_temps['right'], relief=SUNKEN, width=4)
        right_entry.place(relx=0.85, rely=0.25)

        left_label = Label(text=self.__temperatures[1])
        left_label.place(relx=0.1, rely=0.2)

        left_entry = Entry(master=self.master, textvariable=self._s_temps['left'], relief=SUNKEN, width=4)
        left_entry.place(relx=0.1, rely=0.25)

        # top, bottom
        top_label = Label(text=self.__temperatures[2])
        top_label.place(relx=0.48, rely=0)

        top_entry = Entry(master=self.master, textvariable=self._s_temps['top'], relief=SUNKEN, width=4)
        top_entry.place(relx=0.48, rely=0.04)

        bottom_entry = Entry(master=self.master, textvariable=self._s_temps['bottom'], relief=SUNKEN, width=4)
        bottom_entry.place(relx=0.5, rely=0.4)

        bottom_label = Label(text=self.__temperatures[3], pady=5)
        bottom_label.place(relx=0.5, rely=0.4)

        bottom_entry.pack()
        bottom_label.pack()

        # grid for width and height
        Label(text='width', pady=10).pack()
        Entry(master=self.master, textvariable=self._s_size[0], relief=SUNKEN).pack()

        Label(text='height',  pady=10).pack()
        Entry(master=self.master, textvariable=self._s_size[1], relief=SUNKEN).pack()

    @staticmethod
    def command_get_temperature(size, **kwargs):
        try:
            arguments = {key: float(value.get()) for key, value in kwargs.items()}
            size = (float(size[0].get()), float(size[1].get()))
        except ValueError:
            messagebox.showerror('Invalid input', 'Values must be a number')
        else:
            temp_matrix = get_plate_temperature(size, **arguments)
            TopWindow(temp_matrix)


class TopWindow:
    def __init__(self, temperature_matrix):
        self.top_window = Toplevel()
        self.top_window.title('Result')
        self.temp_matrix = temperature_matrix
        self.create_grid_temp()

    def create_grid_temp(self):
        for i in range(len(self.temp_matrix)):
            for j in range(len(self.temp_matrix[i])):
                Label(text=self.temp_matrix[i][j],
                      master=self.top_window, relief=SUNKEN).grid(row=i, column=j, pady=10, padx=10)
