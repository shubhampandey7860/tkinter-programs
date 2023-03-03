from tkinter import * 
App=Tk()
App.title('Ico converter')


def open_img():
    from PIL import Image
    from tkinter import filedialog
    global img
    App.img_dir=filedialog.askopenfilename(initialdir='C:',title='select your image',filetypes=(('PNG Images','*.png'),('JPG Images','*.jpg'),('All files','*.*')))
    
    
    img=Image.open(App.img_dir)
    
    
def con_img():
    from PIL import Image
    img.save(f'{ico_name.get()}.ico',format='ICO',sizes=[(ico_size.get(),ico_size.get())])
    success = Toplevel()
    success.title('success')
    msg = Label(success,text='conversion success')
    msg.pack()
    success.mainloop()
    
    
def preview():
    prev= Toplevel()
    prev.title('Icon preview')
    prev.iconbitmap(f'{ico_name.get()}.ico')
    prev_lbl = Label(prev,text='checkout your icon!')
    prev_lbl.pack() 
    
    prev.mainloop()
    
    
    
chooselbl = Label(App,text='select your image')
chooselbl.grid(row=0,column=0,pady=10)   

chooseB = Button(App,text='choose',command=open_img) 
chooseB.grid(row=0,column=1,pady=10)   

sizeL = Label(App,text='select a size for the icon')
sizeL.grid(row=1,column=0)
ico_size=IntVar()
sizes_options =[16,24,32,48,64,128,255]
ico_size.set(32)
size_menu = OptionMenu(App,ico_size,*sizes_options)
size_menu.grid(row=1,column=1,pady=10)
fnameL = Label(App,text='enter the icon name:')
fnameL.grid(row=2,column=0,pady=10)

ico_name = Entry(App)
ico_name.grid(row=2,column=1,pady=10)

convB = Button(App,text='Convert',command=con_img)
convB.grid(row=3,column=0,pady=10)

prevB = Button(App,text='Preview',command=preview)
prevB.grid(row=3,column=1,pady=10)

App.mainloop()
    
        