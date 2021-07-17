from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import select

Folder_Name = ""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
        
    else:
        locationError.config(text="Please Choose Folder!!",fg="red")
        
        
#download_video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    
    
    if(len(url)> 1):
        ytdError.config(text="")
        yt = YouTube(url)
        
        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
            
            
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()
            
            
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
            
            
        else:
            ytdError.config(text="Paste Link Again!!",fg="red")
            
            
            
            
            
        #download_function
        select.download(Folder_Name)
        ytdError.config(text="Download Completed")
            
            
            


root = Tk ()
root.title("YouTube Downloader")
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1) #set all content in center


#Ytd link Label
ytdLabel = Label(root,text="Enter The URL Of The Video",font=("jost",15))
ytdLabel.grid()


#EntryBox
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()


#Error_Msg
ytdError = Label(root,text="Error Msg",fg="Red",font=("jost",10))
ytdError.grid()

#asking_save_file_label
saveLabel = Label(root,text="Save The Video File",font=("jost",15,"bold"))
saveLabel.grid()


#btn_save_file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error_msg_location
locationError = Label(root,text="Error Msg Of Path",fg="red",font=("jost",10))
locationError.grid()


#Download_Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()


#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#Download_btn
downloadBtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadBtn.grid()

#Developer_Label
developerLabel  = Label(root,text="Jaysinh Dabhi",font=("jost",15))
developerLabel.grid()

root.mainloop()
