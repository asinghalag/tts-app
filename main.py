from gtts import gTTS
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def text_to_speech_from_file():
    try:
        # Open file selection dialog
        root = tk.Tk()
        root.withdraw()  # hide root window
        file_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if not file_path:
            messagebox.showinfo("Cancelled", "No file selected.")
            return

        # Read text from file
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.strip():
            messagebox.showerror("Error", "The file is empty.")
            return

        # Ask for custom output filename
        filename = simpledialog.askstring("Save As", "Enter output filename (without extension):")
        if not filename:
            filename = "output"

        # Add .mp3 extension
        filename = filename.strip() + ".mp3"

        # Convert text to speech
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        messagebox.showinfo("Success", f"MP3 file saved as {filename}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    text_to_speech_from_file()
