from tkinter import * 
from datetime import datetime
 
App = Tk()
App.title('Age Calculator')
bg = 'black'
fg = 'cyan'
App.geometry('250x250')


App['background']=bg 

msg = Label(App,text = 'Enter your dob',foreground=fg,background=bg)
msg.grid(row=1,column=1,columnspan=3)

dayL = Label(App,text = 'Day',foreground=fg,background=bg)
dayE = Entry(App,width = 2,foreground=fg,background=bg)
 

monthL = Label(App,text = 'Month:',background=bg,foreground=fg)
monthE = Entry(App,width = 2,background=bg,foreground=fg)

YearL = Label(App,text = 'Year :',background=bg,foreground=fg)
YearE = Entry(App,width = 4,background=bg,foreground=fg)
 
dayL.grid(row=1,column=0)
dayE.grid(row=1,column=1)
monthL.grid(row=1,column=2)
monthE.grid(row=1,column=3)
YearL.grid(row=1,column=4)
YearE.grid(row=1,column=5) 


def find_days():
    date = int(dayE.get())
    mon =  int(monthE.get())
    year = int(YearE.get())
    dob = datetime(day=date,month=mon,year=year)
    
    time_now = datetime.now()
    time_dif = time_now - dob 
    
    dys = Label(App,text='You lived '+str(time_dif.days)+'days!')
    dys.grid(row=3,columnspan=4,column=0)

   
    
    
def find_sc():
    date = int(dayE.get())
    mon =  int(monthE.get())
    year = int(YearE.get())
    dob = datetime(day=date,month=mon,year=year)
    
    time_now = datetime.now()
    time_dif = time_now - dob 
    
    scs = Label(App,text='You lived '+str(time_dif.total_seconds())+'seconds')
    scs.grid(row=4,column=0,columnspan=6)
    
        
    




dysB = Button(App,text='Total_days',command=find_days,background=bg,foreground=fg) 

scsB = Button(App,text='Total_Seconds',command=find_sc,background=bg,foreground=fg) 
dysB.grid(row=2,column=0,columnspan=3)
scsB.grid(row=2,column=3,columnspan=3)


App.mainloop()

 