# import os
# from tkinter import Tk, Button, Label
# from PIL import Image, ImageTk

# class ImageViewer:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Image Viewer")
#         self.master.geometry('400x300')
#         self.image_dir = f"/Users/amirkhan/Python Development/python academic"  # Directory containing images
#         self.images = self.load_images()
#         self.current_index = 0

#         self.image_label = Label(self.master)
#         self.image_label.grid(row=0, column=0, columnspan=2)

#         self.prev_button = Button(self.master, text="Previous", command=self.show_previous)
#         self.prev_button.grid(row=1, column=0)

#         self.next_button = Button(self.master, text="Next", command=self.show_next)
#         self.next_button.grid(row=1, column=1)

#         self.show_image()

#     def load_images(self):
#         images = []
#         for filename in os.listdir(self.image_dir):
#             if filename.endswith(".jpg") or filename.endswith(".png"):
#                 image_path = os.path.join(self.image_dir, filename)
#                 img = Image.open(image_path)
#                 images.append(img)
#         return images

#     def show_image(self):
#         image = self.images[self.current_index]
#         photo = ImageTk.PhotoImage(image)
#         self.image_label.config(image=photo)
#         self.image_label.image = photo

#     def show_previous(self):
#         self.current_index = (self.current_index - 1) % len(self.images)
#         self.show_image()

#     def show_next(self):
#         self.current_index = (self.current_index + 1) % len(self.images)
#         self.show_image()

# if __name__ == "__main__":
#     root = Tk()
#     image_viewer = ImageViewer(root)
#     root.mainloop()
import os
from tkinter import Tk, Button, Label, Frame
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")
        self.image_dir = f"/Users/amirkhan/Python Development/python academic"  # Directory containing images
        self.images = self.load_images()
        self.current_index = 0

        self.image_frame = Frame(self.master)
        self.image_frame.pack(pady=10)

        self.image_label = Label(self.image_frame, width=400, height=400)
        self.image_label.pack()

        self.button_frame = Frame(self.master)
        self.button_frame.pack(pady=10)

        self.prev_button = Button(self.button_frame, text="Previous", command=self.show_previous)
        self.prev_button.pack(side="left", padx=10)

        self.next_button = Button(self.button_frame, text="Next", command=self.show_next)
        self.next_button.pack(side="right", padx=10)

        self.show_image()

    def load_images(self):
        images = []
        for filename in os.listdir(self.image_dir):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                image_path = os.path.join(self.image_dir, filename)
                img = Image.open(image_path)
                images.append(img)
        return images

    def show_image(self):
        image = self.images[self.current_index]
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def show_previous(self):
        self.current_index = (self.current_index - 1) % len(self.images)
        self.show_image()

    def show_next(self):
        self.current_index = (self.current_index + 1) % len(self.images)
        self.show_image()

if __name__ == "__main__":
    root = Tk()
    image_viewer = ImageViewer(root)
    root.mainloop()
