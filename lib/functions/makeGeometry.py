
def make_geometry(root, width, height):
    """function to generate tk-compatible geometry string from width and height"""
    x_pos = int((root.winfo_screenwidth() / 2) - (width / 2))
    y_pos = int((root.winfo_screenheight() / 2) - (height / 2))
    geometry_string = str(width) + 'x' + str(height) + '+' + str(x_pos) + '+' + str(y_pos)
    return geometry_string


if __name__ == '__main__':
    """module unit test, create test window of size 1280x720"""
    from tkinter import Tk
    test_root = Tk()
    test_geometry = make_geometry(test_root, 1280, 720)
    test_root.geometry(test_geometry)
    print('function output:', test_geometry)
    test_root.mainloop()
