from tkinter import *


def fun():
    name_save=name.get()
    #robo_save=robo.get()           #if it is checked will get 1 or else get 0
    name_entry.delete(0,10)         #this will clear the value entered in dilog box
    #name_entry.destroy()           #this will destroy the label itself
    
    if((len(name_save)==0)):
        print("Empty")
        msg.place(x=10,y=500)
        save_butt.flash()           #flashes the button 3,4 times
    else:
        print("Welcome "+str(name_save))
        msg.destroy()
        return 99
''' newWindow= Toplevel(screen)
    newWindow.title("New Tab")
    screen.geometry("400x600")
    print("Print clicked") '''     #this can create a new window upon the click of a button                             
def dest():                       #function to close the main window
    screen.destroy()
    #top=Toplevel().iconify()  #will iconify the default tk scrren
    #top=Toplevel().withdraw() #will remove the default tk screen
    #top=Toplevel().title("new")
    #top.mainloop()
def donothing():
    print()





#EDITING THE MAIN WINDOW
screen =Tk()                        #This is the base code that generates the main window
                                    #'screen' is the user defined object name we used to specify its properties 
screen.geometry("400x600")          #this function will assign the size of the window by mentined size
screen.title("Sample Window")       #this function will define the heading of the windows





#EDITING A LABEL INSIDE THE WINDOW
Heading=Label(text="THIS IS HEADING",
              anchor="center",      #(n, ne, e, se, s, sw, w, nw, or center(default))
              bg="grey",fg="white", #colours are listed in the attched png file
              relief="groove" ,     #relif:groove,raised,flat,solid,sunken,
              width="400",height="3",
              font="TIMESNEWROMAN",
              cursor="dot",
              #image="TkInterColorCharts.png",
              underline=0
              )
''' PARAMETERS
        anchor:defines the position of the heading in the block defined in label
        bg:determines the colour of the block that is to be created using label
        fg:determines the colour of the font in the block
        relif:determines the engraving of the block with rest of window
        height and width : determinees the width and height of the block
        font:determines the font of the label
        dot:this determines the shape of cursor over the label
        underline:this will create an underline as the integer number ill giveaway its position
'''
Heading.pack()
#Heading.pack(expand=YES, fill=BOTH)
#Heading.place(x=10,y=10)
#Heading.grid(row=1,colomn=2)
#all these options are used to arrange the label/widget




#EDITING THE SCROLL #but dont know how to work it out
'''
scroll=Scrollbar(screen)
scroll.pack(side=RIGHT,fill=Y)
'''



#EDITING THE CANVAS
#can=Canvas(bg="lightgrey",height="550",width="400")#creates a canvas

#CREATE AN ARC IN CANVAS
'''
cordinates=10,50,240,410             #this are the cordinates for the arc inside the canvas
arc=can.create_arc(cordinates,
            start=0,extent=90,      #this is the angle of arc start and ending
            fill="black")            #this is the colur of the arc inside the canvas
'''
#CREATE AN IMAGE IN CANVAS
'''
filename = PhotoImage(file = "TkInterColorCharts.png")
image = can.create_image(100, 300, anchor=S, image=filename)#first 2 parameters are the size of the image
'''
#CREATE A LINE IN CANVAS
'''
line = can.create_line(10, 20, 40, 50,100,200,300,400,fill="blue") #this will create a line in canvas and these are the cordinates and colour
'''
#CRETAE AN OVAL IN CANVAS
'''
oval = can.create_oval(100, 200, 400, 500,fill="blue")
'''
#CREATE ANY POLYGON
'''
poly=can.create_polygon(10,20,300,400,500,80,fill="blue")
'''
#can.pack()






#EDITING MENU
mb=Menu(screen,activeforeground="blue")#main menu option
drop1=Menu(mb,tearoff=0,activebackground="red")#the fist option in horizontal tab
#drop1.add_command(label="opt1", command=donothing)
drop1.add_radiobutton(label="opt1", command=donothing)
drop1.add_command(label="opt2", command=donothing)
drop1.add_separator()
drop1.add_command(label="opt3", command=donothing)
mb.add_cascade(label="drop1", menu=drop1)#naming the thing in horizontal tab
drop2=Menu(mb,tearoff=0)#thesecond option in horizontal tab
drop2.add_command(label="opt1", command=donothing)
drop2.add_command(label="opt2", command=donothing)
mb.add_cascade(label="drop2", menu=drop1)#naming the item 
screen.config(menu=mb)









