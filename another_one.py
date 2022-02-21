# IMPORTING DIFFERENT LIBRARIES

from tkinter import *        #This library will help me to make GUI (Graphical User Interface)
from pytube import YouTube   #Please make sure you have the pytube library installed in your directory.
                             #To install open terminal and paste the following code (see below):
                             #pip install pytube

def download():

    link = ENTER_LINK_FIELD.get()       #FETCHING THE LINK ENTERED BY THE USER
    save_path = "E:/"     #THE VIDEO WILL BE DOWNLOADED IN 'E:/' DRIVE
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()    #IT WILL FETCH THE HIGHEST RESOLUTION OF THE VIDEO POSSIBLE

    ys.download(save_path)     #DOWNLOADING THE FILE IN THE DEFINED PATH

    DOWNLOAD_FINISHED_LABEL = Label(Sparsh_Root, text = "Download Finished", font = ('Bahnschrift 12 bold'))
    DOWNLOAD_FINISHED_LABEL.pack(side = BOTTOM)


# CREATING GUI (TKINTER) WINDOW

Sparsh_Root = Tk()
Sparsh_Root.title("Main")
Sparsh_Root.geometry("800x600")



# CREATING TITLE LABEL

TITLE_LABEL = Label(Sparsh_Root, text = "Download YouTube Videos Easily!", font = ('Algerian 19 bold italic underline'))
TITLE_LABEL.pack()

PASTE_THE_LINK_LABEL = Label(Sparsh_Root, text = "Paste the YouTube video link below", font =('Bahnschrift 15 bold'))
PASTE_THE_LINK_LABEL.pack()

# MAKING THE BOX TO ENTER THE LINKS INTO
ENTER_LINK_FIELD = Entry(Sparsh_Root)
ENTER_LINK_FIELD.pack()

# MAKING THE DOWNLOAD BUTTON
DOWNLOAD_BUTTON = Button(Sparsh_Root, text = "DOWNLOAD", fg = "Black", bg = "Red", activebackground = 'blue', font = ('Bahnschrift 15 bold'), command = download)
DOWNLOAD_BUTTON.pack()    #PACKING or 'DISPLAYING' THE DOWNLOAD BUTTON ON THE SCREEN

Sparsh_Root.mainloop()
