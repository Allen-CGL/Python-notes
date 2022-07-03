#=================Introduction=================================================
from tkinter import*

root = Tk()#root widget, has to be first in any tkinter code

#creating label widget
myLabel = Label(root, text='hello world')

#shoving it onto the screen
myLabel.pack()

root.mainloop()

#=================Positioning With Tkinter's Grid System=======================
from tkinter import*

root = Tk()#root widget

#creating label widget
myLabel1 = Label(root, text='hello world').grid(row = 0, column = 0)
myLabel2 = Label(root, text='my name is Allen').grid(row = 1, column = 5)
myLabel3 = Label(root, text='relative').grid(row = 1, column = 1)

#shoving it onto the screen(r and c are relative)
#myLabel1.grid(row = 0, column = 0)
#myLabel2.grid(row = 1, column = 5)
#myLabel3.grid(row = 1, column = 1)

root.mainloop()

#=================Creating Buttons=============================================
from tkinter import*

root = Tk()#root widget

def myClick():
    myLabel = Label(root, text='look I click it')
    myLabel.pack()
    
myButton = Button(root, text='click me',command=myClick ,fg='black', bg='#FFC0CB', padx=10, pady=50)
#myButton = Button(root, text='click me',state=DISABLED)

myButton.pack()

root.mainloop()

#=================Creating Input Fields========================================
from tkinter import*

root = Tk()#root widget

e = Entry(root, width=50, borderwidth=5, bg='pink' ,fg='black')
e.pack()
e.insert(0,'enter your name: ') #box, default text inside the box

def myClick():
    hello = 'hello ' + e.get() #e.get gets whatever you type in the box
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
myButton = Button(root, text='enter something',command=myClick ,fg='black', bg='#FFC0CB', padx=10, pady=50)
#myButton = Button(root, text='click me',state=DISABLED)

myButton.pack()

root.mainloop()

#=================Build A Simple Calculator App================================
from tkinter import*

root = Tk()#root widget
root.title('simple calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))  
    return

def button_clear():
    e.delete(0, END)
    
def button_add():
    global f_num
    global math
    math = 'addition'
    f_num = int(e.get())
    e.delete(0, END)

def button_subtract():
    global f_num
    global math
    math = 'subtraction'
    f_num = int(e.get())
    e.delete(0, END)

def button_multiply():
    global f_num
    global math
    math = 'multiplication'
    f_num = int(e.get())
    e.delete(0, END)

def button_divide():
    global f_num
    global math
    math = 'division'
    f_num = int(e.get())
    e.delete(0, END)
    
def button_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == 'addition':
      e.insert(0, f_num + int(second_num))
    if math == 'subtraction':
      e.insert(0, f_num - int(second_num))
    if math == 'multiplication':
      e.insert(0, f_num * int(second_num))
    if math == 'division':
      e.insert(0, f_num / int(second_num))
    
#define buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1)) #can't have a input with normal function
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=91, pady=20, command=button_equal)
button_clear = Button(root, text='clear', padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text='/', padx=41, pady=20, command=button_divide)

#put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()

#==============Using Icons, Images, and Exit Buttons===========================
from tkinter import*
from PIL import ImageTk, Image

root = Tk()#root widget

#icon on the top right of the window
root.title('hello')
#root.iconbitmap('path/xxx.ico')

#image
#root.geometry("700x500")
#frame = Frame(root, width=600, height=400)
#frame.pack()
#frame.place(anchor='center', relx=0.5, rely=0.5)
my_img = ImageTk.PhotoImage(Image.open("BLACKPINK7.jpg"))
my_label = Label(image = my_img) #my_label = Label(frame, image = my_img)
my_label.pack()

#button quit
button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()

#===============Build an Image Viewer App======================================
from tkinter import*
from PIL import ImageTk, Image

root = Tk()#root widget

#icon on the top right of the window
root.title('hello')
#root.iconbitmap('path/xxx.ico')

my_image1 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/100808-564335.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/1807120101032275-600x400.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/blackpink.jpg'))
my_image4 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/BLACKPINK7.jpg'))

image_list = [my_image1,my_image2,my_image3,my_image4]

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)



def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    
    if image_number == 4:
        button_forward = Button(root, text='>>', state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='exit program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
button_exit.grid(row=1,column=1)

root.mainloop()

#===========================Adding A Status Bar================================
from tkinter import*
from PIL import ImageTk, Image

root = Tk()#root widget

#icon on the top right of the window
root.title('hello')
#root.iconbitmap('path/xxx.ico')

my_image1 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/100808-564335.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/1807120101032275-600x400.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/blackpink.jpg'))
my_image4 = ImageTk.PhotoImage(Image.open(r'C:/Users/wakan/OneDrive/圖片/Saved Pictures/BlackPink/BLACKPINK7.jpg'))

image_list = [my_image1,my_image2,my_image3,my_image4]

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)#status bar

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)



def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    
    if image_number == 4:
        button_forward = Button(root, text='>>', state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)#status bar
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)#status bar
    
def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)#status bar
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)#status bar
    
button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='exit program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
button_exit.grid(row=1,column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)#status bar

root.mainloop()

#====================Adding Frames To Your Program=============================
from tkinter import*
from PIL import ImageTk, Image

root = Tk()#root widget

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)#when using frame, pack and grid can be used at the same time

b = Button(frame, text='do not click here')
b2 = Button(frame, text='......or here')
b.grid(row=0, column=0)
b2.grid(row=1, column = 1)

root.mainloop()

#========================Radio Buttons==========================================
from tkinter import*
from PIL import ImageTk, Image

root = Tk()#root widget

toppings = [('pepperonis','pepperoni'),('cheeses','cheese'),('mushrooms','mushroom'),('onions','onion'),]

pizza = StringVar()
pizza.set('pepperoni') #choice set to the value that is 'pepperoni'

for name, topping in toppings:
    Radiobutton(root, text=name, variable=pizza, value=topping).pack(anchor=W)
    
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myLabel = Label(root, text=pizza.get())#get the value of the variable now (clicked)
myLabel.pack()

myButton = Button(root, text='click me', command=lambda: clicked(pizza.get()))#get the value of the variable now (clicked)
myButton.pack()

root.mainloop()
