from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
root.title("TO DO LIST")


global j
j=1
conn = sqlite3.connect('todo.db')
c=conn.cursor()



c.execute("""CREATE TABLE IF NOT EXISTS todo (task text)""")



def rootclose():
	root.destroy()

def delpopup1():
	messagebox.showinfo("INFO","ENTER TASK ID TO DELETE")

def editpopup1():
	messagebox.showinfo("INFO","ENTER TASK ID TO EDIT")

def editpopup2():
	messagebox.showinfo("INFO","ENTER VALID TASK ID TO EDIT")

def add():
	global show_labelframe
	global labelframe_content
	global j

	
	conn = sqlite3.connect('todo.db')
	c=conn.cursor()
	if(add_entry.get()==""):
		response=messagebox.askyesno("warning","wanna enter empty Task?")
		if(response==1):
			c.execute("INSERT INTO todo Values (:task)",
				{
				'task':add_entry.get()
				})

			show_labelframe.destroy()
			labelframe_content.destroy()
		else:
			pass
	else:
		c.execute("INSERT INTO todo Values (:task)",
				{
				'task':add_entry.get()
				})
	add_entry.delete(0,END)	
	show_labelframe.destroy()
	labelframe_content.destroy()

	

	conn.commit()
	conn.close()
	show()

def delete():
	global show_labelframe
	global labelframe_content
	global j
	
	conn = sqlite3.connect('todo.db')
	c=conn.cursor()

	try:
		c.execute("DELETE from todo WHERE oid="+del_entry.get())
		del_entry.delete(0,END)
		j=j-1
		
		
	except sqlite3.OperationalError as e:
		delpopup1()


	show_labelframe.destroy()
	labelframe_content.destroy()	

	conn.commit()
	conn.close()
	show()

def show():


	global show_labelframe
	global labelframe_content
	global j

	conn = sqlite3.connect('todo.db')
	c=conn.cursor()
	c.execute("SELECT task,oid FROM todo")
	records=c.fetchall()
	print_records=''
	for record in records:
		print_records+="   "+str(record[1])+"    "+str(record[0])+","
	
	a=print_records.split(",")
	show_labelframe=LabelFrame(root,text="Your Tasks To Do")
	show_labelframe.grid(row=0,column=2,rowspan=6,columnspan=2)
	default_label=Label(show_labelframe,text="  ID  TASK")
	default_label.grid(row=0,column=0,sticky=W)
	for i in a:
		
		labelframe_content=Label(show_labelframe,text=i)
		
		labelframe_content.grid(row=j,column=0,columnspan=2,sticky=W)
		j=j+1

	conn.commit()
	conn.close()

def update():
	global edit 
	global r,n

	conn = sqlite3.connect('todo.db')
	c=conn.cursor()

	r=to_entry.get()
	n=edit_entry_edit.get()

	c.execute("""UPDATE todo SET task=:tasky WHERE oid=:oid""",{

		'tasky':r,
		'oid':n})
	edit.destroy()
	
	show_labelframe.destroy()
	labelframe_content.destroy()
	conn.commit()
	conn.close()
	show()
	
def edit():

	try:
		global to_entry
		global edit_entry_edit
		global r,n
		global edit
		global edit_entry
		conn = sqlite3.connect('todo.db')
		c=conn.cursor()
		edit=Tk()
		edit.title("Edit Task")

		
		edit_entry_label=Label(edit,text="Task ID:")
		edit_entry_edit=Entry(edit,width=5)
		to_label=Label(edit,text="To:")
		to_entry=Entry(edit,width=60)
		
		c.execute("SELECT task FROM todo WHERE oid="+edit_entry.get())
		r1=c.fetchone()
		r=str(r1[0])
		n=edit_entry.get()


		edit_entry_edit.insert(0,n)
		to_entry.insert(0,r)


		edit_btn_edit=Button(edit,text="edit task",fg="white",bg="#1E90FF",border=2,command=update)
		edit_entry_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
		edit_entry_edit.grid(row=0,column=1,padx=5,pady=5,sticky=W)
		to_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
		to_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
		edit_btn_edit.grid(row=1,column=0,columnspan=4,padx=10,pady=5,ipadx=169,ipady=10)


		conn.commit()
		conn.close()

		
	except sqlite3.OperationalError as e:
		edit.destroy()
		editpopup1()
	
	except TypeError as e:
		edit.destroy()
		editpopup2()

	edit_entry.delete(0,END)	
	edit.mainloop()



show()

global add_entry
global edit_entry
global del_entry

add_label=Label(root,text="Add a Task")
add_entry=Entry(root,width=50)
add_btn=Button(root,text="Add Task",fg="white",bg="#1E90FF",border=2,command=add)

edit_label=Label(root,text="Edit Id")
edit_entry=Entry(root,width=50)
edit_btn=Button(root,text="Edit Task",fg="white",bg="#1E90FF",border=2,command=edit)

del_label=Label(root,text="Delete Id")
del_entry=Entry(root,width=50)
del_btn=Button(root,text="Delete Task",fg="white",bg="#1E90FF",border=2,command=delete)

final_del_btn=Button(root,text="EXIT",fg="white",bg="#1E90FF",border=2,command=rootclose)




add_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
add_entry.grid(row=0,column=1,padx=10,pady=5)
add_btn.grid(row=1,column=0,padx=10,pady=5,columnspan=2,ipadx=167,ipady=10)

edit_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
edit_entry.grid(row=2,column=1,padx=10,pady=5)
edit_btn.grid(row=3,column=0,padx=10,pady=5,columnspan=2,ipadx=169,ipady=10)

del_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
del_entry.grid(row=4,column=1,padx=10,pady=5)
del_btn.grid(row=5,column=0,padx=10,pady=5,columnspan=2,ipadx=163,ipady=10)

#final_del_btn.grid(row=6,column=0,padx=10,pady=5,columnspan=2,ipadx=163,ipady=10)


conn.commit()
conn.close()
root.mainloop()