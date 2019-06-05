import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from imgdft import filter_img

def start():
    root = tk.Tk()
    root.title('RayosX')

    Application(root)

    root.mainloop()


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.pack()

        self.imgpath = None

    def create_widgets(self):
        # Frames
        # self.frame_buttons = tk.Frame(self)

        # Entrada de archivo
        self.lbl_file = tk.Label(self, text='Ruta de archivo')
        self.entry_imagepath = tk.Entry(self, width=75)
        self.btn_browse = tk.Button(self, text='Examinar')
        self.btn_load = tk.Button(self, text='Cargar')
        # Grid configure
        self.lbl_file.grid(row=0, column=0)
        self.entry_imagepath.grid(row=0, column=1, columnspan=2)
        self.btn_browse.grid(row=0, column=3)
        self.btn_load.grid(row=0, column=4)

        # Renglón para filtros
        self.lbl_filter = tk.Label(self, text='Valor de corte:')
        self.entry_wf = tk.Entry(self)
        self.entry_wf.insert(0, '15')
        self.btn_filter = tk.Button(self, text='Filtrar')
        # Grif configure
        self.lbl_filter.grid(row=1, column=0)
        self.entry_wf.grid(row=1, column=1)
        self.btn_filter.grid(row=1,column=4)

        self.frame_img = tk.Frame(self)
        self.frame_img.grid(row=2, columnspan=5)

        # Eventos
        self.btn_browse.bind('<Button-1>', self.__browse_event)
        self.btn_load.bind('<Button-1>', self.__load_image)
        self.btn_filter.bind('<Button-1>', self.__execute_ft)



    def __browse_event(self, event):
        file = filedialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        if file:
            self.entry_imagepath.delete(0, tk.END)
            self.entry_imagepath.insert(0, file.name)

    def __load_image(self, event):
        self.__limpiar_frame()

        filename = self.entry_imagepath.get()
        self.imgpath = filename
        render = ImageTk.PhotoImage(Image.open(filename).resize((600,600)), '500x500')
        lbl_image = tk.Label(self.frame_img, image=render)
        lbl_image.image = render
        lbl_image.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

    def __execute_ft(self, event):
        wf = float(self.entry_wf.get())
        print(wf)
        filter_img(self.imgpath, wf)

        self.__limpiar_frame()
        render = ImageTk.PhotoImage(Image.open('resultado.png').resize((600,600)), '500x500')
        lbl_image = tk.Label(self.frame_img, image=render)
        lbl_image.image = render
        lbl_image.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

    def __limpiar_frame(self):
        for w in self.frame_img.winfo_children():
            w.destroy()