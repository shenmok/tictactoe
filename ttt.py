# 2022

#------------------------------------------------------------------
# Made By Akash
# Helped by bee ( a discord username ) and Anshuman Thakur and countless( i forgot the exact number :p) examples on the internet and community
# Thanks for reading this and using this.
#------------------------------------------------------------------

# importing things i need

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
import pathlib
import time

# image defining

normal_id = pathlib.Path(__file__).parent / 'images_ttt' / 'default2.png'
hover_id = pathlib.Path(__file__).parent / 'images_ttt' / 'blue.png'

click_x_id = pathlib.Path(__file__).parent / 'images_ttt' / 'mark_x.png'
click_o_id = pathlib.Path(__file__).parent / 'images_ttt' / 'mark_o.png'

vertical_win_x_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_x.png'
horizontal_win_x_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_x.png'
diagonal1_win_x_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_x.png'
diagonal2_win_x_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_x.png'

vertical_win_o_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_o.png'
horizontal_win_o_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_o.png'
diagonal1_win_o_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_o.png'
diagonal2_win_o_id = pathlib.Path(__file__).parent / 'images_ttt' / 'win_o.png'


# window making

canva = Tk()
canva.geometry('1900x1080')
canva.configure(bg='white')

# image creation

normal = PhotoImage(file=normal_id)
hover = PhotoImage(file=hover_id)
clik_x = PhotoImage(file=click_x_id)
clik_o = PhotoImage(file=click_o_id)
vertical_win_x = PhotoImage(file=vertical_win_x_id)
horizontal_win_x = PhotoImage(file=horizontal_win_x_id)
diagonal1_win_x = PhotoImage(file=diagonal1_win_x_id)
diagonal2_win_x = PhotoImage(file=diagonal2_win_x_id)
vertical_win_o = PhotoImage(file=vertical_win_o_id)
horizontal_win_o = PhotoImage(file=horizontal_win_o_id)
diagonal1_win_o = PhotoImage(file=diagonal1_win_o_id)
diagonal2_win_o = PhotoImage(file=diagonal2_win_o_id)


# variable for win and player where player false = x and true = o

win = False
player = False

# button list for manually checking current image 

button_images = ['normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal']

# winner check function 

