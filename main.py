"""A program that opens a pop window after scanning the right QR code.
The popup window gives an entry space, where the user has to enter the full path of an image.
After hitting the enter button, the user will see a message if the path was successfully read or not.
If everything is successful, the user has to choose a button among the three provided ones.
Each button applies a 'filter' to the image.
The three 'filters' either make the image grayscale, add gaussian blur,
or remove the red channel pixels from the image. The newly generated images are saved locally."""

from functools import partial
import cv2
import tkinter as tk
import numpy as np
import os
import sys
import qrcode

sys.path.insert(0, os.path.abspath('../'))
# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('../../'))
#
# extensions = ['sphinx.ext.autodoc']


# def skip(app, what, name, obj, would_skip, options):
#     if name in ( '__init__',):
#         return False
#     return would_skip
#
#
# def setup(app):
#     app.connect('autodoc-skip-member', skip)


def gen_qr_codes():
    """
    Saves several generated QR codes
    """
    # QR code #1 the original
    qr1 = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=15,
        border=1,
    )
    qr1.add_data('scan me')
    qr1.make(fit=True)
    img = qr1.make_image(fill_color='black', back_color='white').convert('RGB')
    img.save('qr1.png')

    # QR code #2
    qr2 = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=1,
    )
    qr2.add_data('scan me')
    qr2.make(fit=True)
    img = qr2.make_image(fill_color='white', back_color='black').convert('RGB')
    img.save('qr2.png')

    # QR code #3
    qr3 = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=15,
        border=1,
    )
    qr3.add_data('do not scan me')
    qr3.make(fit=True)
    img = qr3.make_image(fill_color='black', back_color='white').convert('RGB')
    img.save('qr3.png')

    # QR code #4
    qr4 = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=15,
        border=1,
    )
    qr4.add_data('scan me')
    qr4.make(fit=True)
    img = qr4.make_image(fill_color='black', back_color='white').convert('RGB')
    img.save('qr4.png')


def enter_path(label_result, entry_path):
    """
    Outputs the image path
    :param label_result
    :param entry_path
    :return: A string that is the input in the entry section
    :rtype: str
    """
    path = (entry_path.get())
    label_result.config(text=path + ' path successfully read')

    return path


def enter_qr_path(label_result, entry_qr_path):
    """
    Checks if the inputted QR path matches with the original one
    :param label_result
    :param entry_qr_path
    :return: A string that states whether the inputted QR path is right or wrong and gives a corresponding instruction
    :rtype: str
    """
    img_orig = cv2.imread('qr1.png')
    det_orig = cv2.QRCodeDetector()
    val_orig, pts_orig, st_code_orig = det_orig.detectAndDecode(img_orig)

    path = (entry_qr_path.get())

    img_2 = cv2.imread(path)
    det_2 = cv2.QRCodeDetector()
    val_2, pts_2, st_code_2 = det_2.detectAndDecode(img_2)

    if val_2 == val_orig and pts_2.all() == pts_orig.all() and st_code_2.all() == st_code_orig.all():
        label_result.config(text='QRs match, press Quit')
    else:
        label_result.config(text='Input the right QR path')


def gray(label_result):
    """
    Converts the image to grayscale
    :param label_result:
    :return: An image with the filter saved locally
    """
    img = cv2.imread(enter_path())
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_path = 'gray.jpg'
    cv2.imwrite(gray_path, gray_img)
    label_result.config(text='Image successfully saved')


def gaus_blur(label_result):
    """
    Adds Gaussian Blur to the image
    :param label_result:
    :return: An image with the filter saved locally
    """
    img = cv2.imread(enter_path())
    gaus_img = cv2.GaussianBlur(img, (63, 63), 10)
    gaus_path = 'gaus.jpg'
    cv2.imwrite(gaus_path, gaus_img)
    label_result.config(text='Image successfully saved')


def remove_red(label_result):
    """
    Removes the red channel pixels from the image
    :param label_result:
    :return: An image with the filter saved locally
    """
    img = cv2.imread(enter_path())
    c_img_arr = np.array(img, np.uint8)
    c_img_arr[::, ::, 0] = 0
    remove_red_path = 'remove_red.jpg'
    cv2.imwrite(remove_red_path, c_img_arr)
    label_result.config(text='Image successfully saved')


if __name__ == "__main__":

    # Calling the function to generate the QR codes
    gen_qr_codes()

    # Creating the popup window for validating a QR code
    qr_root = tk.Tk()
    qr_root.geometry('500x500')
    qr_root.title('Verifying a QR code')
    qr_path = tk.StringVar()

    labelQRPath = tk.Label(qr_root, text='Please input a QR path', font=30).place(x=20, y=20)

    labelResultQR = tk.Label(qr_root)
    labelResultQR.place(x=300, y=90)

    # Input path place for the QR
    entry_qr_path = tk.Entry(qr_root, textvariable=qr_path).place(x=300, y=20)

    enter_qr_path = partial(enter_qr_path, labelResultQR, qr_path)

    # Enter button for the QR path and Quit button in case paths match
    qr_path_button = tk.Button(qr_root, text='Enter', command=enter_qr_path).place(x=300, y=50)
    tk.Button(qr_root, text="Quit", command=qr_root.destroy).place(x=300, y=120)
    qr_root.mainloop()

    # creating the popup window for Image Filtering

    root = tk.Tk()
    root.geometry('700x700')
    root.title('Image Filtering')
    path = tk.StringVar()

    # Labels for printing the needed text
    labelEntryPath = tk.Label(root, text='Please input an image path', font=30).place(x=20, y=20)

    labelResultEnter = tk.Label(root)
    labelResultEnter.place(x=300, y=90)

    labelResultGray = tk.Label(root)
    labelResultGray.place(x=30, y=150)

    labelResultGaus = tk.Label(root)
    labelResultGaus.place(x=280, y=150)

    labelResultRemRed = tk.Label(root)
    labelResultRemRed.place(x=500, y=150)

    # Input path place for the image
    entry_path = tk.Entry(root, textvariable=path).place(x=300, y=20)

    # Partial functions for adding text(image successfully saved)
    enter_path = partial(enter_path, labelResultEnter, path)
    gray = partial(gray, labelResultGray)
    gaus_blur = partial(gaus_blur, labelResultGaus)
    remove_red = partial(remove_red, labelResultRemRed)

    # Buttons
    path_button = tk.Button(root, text='Enter', command=enter_path).place(x=300, y=50)
    gray_button = tk.Button(root, text='Grayscale', command=gray).place(x=30, y=120)
    gaus_blur_button = tk.Button(root, text='Gaussian Blur', command=gaus_blur).place(x=280, y=120)
    remove_red_button = tk.Button(root, text='Remove red channel', command=remove_red).place(x=500, y=120)

    root.mainloop()
