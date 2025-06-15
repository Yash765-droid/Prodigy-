
import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

class QRScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Scanner")

        self.video = cv2.VideoCapture(0)

        self.label = tk.Label(self.root, text="Scan a QR Code", font=("Arial", 15))
        self.label.pack()

        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack()

        self.scan_button = tk.Button(self.root, text="Scan", command=self.scan_qr)
        self.scan_button.pack()

        self.open_link_button = tk.Button(self.root, text="Open Link", command=self.open_link, state=tk.DISABLED)
        self.open_link_button.pack()

        self.qr_data = None

    def scan_qr(self):
        ret, frame = self.video.read()
        if ret:
            decoded_objects = decode(frame)
            if decoded_objects:
                self.qr_data = decoded_objects[0].data.decode("utf-8")
                self.label.config(text=f"Scanned: {self.qr_data}")
                self.open_link_button.config(state=tk.NORMAL if self.qr_data.startswith("http") else tk.DISABLED)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            self.root.image = imgtk

        self.root.after(100, self.scan_qr)

    def open_link(self):
        if self.qr_data and self.qr_data.startswith("http"):
            webbrowser.open(self.qr_data)

    def __del__(self):
        self.video.release()

root = tk.Tk()
app = QRScanner(root)
root.mainloop()
