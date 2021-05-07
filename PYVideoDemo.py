# import...
'''
How To Install TKDND2
Video Link : https://www.youtube.com/watch?v=JIy0QjwQBl0
'''
from TkinterDnD2 import DND_FILES, TkinterDnD
import tkinter as tk

'''
For Installing cv2 Type
pip install opencv-python
'''
import cv2

# root-functions

root = TkinterDnD.Tk()
root.resizable(0, 0)
root.geometry('600x300')
# root.overrideredirect(1)
root.attributes('-alpha', 0.79)
root.attributes('-fullscreen', True)
root.config(bg='#fff')


# function
def drop_(e):
    global v, vid
    vid = cv2.VideoCapture(e.data)
    v = 1
    # webbrowser.open(e.data)
    video['width'] = 1300
    video['height'] = 1000
    # video['text'] = ''


# video
v = 0
img = tk.PhotoImage(None)
vid = cv2.VideoCapture(None)
video = tk.Label(border=1, image=None, text='Drag Video', justify='center', bg='#fff', fg='#333', font=(50), width=20,
                 height=15)
text_label = tk.Entry(border=0, bg='#fff', fg='#333', font=(50), width=22)
text_label.insert('end', 'Drag Video To Play In App')
text_label.grid(row=0, column=0)
video.grid(row=0, column=1)
# function
video.drop_target_register(DND_FILES)
video.dnd_bind('<<Drop>>', drop_)
# main-loop-while-loop

while True:
    root.update()
    root.update_idletasks()
    if v == 0:
        pass
    if v == 1:
        cap, cam = vid.read()
        cv2.imwrite('vid_v.png', cam)
        img = tk.PhotoImage(file='vid_v.png')
        video['image'] = img
        root.update_idletasks()
        root.update()
