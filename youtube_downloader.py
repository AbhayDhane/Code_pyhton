import os
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        
        folder = filedialog.askdirectory(title="Select Download Folder")
        if folder:
            status_label.config(text="📥 Downloading...")
            stream.download(output_path=folder)
            messagebox.showinfo("Success", f"Downloaded:\n{yt.title}")
            status_label.config(text="✅ Download complete.")
        else:
            status_label.config(text="❌ Download canceled.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download:\n{e}")
        status_label.config(text="❌ Error occurred.")

# GUI setup
root = Tk()
root.title("🎬 YouTube Video Downloader")
root.geometry("500x200")

Label(root, text="Enter YouTube URL:", font=("Arial", 12)).pack(pady=10)
url_entry = Entry(root, width=60, font=("Arial", 12))
url_entry.pack()

Button(root, text="Download Video", font=("Arial", 12), command=download_video).pack(pady=10)
status_label = Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()
