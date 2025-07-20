import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
import os

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🖼️ Simple Image Editor")
        self.root.geometry("600x500")

        self.img = None
        self.img_path = ""

        # UI Elements
        self.label = tk.Label(root, text="No Image Selected", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Label(root)
        self.canvas.pack()

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Open Image", command=self.open_image).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Rotate 90°", command=self.rotate_image).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Flip Horizontally", command=self.flip_image).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Grayscale", command=self.convert_gray).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Save Image", command=self.save_image).grid(row=0, column=4, padx=5)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
        if file_path:
            self.img_path = file_path
            self.img = Image.open(file_path)
            self.show_image(self.img)
            self.label.config(text=os.path.basename(file_path))

    def show_image(self, img):
        img_resized = img.resize((400, 300))
        self.tk_img = ImageTk.PhotoImage(img_resized)
        self.canvas.config(image=self.tk_img)

    def rotate_image(self):
        if self.img:
            self.img = self.img.rotate(90, expand=True)
            self.show_image(self.img)

    def flip_image(self):
        if self.img:
            self.img = ImageOps.mirror(self.img)
            self.show_image(self.img)

    def convert_gray(self):
        if self.img:
            self.img = ImageOps.grayscale(self.img)
            self.show_image(self.img)

    def save_image(self):
        if self.img:
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                self.img.save(save_path)
                messagebox.showinfo("Saved", f"Image saved at {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
