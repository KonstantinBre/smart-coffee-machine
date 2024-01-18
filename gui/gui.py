import cv2
import tkinter as tk
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
        # Erstelle ein Label für die Überschrift
        self.title_label = tk.Label(window, text="Webcam App", font=("Helvetica", 16))
        self.title_label.pack(pady=40)  # pady für vertikalen Abstand
        
        # Öffne die Kamera
        self.cap = cv2.VideoCapture(1)
        
        # Initialisiere das Tkinter-Label, um das Kamerabild anzuzeigen
        self.label = tk.Label(window)
        self.label.pack(padx=10, pady=10)
        
        
        # Button zum Schließen der App
        self.close_button = tk.Button(window, text="Beenden", command=self.close)
        self.close_button.pack(padx=10, pady=10)
        
        # Aktualisiere das Kamerabild in regelmäßigen Abständen
        self.update()

    def update(self):
        # Lies ein Frame von der Kamera
        ret, frame = self.cap.read()

        # Konvertiere das OpenCV-Frame zu einem Tkinter-Bild
        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image=image)
            self.label.photo = photo
            self.label.config(image=photo)
            self.window.after(10, self.update)  # Aktualisiere alle 10 Millisekunden

    def close(self):
        # Stoppe die Kamera und schließe das Fenster
        self.cap.release()
        self.window.destroy()

# Erstelle die Tkinter-App und starte das Hauptfenster
root = tk.Tk()
app = WebcamApp(root, "Webcam App")
root.mainloop()
