import tkinter
from tkinter import  *
from tkinter import PhotoImage, Listbox, messagebox

root=Tk()
root.title("TO-DO-List")
fg= ' dark blue'
root.geometry("400x750+400+200")
root.resizable(False,False)

task_list= []

def addtask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("task.txt","a") as taskfile:
            taskfile.write(task+"\n(task)")
            task_list.append(task)
            listbox.insert(END,task)
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
         task_list.remove(task)
         with open("tasklist.txt","w") as taskfile:
                for task in task_list:
                    taskfile.write(task+"\n")
         listbox.delete(ANCHOR)
         messagebox.showinfo("Message", "Your task has been deleted")
         
def message():
          messagebox.showinfo("Message", "Your task has been added")
          task_entry.delete(0,END)
          task_entry.focus()

def openTaskFile():
    try:
        global task_list
        with open("task.txt","r") as taskfile:
            tasks = taskfile.readlines()
            for task in tasks:
                if task != "\n":
                    task_list.append(task)
                    listbox.insert(END, task)


               
    
    except:
        file=open('tasklist.txt', 'w')
        file.close()


heading=Label(root,text="To-Do-List",font="Italic",fg="white",bg="#7D34B1",padx=40,pady=10,relief=RAISED,anchor=W)
heading.place(x=130,y=50)
#main
frame=Frame(root,width=400,height=50,bg="light blue")
frame.place(x=0,y=180)
task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text="ADD",font="arial 20 bold ",width=6,bg="#5a95ff",fg="#ffccff",bd=0, command=addtask)
button.place(x=300,y=0)


#listbox
frame1=Frame(root, bd=3,width=700,height=180,bg="#8717E2")
frame1.pack(pady=(260,0))
listbox= Listbox(frame1,font=('arial' ,12),width=40,height=16,bg="#32405b", fg="white",cursor="hand2",selectbackground="#5a95ff" )
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1,command=listbox.yview)
scrollbar.pack(side=LEFT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
#delete
Delete_icon=PhotoImage(file="Image/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
messagebox=Label(root,text="are you sure",fg="white",bg="white",padx=40,pady=10,relief=RAISED,anchor=W)
#messages

message=Label(root,text="Welcome to To-Do-List",fg="white",bg="black",padx=40,pady=10,relief=RAISED,anchor=W)
message.place(x=130,y=10)

root.config(bg="#34AAB1")
root.geometry("400x750+400+200")




root.mainloop()