def check_win():
    global win, player
    
    if button_images[0] == button_images[1] == button_images[2] == 'clik_x':
        
        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        tl.config(image=horizontal_win_x)
        tc.config(image=horizontal_win_x)
        tr.config(image=horizontal_win_x)
        
    elif button_images[3] == button_images[4] == button_images[5] == 'clik_x':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        ml.config(image=horizontal_win_x)
        mc.config(image=horizontal_win_x)
        mr.config(image=horizontal_win_x)
        
    elif button_images[6] == button_images[7] == button_images[8] == 'clik_x':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        bl.config(image=horizontal_win_x)
        bc.config(image=horizontal_win_x)
        br.config(image=horizontal_win_x)
        
    elif button_images[0] == button_images[3] == button_images[6] == 'clik_x':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        tl.config(image=vertical_win_x)
        ml.config(image=vertical_win_x)
        bl.config(image=vertical_win_x)
        
    elif button_images[1] == button_images[4] == button_images[7] == 'clik_x':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        tc.config(image=vertical_win_x)
        mc.config(image=vertical_win_x)
        bc.config(image=vertical_win_x)
        
    elif button_images[2] == button_images[5] == button_images[8] == 'clik_x':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        tr.config(image=vertical_win_x)
        mr.config(image=vertical_win_x)
        br.config(image=vertical_win_x)
        
    elif button_images[0] == button_images[4] == button_images[8] == 'clik_x':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        tl.config(image=diagonal1_win_x)
        mc.config(image=diagonal1_win_x)
        br.config(image=diagonal1_win_x)
        
    elif button_images[2] == button_images[4] == button_images[6] == 'clik_x':
            
        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','X wins' ,icon='info')
        tr.config(image=diagonal2_win_x)
        mc.config(image=diagonal2_win_x)
        bl.config(image=diagonal2_win_x)
        
    elif button_images[0] == button_images[1] == button_images[2] == 'clik_o':
        
        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        tl.config(image=horizontal_win_o)
        tc.config(image=horizontal_win_o)
        tr.config(image=horizontal_win_o)
        
    elif button_images[3] == button_images[4] == button_images[5] == 'clik_o':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        ml.config(image=horizontal_win_o)
        mc.config(image=horizontal_win_o)
        mr.config(image=horizontal_win_o)
        
    elif button_images[6] == button_images[7] == button_images[8] == 'clik_o':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        bl.config(image=horizontal_win_o)
        bc.config(image=horizontal_win_o)
        br.config(image=horizontal_win_o)
        
    elif button_images[0] == button_images[3] == button_images[6] == 'clik_o':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        tl.config(image=vertical_win_o)
        ml.config(image=vertical_win_o)
        bl.config(image=vertical_win_o)
        
    elif button_images[1] == button_images[4] == button_images[7] == 'clik_o':

        disable_buttons()
        win=True
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        tc.config(image=vertical_win_o)
        mc.config(image=vertical_win_o)
        bc.config(image=vertical_win_o)
        
    elif button_images[2] == button_images[5] == button_images[8] == 'clik_o':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        tr.config(image=vertical_win_o)
        mr.config(image=vertical_win_o)
        br.config(image=vertical_win_o)
        
    elif button_images[0] == button_images[4] == button_images[8] == 'clik_o':

        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        tl.config(image=diagonal1_win_o)
        mc.config(image=diagonal1_win_o)
        br.config(image=diagonal1_win_o)
        
    elif button_images[2] == button_images[4] == button_images[6] == 'clik_o':
            
        disable_buttons()
        win=True
        player=False
        showinfo('Tic Tac Toe','O wins' ,icon='info')
        tr.config(image=diagonal2_win_o)
        mc.config(image=diagonal2_win_o)
        bl.config(image=diagonal2_win_o)
        
#draw function part
    elif all(i in ('clik_x','clik_o') for i in button_images) and win==False:
        showinfo('Tic Tac Toe','DRAW' ,icon='info')
                                
# disabling buttons function

def disable_buttons():
    button_images[0]=button_images[1]=button_images[2]=button_images[3]=button_images[4]=button_images[5]=button_images[6]=button_images[7]=button_images[8]='disabled'
    
# reset function

def reset_b():
    button_images[0]=button_images[1]=button_images[2]=button_images[3]=button_images[4]=button_images[5]=button_images[6]=button_images[7]=button_images[8]='normal'
    time.sleep(1)
    tl.config(image = normal)
    tc.config(image = normal)
    tr.config(image = normal)
    ml.config(image = normal)
    mc.config(image = normal)
    mr.config(image = normal)
    bl.config(image = normal)
    bc.config(image = normal)
    br.config(image = normal)
    showinfo('Tic Tac Toe', 'Game Reset', icon='warning')
# tl functions

def on_enter(e):
    if button_images[0] == 'normal':
        tl.config(image=hover)
        button_images[0] = 'hover'
        
def on_leave(e):
    if button_images[0] == 'hover':
        tl.config(image=normal)
        button_images[0] = 'normal'

def on_click(e):
    global player, win
    
    if button_images[0] == 'hover' and player == False:
        tl.config(image=clik_x)
        button_images[0] = 'clik_x'
        player = True
        
    elif button_images[0] == 'hover' and player == True:
        tl.config(image=clik_o)
        button_images[0] = 'clik_o'
        player = False
        
    elif button_images[0] == 'clik_x' or button_images[0] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
    
   
# tc functions

def on_enter1(e):
    if button_images[1] == 'normal':
        tc.config(image=hover)
        button_images[1] = 'hover'
        
def on_leave1(e):
    if button_images[1] == 'hover':
        tc.config(image=normal)
        button_images[1] = 'normal'
    
   
