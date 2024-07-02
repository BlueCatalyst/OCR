from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pytesseract as tesseract

tesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

root = None
panel = None
text = None


def open_file():
    filename = filedialog.askopenfilename(title='open')
    return filename


def open_image():
    filename = open_file()
    image = Image.open(filename)
    image = image.resize((640, 350))
    image = ImageTk.PhotoImage(image)
    panel = Label(root, image=image)
    panel.image = image
    panel.pack()
    recognized_text = tesseract.image_to_string(Image.open(filename))
    text = Text(root, wrap=WORD)
    text.insert(INSERT, recognized_text)
    text.pack()
    text.config(state=NORMAL)
    return panel, text


def create_gui():
    root = Tk()
    root.title("Image OCR")
    root.geometry("640x500")
    root.resizable(width=True, height=True)
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_image)
    filemenu.add_command(label="Close", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    root.mainloop()


create_gui()