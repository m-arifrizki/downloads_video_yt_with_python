# import required 
import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from cv2 import dft
from pytube import YouTube

def createwidgits():
    # creating a button
    link_label = Label(root, text ='Paste URL: ', bg=('gray'))
    # placing the label
    link_label.grid(row=1, column=0, pady=10, padx=10)

    # creating a entry point
    root.link_text = Entry(root, width=60 , textvariable=video_link)
    # placing the point
    root.link_text.grid(row=1, column=1,pady=10, padx=10)

    # creating a destination label
    destination_label = Label(root, text ='Destination: ', bg=('gray'))
    # placing the label
    destination_label.grid(row=2, column=0, pady=10, padx=10)

    # creating a destination box
    root.destination_label = Entry(root, width=60 , textvariable=Download_path)
    # placing the box
    root.destination_label.grid(row=2, column=1,pady=10, padx=10)

    # create a browse button
    browse_but = Button(root, text="Browse", command=browse, width=10, bg=('green'))
    # place the button
    browse_but.grid(row=2, column=2, pady=10, padx=10)

    # create a download button
    download_but = Button(root, text="Download", command=download_video, width=15, bg=('green'))
    # place the button
    download_but.grid(row=3, column=1, pady=3, padx=3)

# define browse button function
def browse():
    # set directory
    downlaod_dir = filedialog.askdirectory(initialdir="Downlaod path")
    Download_path.set(downlaod_dir)

# create youtube video download function
def download_video():

    url = video_link.get()
    folder = Download_path.get()
    get_video = YouTube(url)
    get_stream = get_video.streams.filter(progressive=True, file_extension='mp4').desc().first().download(folder)

    messagebox.showinfo("Your video downloaded successfully")

# creating an instance
root = tk.Tk()

# size of the window
root.geometry("730x200")
root.resizable(False,False)
# name of the window
root.title("Download_YouTube")
# colors of the window
root.config(background=('black'))

video_link = StringVar()
Download_path = StringVar()

createwidgits()

root.mainloop()