#EDITING A LABEL
name_text=Label(text="Name : ",font="TIMESNEWROMAN"#create a label says name:, this has other parametrs like underline,pd,padx,pady,etc..
                )
#name_text.config(bg="white",fg="black")            #you can use parametes inside config or inside the label itself ,same effct
name_text.place(x=10,y=100)                         #we can pack() it which places it to the next free location automatically
                                                    #or place() or grid() it which places it as per the desired location






#EDITING AN ENTRY
name=StringVar()                                    #this will say that the value that is going to be entered are of string
                                                    #IntVar():this will enter the value as a number
name_entry=Entry(textvariable=name,                 #enered value is saved into this name variable
                 #command=fun,                      #this will call the function upon typing,but dont know why showing error on uncommnting also execute witout clicking entry
                 highlightcolor="blue",
                 #show="*",                         #incase the entry is for passsword , this will conver to *
                 width="40",)                        #this will create a empty dilog box to enter the value 
name_entry.place(x=110,y=101)







#EDITING A RADIOBUTTON
gender_text=Label(text="Gender : ",font="TIMESNEWROMAN")
gender_text.place(x=10,y=150)
gender=IntVar(screen)
gender1_entry=Radiobutton(screen,text="Male",variable=gender,value=1).place(x=115,y=151)
gender1_entry=Radiobutton(screen,text="Female",variable=gender,value=2).place(x=165,y=151)
#gender1_entry.place(x=165,y=151)                   #you can also use this way too

'''
parameters are same as all other
deselect(),select(),flash(),invoke()
'''





#EDITING A DROPDOWN OPTION
age_text=Label(text="Age : ",font="TIMESNEWROMAN")
age_text.place(x=10,y=200)
age=StringVar(screen)                               #the option choosed will be saved to a string variable called age
age.set("Select")                                   #default option
age_entry= OptionMenu(screen,age,"1","2","3","4","5","6","7","8","9","10")#parmetr: smaster,varaible,values 
age_entry.place(x=105,y=201)








#EDITING A LISTBOX
'''
lis_text=Label(text="choose option",font="TIMESNEWROMAN",height=2,width=10)
lis_text.place(x=10,y=270)
lis=Listbox()
lis.insert(1,"opt 1")
lis.insert(2,"opt 2")
lis.insert(3,"opt 3")
lis.insert(4,"opt 4")
lis.place(x=135,y=250)
'''
'''
lis.size() #returns the number of lines used in the listbox
lis.activate(1)#selects the option as in index 1
'''






#EDITING A CHECKBOX
robo_text=Label(text="I'm not a robot ",font="TIMESNEWROMAN")
robo_text.place(x=5,y=380)
robo=IntVar(screen)
robo_entry=Checkbutton(screen,text=" ",
                       variable=robo,
                       activebackground="red",  #colour when checkbox is ticked/unticked
                       command=fun,             #command or can be used to call a function
                       offvalue=0 ,             #value sent when box is unchecked
                       onvalue=999 ,            #value sent whn box is checked
                       state=NORMAL
                       )
robo_entry.place(x=115,y=381)
'''
robo_entry.deselect() :uncheck the box
robo_entry.flash() : flashes the box
robo_entry.invoke :gets the return value
robo_entry.select():checks the box
robo_entry.toggle() : toggles the value
'''



#EDITING A MESSAGE
msg=Message(screen,text="Empty",fg="red",width="50")
'''
msg.place(x=,y=)
'''



#EDITING A BUTTON INSIDE THE WINDOW
save_butt=Button(screen,text="Save",bg="white",fg="black",
                 activebackground="orange",     #this is the colour when button is pressed
                 activeforeground="black",
                 #relif="groove",
                 state=NORMAL,                  #DISABLED:disables button,ACTIVE:pressed at start position,NORMAL(default)
                 width="30",height="2",
                 bd=2,                          #will define the border thickness of button
                 command=fun)                   #upon clicking button it will call the function fun()
#parameters=master,values,
save_butt.place(x=80,y=450)
dest_butt=Button(screen,text="Exit",bg="white",fg="black",activebackground="red",width="20",height="2",command=dest)
#parameters=master,values,etc.                  #this will create a button 
dest_butt.place(x=250,y=520)
'''
save_butt.invoke()                             #this will get the value that is returned from the called function
save_butt.flash()                              #flashes the button 3,4 times
'''

screen.mainloop()

