import customtkinter as ct
import os
from yt_dlp import YoutubeDL
import subprocess


def AlbumDownload(playlist_url, AlbumName):
    # Ensure the output directory exists
    if not os.path.exists(AlbumName):
        os.makedirs(AlbumName)

    # Define yt-dlp options for audio download
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(AlbumName, '%(playlist_index)s - %(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
        'playlist_items': '1-',  # Download all items in the playlist
    }

    # Download playlist or album
    with YoutubeDL(ydl_opts) as ydl:
        print("Starting download...")
        ydl.download([playlist_url])


def AlbumURL(frame, BackButton):
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

    TitleLabel = ct.CTkLabel(master=frame, text="Album Download", font=("Arial", 24))
    TitleLabel.grid(row=1, column=0, pady=(10, 5), sticky="n")

    # URL entry
    URLField = ct.CTkEntry(master=frame, placeholder_text="Enter YouTube URL")
    URLField.grid(row=2, column=0, pady=10, sticky="n")

    #Album Folder Name
    AlbumName= ct.CTkEntry(master= frame, placeholder_text="Enter Album Name")
    AlbumName.grid(row=3, column=0, pady=10, sticky="n")

    # Download button
    DownloadButton = ct.CTkButton(master=frame, text="Download", command=lambda: AlbumDownload(URLField.get(), AlbumName.get()))
    DownloadButton.grid(row=4, column=0, pady=(20, 10), sticky="n")






