from tkinter import *
from PIL import Image,ImageTk
from tkinter import font as tkFont
root=Tk()
root.title("image viewer")
root.iconbitmap("C:/Users/KISHOREGANESH S/Desktop/important shit/py GUI/hi.ico")
helv36 = tkFont.Font(family='Helvetica', size=45, weight='bold')
idx=0 #global
img0=ImageTk.PhotoImage(Image.open("img/0.png"))
img1=ImageTk.PhotoImage(Image.open("img/1.png"))
img2=ImageTk.PhotoImage(Image.open("img/2.png"))
img3=ImageTk.PhotoImage(Image.open("img/3.png"))
img4=ImageTk.PhotoImage(Image.open("img/4.png"))

imglist=[img0,img1,img2,img3,img4]

mylabel0=Label(image=imglist[idx],borderwidth=50,bg="black")
mylabel0.grid(row=0,column=0,columnspan=3)

def Next():
	global idx
	global mylabel0
	if idx<len(imglist)-1:
		idx=idx+1


	mylabel0.grid_forget()
	mylabel0=Label(image=imglist[idx],borderwidth=50,bg="black")
	mylabel0.grid(row=0,column=0,columnspan=3)
	button_back=Button(root,font="helv36",text="< Back",command=Back,padx=60,pady=20,bg="#008CBA",fg="#FFFFFF")
	button_back.grid(row=1,column=0)
	


	if idx>=len(imglist)-1:
		button_next=Button(root,font="helv36",text="Next >",state=DISABLED,padx=60,pady=20,bg="#008CBA",fg="#FFFFFF")
		button_next.grid(row=1,column=2)


def Back():
	global idx
	global mylabel0
	if idx>0 and idx<=len(imglist)-1:
		idx=idx-1
	mylabel0.grid_forget()
	mylabel0=Label(image=imglist[idx],borderwidth=50,bg="black")
	mylabel0.grid(row=0,column=0,columnspan=3)
	button_next=Button(root,font="helv36",text="Next >",command=Next,padx=60,pady=20,bg="#008CBA",fg="#FFFFFF")
	button_next.grid(row=1,column=2)



	if idx==0:
		button_back=Button(root,font="helv36",text="< Back",state=DISABLED,padx=60,pady=20,bg="#008CBA",fg="#FFFFFF")
		button_back.grid(row=1,column=0)



	



button_back=Button(root,font="helv36",text="< Back",command=Back,state=DISABLED,padx=60,pady=20,)
button_quit=Button(root,font="helv36",text="EXIT",command=root.quit,padx=60,pady=20,bg="#ff0000",fg="#FFFFFF")
button_next=Button(root,font="helv36",text="Next >",command=Next,padx=60,pady=20,bg="#008CBA",fg="#FFFFFF")


button_back.grid(row=1,column=0) 
button_quit.grid(row=1,column=1)
button_next.grid(row=1,column=2)
root.mainloop()