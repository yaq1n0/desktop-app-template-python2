# module imports
from PIL import Image, ImageTk


def create_tk_image(path, x_size, y_size):
    """function to create a Tk compatible image with the given path and x_size and y_size"""
    img_open = Image.open(path)
    img_resized = img_open.resize((x_size, y_size))
    img_tk = ImageTk.PhotoImage(img_resized)
    return img_tk


if __name__ == '__main__':
    """module unit test, create Tk window with test image"""
    from tkinter import Tk, Label
    from lib.functions.makeGeometry import make_geometry

    test_root = Tk()
    test_root.geometry(make_geometry(test_root, 500, 500))
    _img = create_tk_image('../../resources/test.png', 500, 500)
    picture_label = Label(test_root, image=_img)
    picture_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    test_root.mainloop()
