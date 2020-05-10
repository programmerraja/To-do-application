#"to do list are sotred in files "
#once you finished check that
#it stored in files you can get it back lets run again
from tkinter import Label,Entry,Checkbutton,StringVar,Tk,PhotoImage

import os
from tkinter import messagebox

class To_do_list:
    def __init__(self,window):
        try:
           #this function only work on linux 
           self.os_name=os.uname()
        except:
            self.os_name="windows"
        window.destroy()

        self.Todowindow=Tk()
        self.Todowindow.title("T0 Do List")
        self.Todowindow.geometry("500x500+400+30")
        #self.Todowindow.resizable(0,0)
        #to hold check box                       
        self.task=["" for i in range(10)]
        #to acess check box using index 
        self.i=0
        #axis to place check box 
        self.x=120
        self.y=100

        #to store user input job in entry box
        self.job=StringVar()
        
        self.dir=os.getcwd()

        self.label=Label(self.Todowindow,text="Enter your to do list here ")
        self.label.place(x=100,y=100)
        self.coder=Label(self.Todowindow,text="Programmer Raja ")
        self.coder.place(x=140,y=480)

        try:
            if(self.os_name=="windows"):
               self.image=PhotoImage(file=os.path.join(self.dir,"image","todo.png"))
            else:
                 self.image=PhotoImage(file=os.path.join(self.dir,"image","todo.png"))
            self.label=Label(self.Todowindow,image=self.image).place(x=0,y=0)
        except:
             messagebox.showinfo("ERROR","image is missing ! ")
            

        self.label_job=Label(self.Todowindow,text="Enter Your Task Here",background="lightblue",fg="green").place(x=130,y=450)

        self.entry=Entry(self.Todowindow,width=40,textvariable=self.job)
        self.entry.place(x=130,y=470)
        
        #adding old list in file when user opening 
        self.add_to_file_a()
        
        self.entry.bind("<Return>",lambda event,task=self.entry.get(): self.add_task(event,self.entry.get()))


       
    def add_task(self,event,task):
        #checking that user enter task and the y axis limit
        if(task and self.y<400):
            try:
                    self.file=open(os.path.join("files","to_do_list.txt"),"a")
            except:
                 self.file=open(os.path.join("files","to_do_list.txt"),"w")
            self.task[self.i]=Checkbutton(self.Todowindow,text=task,)
            self.task[self.i].place(x=self.x,y=self.y)
            #when user add by own we need t write it on file 
            if(event!=5):
              self.file.write(self.entry.get()) 
              self.file.write("\n")
            self.task[self.i].bind("<Button-1>",self.remove_task)
            self.y+=30
            self.i+=1
            
        self.job.set("")
        self.file.close()

    def remove_task(self,event):

        self.file_w=open(os.path.join("files","to_do_list.txt"),"w")
        #getting the completed job text 
        self.text=event.widget["text"] 
        # destroy the completed list 
        event.widget.destroy()

        #adding to file except completed list
        self.add_to_file_r()
        
        self.file_w.close()
        
        #once rearrange need to reset the values
        self.y=100
        self.i=0
        self.task=["" for i in range(10)]

        #after reseting add to window 
        self.add_to_file_a()
        
    def add_to_file_r(self):
        #adding to file except completed list 
        for line in range(len(self.task)):
                    if(self.task[line]):
                        try:
                         if(str(self.task[line]["text"]) !=str(self.text)):
                            self.file_w.write(self.task[line]["text"])
                            self.file_w.write("\n")
                            self.task[line].destroy()
                        except:
                            pass
                    
    def add_to_file_a(self):
        #reading from file and add to window
        self.file=open(os.path.join("files","to_do_list.txt"),"r")
        #checking is file is empty or not 
        if(len(self.file.readlines())>=1):
            self.file.seek(0)
            li=self.file.readlines()
            for line in range(0,len(li)):
                    self.add_task(5,li[line].strip("\n"))
            self.file.close()
        
        
to= To_do_list(Tk())
