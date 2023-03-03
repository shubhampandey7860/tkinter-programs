from tkinter import * 
die = {0:'🎲',1:'',2:'⚁',3:'⚂',4:'⚃',5:'⚄',6:'⚅'}

App = Tk()
App.title("Dice")
App.config(bg='yellow')
dice = Label(App,text=die[0],font=('Times',100),foreground='white')

dice.grid(row=0,column=0,padx=25,pady=5)

def roll():
    from random import randint
    i=randint(1,6)
    msg = Label(App,text=die[i],font=('Times',100),foreground='white')
    msg.grid(row=0,column=0,padx=25,pady=5)
    
rolls = Button(App,text="Roll",command=roll)
rolls.grid(row=1,column=1)
App.mainloop()    
    