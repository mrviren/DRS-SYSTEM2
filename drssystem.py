import tkinter
import cv2
import PIL.Image, PIL.ImageTk


SET_WIDTH = 650
SET_HEIGHT = 430

window = tkinter.Tk()
window.title("Virendra Third Umpire Decision review Kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
#window.mainloop()
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)

canvas.pack()
btn = tkinter.Button(window, text="<< previous (fast)",width = 50)
btn.pack()
btn = tkinter.Button(window, text="<< previous (slow)",width = 50)
btn.pack()
btn = tkinter.Button(window, text="<< next (fast)",width = 50)
btn.pack()
btn = tkinter.Button(window, text="<< next (slow)",width = 50)
btn.pack()
window.mainloop()