def on_click1(e):
    global player, win
     
    if button_images[1] == 'hover' and player == False:
        tc.config(image=clik_x)
        button_images[1] = 'clik_x'
        player = True
        
    elif button_images[1] == 'hover' and player == True:
        tc.config(image=clik_o)
        button_images[1] = 'clik_o'
        player = False
        
    elif button_images[1] == 'clik_x' or button_images[1] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
        
# tr functions

def on_enter2(e):
    if button_images[2] == 'normal':
        tr.config(image=hover)
        button_images[2] = 'hover'
        
def on_leave2(e):
    if button_images[2] == 'hover':
        tr.config(image=normal)
        button_images[2] = 'normal'
    
   
def on_click2(e):
    global player, win
     
    if button_images[2] == 'hover' and player == False:
        tr.config(image=clik_x)
        button_images[2] = 'clik_x'
        player = True
        
    elif button_images[2] == 'hover' and player == True:
        tr.config(image=clik_o)
        button_images[2] = 'clik_o'
        player = False
        
    elif button_images[2] == 'clik_x' or button_images[2] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
        
# ml functions

def on_enter3(e):
    if button_images[3] == 'normal':
        ml.config(image=hover)
        button_images[3] = 'hover'
        
def on_leave3(e):
    if button_images[3] == 'hover':
        ml.config(image=normal)
        button_images[3] = 'normal'
    
   
def on_click3(e):
    global player, win
     
    if button_images[3] == 'hover' and player == False:
        ml.config(image=clik_x)
        button_images[3] = 'clik_x'
        player = True
        
    elif button_images[3] == 'hover' and player == True:
        ml.config(image=clik_o)
        button_images[3] = 'clik_o'
        player = False
        
    elif button_images[3] == 'clik_x' or button_images[3] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
    
# mc functions

def on_enter4(e):
    if button_images[4] == 'normal':
        mc.config(image=hover)
        button_images[4] = 'hover'
        
def on_leave4(e):
    if button_images[4] == 'hover':
        mc.config(image=normal)
        button_images[4] = 'normal'
    
   
def on_click4(e):
    global player, win
     
    if button_images[4] == 'hover' and player == False:
        mc.config(image=clik_x)
        button_images[4] = 'clik_x'
        player = True
        
    elif button_images[4] == 'hover' and player == True:
        mc.config(image=clik_o)
        button_images[4] = 'clik_o'
        player = False
        
    elif button_images[4] == 'clik_x' or button_images[4] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
       
# mr functions

def on_enter5(e):
    if button_images[5] == 'normal':
        mr.config(image=hover)
        button_images[5] = 'hover'
        
def on_leave5(e):
    if button_images[5] == 'hover':
        mr.config(image=normal)
        button_images[5] = 'normal'
    
   
def on_click5(e):
    global player, win
     
    if button_images[5] == 'hover' and player == False:
        mr.config(image=clik_x)
        button_images[5] = 'clik_x'
        player = True
        
    elif button_images[5] == 'hover' and player == True:
        mr.config(image=clik_o)
        button_images[5] = 'clik_o'
        player = False
        
    elif button_images[5] == 'clik_x' or button_images[5] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
        
# bl functions

def on_enter6(e):
    if button_images[6] == 'normal':
        bl.config(image=hover)
        button_images[6] = 'hover'
        
def on_leave6(e):
    if button_images[6] == 'hover':
        bl.config(image=normal)
        button_images[6] = 'normal'
    
   
def on_click6(e):
    global player, win
     
    if button_images[6] == 'hover' and player == False:
        bl.config(image=clik_x)
        button_images[6] = 'clik_x'
        player = True
        
    elif button_images[6] == 'hover' and player == True:
        bl.config(image=clik_o)
        button_images[6] = 'clik_o'
        player = False
        
    elif button_images[6] == 'clik_x' or button_images[6] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
        
# bc functions

def on_enter7(e):
    if button_images[7] == 'normal':
        bc.config(image=hover)
        button_images[7] = 'hover'
        
def on_leave7(e):
    if button_images[7] == 'hover':
        bc.config(image=normal)
        button_images[7] = 'normal'
    
   
