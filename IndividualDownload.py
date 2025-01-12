import customtkinter as ct
import os
from yt_dlp import YoutubeDL

def DownloadIndividual(URL, OutputPath):
    # Specify the path to ffmpeg if it's not in the system's PATH
    ffmpeg_path = 'C:\\ffmpeg\\bin'  # Example path on Windows
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(OutputPath, '%(title)s.%(ext)s'),
        'ffmpeg_location': 'C:/ffmpeg',  
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])

def IndividualURL(frame, BackButton):
    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Configure grid to center the widgets
    frame.grid_rowconfigure(0, weight=1)  # Space above title
    frame.grid_rowconfigure(1, weight=0)  # Title row
    frame.grid_rowconfigure(2, weight=0)  # Entry row
    frame.grid_rowconfigure(3, weight=0)  # Buttons
    frame.grid_rowconfigure(4, weight=1)  # Space below
    frame.grid_columnconfigure(0, weight=1)  # Center column

    # Back button
    Back = ct.CTkButton(master=frame, text="Back", command=BackButton)
    Back.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    TitleLabel = ct.CTkLabel(master=frame, text="Individual Download", font=("Arial", 24))
    TitleLabel.grid(row=1, column=0, pady=(10, 5), sticky="n")

    # URL entry
    URLField = ct.CTkEntry(master=frame, placeholder_text="Enter YouTube URL")
    URLField.grid(row=2, column=0, pady=10, sticky="n")

    # Download button
    OutputPath= 'Music'
    DownloadButton = ct.CTkButton(master=frame, text="Download", command=lambda: DownloadIndividual(URLField.get(), OutputPath))
    DownloadButton.grid(row=3, column=0, pady=(20, 10), sticky="n")
