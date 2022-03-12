import time
from tkinter import *
from tkinter import messagebox

# creating Tk window
r = Tk()
r.geometry("600x500")
r.title("Time Counter")

#declaration of variables as str.
hour=StringVar()
minute=StringVar()
second=StringVar()

# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(r, width=3, font=("Arial",18,""),
                textvariable=hour)
hourEntry.place(x=80,y=20) 
minuteEntry= Entry(r, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=20)
secondEntry= Entry(r, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=20)

def submit():
    try:
        #getting input by user
        #stored as seconds.
        count = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Need valid values.")
    while count > -1:
        mins,secs = divmod(count,60)
        #mins = count // 60
        #secs = count % 60
        #For example : 150 sec => (150//60)min + (150%60)sec -> 2min 30sec.

        hours = 0
        #we also controll if total min greater than 60
        #like mins,secs relation.
        if mins>60:
            hours, mins = divmod(mins,60)
        
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        #update GUI after 1 sec
        r.update()
        time.sleep(1)

        if(count==0):
            messagebox.showinfo("Countdown","Time is over")
        
        #the value of count will be decreased by 1.
        count -= 1

# button widget
button = Button(r, text='Enter Time', bd='5',
             command= submit)
button.place(x = 50,y = 100)
  
# starting tkinter loop
r.mainloop()
       