def on_click7(e):
    global player, win
     
    if button_images[7] == 'hover' and player == False:
        bc.config(image=clik_x)
        button_images[7] = 'clik_x'
        player = True
        
    elif button_images[7] == 'hover' and player == True:
        bc.config(image=clik_o)
        button_images[7] = 'clik_o'
        player = False
        
    elif button_images[7] == 'clik_x' or button_images[7] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()
        
# br functions

def on_enter8(e):
    if button_images[8] == 'normal':
        br.config(image=hover)
        button_images[8] = 'hover'
        
def on_leave8(e):
    if button_images[8] == 'hover':
        br.config(image=normal)
        button_images[8] = 'normal'
    
   
def on_click8(e):
    global player, win
     
    if button_images[8] == 'hover' and player == False:
        br.config(image=clik_x)
        button_images[8] = 'clik_x'
        player = True
        
    elif button_images[8] == 'hover' and player == True:
        br.config(image=clik_o)
        button_images[8] = 'clik_o'
        player = False
        
    elif button_images[8] == 'clik_x' or button_images[8] == 'clik_o':
        showinfo('Tic Tac Toe', 'As you can see, that box is already taken, please choose some other box.', icon='warning')
    check_win()

# reset button function

def on_click9(e):
    result = askquestion('Tic Tac Toe', 'New Game? Current game will not be saved.', icon='warning')

    if result == 'yes':
        reset_b()
        
    elif result == 'no':
        return
    
         
# the buttons themselves
        
tl = Button(canva, image=normal, width=250, height=250)
tc = Button(canva, image=normal, width=250, height=250)
tr = Button(canva, image=normal, width=250, height=250)
ml = Button(canva, image=normal, width=250, height=250)
mc = Button(canva, image=normal, width=250, height=250)
mr = Button(canva, image=normal, width=250, height=250)
bl = Button(canva, image=normal, width=250, height=250)
bc = Button(canva, image=normal, width=250, height=250)
br = Button(canva, image=normal, width=250, height=250)
reset_btn = Button(canva, text= 'NEW GAME', width=30, height=7)

# the buttons format positions for a 3x3

tl.grid(column=0, row=0)
tc.grid(column=1, row=0)
tr.grid(column=2, row=0)
ml.grid(column=0, row=1)
mc.grid(column=1, row=1)
mr.grid(column=2, row=1)
bl.grid(column=0, row=2)
bc.grid(column=1, row=2)
br.grid(column=2, row=2)
reset_btn.grid(column=4, row=1)


# the events

tl.bind('<Enter>', on_enter)
tl.bind('<Leave>', on_leave)
tl.bind('<ButtonPress>', on_click)

tc.bind('<Enter>', on_enter1)
tc.bind('<Leave>', on_leave1)
tc.bind('<ButtonPress>', on_click1)

tr.bind('<Enter>', on_enter2)
tr.bind('<Leave>', on_leave2)
tr.bind('<ButtonPress>', on_click2)

ml.bind('<Enter>', on_enter3)
ml.bind('<Leave>', on_leave3)
ml.bind('<ButtonPress>', on_click3)

mc.bind('<Enter>', on_enter4)
mc.bind('<Leave>', on_leave4)
mc.bind('<ButtonPress>', on_click4)

mr.bind('<Enter>', on_enter5)
mr.bind('<Leave>', on_leave5)
mr.bind('<ButtonPress>', on_click5)

bl.bind('<Enter>', on_enter6)
bl.bind('<Leave>', on_leave6)
bl.bind('<ButtonPress>', on_click6)

bc.bind('<Enter>', on_enter7)
bc.bind('<Leave>', on_leave7)
bc.bind('<ButtonPress>', on_click7)

br.bind('<Enter>', on_enter8)
br.bind('<Leave>', on_leave8)
br.bind('<ButtonPress>', on_click8)

reset_btn.bind('<ButtonPress>', on_click9)

#idk bout mainloop but this is probably a loop that allows the events to work and register input from keys and clicks and what not

canva.mainloop()
