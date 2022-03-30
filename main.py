from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("500x750")  # for setting the dimension of frame.
root.title("Screen Rec")  # for setting the title.
# bg = PhotoImage(file="Background.png")
root.config(bg="#fff")  # for setting the bg color.
root.resizable(False, False)  # this allows us to resize the window.


def start_rec():  # fcn to start recording with desired filename.
    file = Filename.get()
    rec.start_recording(str(file + ".mp4"), 5)  # converts the file to .mp4 format


def pause_rec():  # fcn to pause recording.
    rec.pause_recording()


def play_rec():  # fcn to resume recording.
    rec.play_recording()


def stop_rec():  # fcn to stop recording.
    rec.stop_recording()


rec = pyscreenrec.ScreenRecorder()  # fcn which triggers recording.

#  Title Icon
image_icon = PhotoImage(file="Title.png")  # inserting the file to window.
root.iconphoto(False, image_icon)  # adding inserted image(icon) into frame(titlebar)

#  Background
image_bg = PhotoImage(file="BG-01.png", width=500, height=750)  # adding image to window
Label(root, image=image_bg, bg="#fff").place(x=-1, y=-1)  # adding image to frame.

#  Heading
lbl = Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold")  # sets the heading
lbl.pack(pady=20)  # adding a heading.

centImg = PhotoImage(file="CentreImg-01.png")  # adds centre frame.
Label(root, image=centImg, bd=0).pack(pady=30)

#  Entry
Filename = StringVar()  # field to add name of a file.
entry = Entry(root, textvariable=Filename, width=18, font="arial 15")
entry.place(x=110, y=570)
Filename.set("        Display Name")

#  Buttons
start = Button(root, text="Start", bg="#FFF797", font="arial 22", bd=0, command=start_rec)
start.place(x=190, y=120)

imgPause = PhotoImage(file="pause.png")
pause = Button(root, image=imgPause, bd=0, bg="#FFF797", command=pause_rec)
pause.place(x=135, y=500)

imgPlay = PhotoImage(file="play.png")
play = Button(root, image=imgPlay, bd=0, bg="#FFF797", command=play_rec)
play.place(x=205, y=489)

imgStop = PhotoImage(file="stop.png")
stop = Button(root, image=imgStop, bd=0, bg="#FFF797", command=stop_rec)
stop.place(x=295, y=500)

root.mainloop()  # this function lets us execute the application.
