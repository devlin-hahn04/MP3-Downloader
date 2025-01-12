import customtkinter as ct
import requests
import tkinter as tk
from pytube import Playlist, YouTube
import os
from IndividualDownload import IndividualURL



ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')

root= ct.CTk()
root.geometry('800x400')



#Body
def BackButton():
    
    for widget in frame.winfo_children():
        widget.destroy()

    MainMenu()


def MainMenu():

    IndividualDonwload= ct.CTkButton(master= frame, text= "Individual Download", command= lambda: IndividualURL(frame, BackButton))
    IndividualDonwload.pack(pady=12, padx=10)


    PlaylistDownload= ct.CTkButton(master= frame, text= "Album Download")
    PlaylistDownload.pack(pady=14, padx=10)

















#Startup 
frame= ct.CTkFrame(master= root)
frame.pack(pady= 20, padx= 60, fill= "both", expand= True)



label= ct.CTkLabel(master= frame, text= "MP3 Downloader")
label.pack(pady= 12, padx= 10)

MainMenu()

root.mainloop()