import tkinter
import cv2
import PIL.Image, PIL.ImageTk

class App:
    def __init__(self, window, window_title, image_path="samples/ID_1_B.jpg"):
        self.window = window
        self.window.title(window_title)

        # Load an image using OpenCv
        self.cv_img = cv2.imread(image_path)

        # Percent by which the image is resized
        self.scale_percent = 50

        self.width = int(self.cv_img.shape[1] * self.scale_percent / 100)
        self.height = int(self.cv_img.shape[0] * self.scale_percent / 100)

        self.dsize = (self.width, self.height)

        self.output = cv2.resize(self.cv_img, self.dsize)

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        #self.height, self.width, no_channels = self.cv_img.shape
        self.height, self.width, no_channels = self.output.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.output))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Button that lets the user blur the image
        self.btn_blur=tkinter.Button(window, text="Blur", width=50, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)

        self.window.mainloop()

    # Callback for the "Blur" button
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (3,3))
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0,0, image=self.photo, anchor=tkinter.NW)


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")
