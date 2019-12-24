#!/usr/bin/python
"""
Created on Sun Jul  7 15:28:06 2019

@author: sean
"""
import random
from tkinter import *

class Welcome():
    def __init__(self,master):
      
        self.master=master
        self.master.geometry('800x600+50+50')
        self.master.title('Log Book for the Great Campaigns of the Civil War')
        
        self.label1=Label(self.master,text='Welcome to the Log Book for the GCACW battles',fg='red').grid(row=0,column=2)

def main():
    root = Tk()
    welcomescreen = Welcome(root)
    root.mainloop

if __name__ == '__main__':
    main()
top = Tk()
top.title("Great Campaigns of the American Civil War")
top.geometry("1200x800")
#banner_img= PhotoImage(file='gcacw.gif')
#Label (top,image=banner_img).grid(row = 1,column=1,columnspan=6)


print('Processing...')

def helloCallBack():
    msg = messagebox.showinfo( "Coming Soon", "This feature has not been built yet")

def dump_event_log():
    global global_event_log
    print(global_event_log)

def add_event(event,side,unit,location,die_roll,die_roll_mod,result,notes):
    # adds an event to the event_log
    # event: the name of the event
    # side: which side caused the event ("Union","Confederate" or "Both")
    # unit: unit involved in the action (could be a leader)
    # location: hex location of noted action
    # die_roll: result of one or two d6
    # die_roll_mod: modifier to the die roll
    # result: result of action
    # notes: misc notes adding explanation to action
    
    global global_event_log
    event_no = len(global_event_log)+1
    global_event_log[event_no] = (event,side,unit,location,die_roll,die_roll_mod,result,notes)

def increment_turn():
    global global_turn
    global global_event_log
    global global_phase
    global_turn += 1
    global_phase = 'Random Events'
    add_event('New Turn','Both','None','None','None','None','Turn #' + str(global_turn),'None')
    create_lables()
    random_event_window()
    
    
    
def decrement_turn():
    global global_turn
    global global_event_log
    global_turn -= 1
    add_event('Undo Turn','Both','None','None','None','None','Turn #' + str(global_turn),'Reduced turn #')
    if global_turn < 0: global_turn = 0
    create_lables()    
    
def create_menus():    
    # create a toplevel menu
    menubar = Menu(top)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=helloCallBack)
    filemenu.add_command(label="Save", command=helloCallBack)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=top.destroy)
    menubar.add_cascade(label="File", menu=filemenu)


    eventmenu = Menu(menubar, tearoff=0)
    eventmenu.add_command(label="Start a Turn", command=increment_turn)
    eventmenu.add_command(label="Random Event Phase", command=random_event_window)
    eventmenu.add_command(label="Leader Transfer Phase", command=helloCallBack)
    eventmenu.add_command(label="Initiative", command=helloCallBack)
    eventmenu.add_command(label="Action", command=helloCallBack)
    eventmenu.add_command(label="Recovery Phase", command=helloCallBack)
    eventmenu.add_command(label="Rollback a Turn", command=decrement_turn)
    menubar.add_cascade(label="Event", menu=eventmenu)

    reportmenu = Menu(menubar, tearoff=0)
    reportmenu.add_command(label="Unit Report", command=helloCallBack)
    reportmenu.add_command(label="Location Report", command=helloCallBack)
    reportmenu.add_command(label="Event Log", command=dump_event_log)
    menubar.add_cascade(label="Report", menu=reportmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=helloCallBack)
    menubar.add_cascade(label="Help", menu=helpmenu)
#       
#
#    # display the menu
    top.config(menu=menubar)

def create_lables():
    banner_row = 1
    status_row = 3
    event_row = 10



    Label (top,text="Scenario:", font = 'Helvetica 12 bold').grid(row = status_row, column=1,columnspan=1)
    Label (top,text="Bloody Spotsylvania", font = 'Helvetica 12').grid(row = status_row, column=2,columnspan=1)  

    Label (top,text="Turn:", font = 'Helvetica 12 bold').grid(row = status_row + 1, column=1,columnspan=1)
    Label (top,text=global_turn, font = 'Helvetica 12').grid(row = status_row + 1, column=2,columnspan=1)
    
    Label (top,text="Phase:", font = 'Helvetica 12 bold').grid(row = status_row + 2, column=1,columnspan=1)
    Label (top,text=global_phase, font = 'Helvetica 12').grid(row = status_row + 2, column=2,columnspan=1)
    
    Label (top,text=" ", font = 'Helvetica 12 bold').grid(row = status_row + 3, column=2,columnspan=5)
    

    # event: the name of the event
    # side: which side caused the event ("Union","Confederate" or "Both")
    # unit: unit involved in the action (could be a leader)
    # location: hex location of noted action
    # die_roll: result of one or two d6
    # die_roll_mod: modifier to the die roll
    # result: result of action
    # notes: misc notes adding explanation to action

    Label (top,text="Event Number", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=1,columnspan=1)    
    Label (top,text="Event Type", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=2,columnspan=1)
    Label (top,text="Side", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=3,columnspan=1)    
    Label (top,text="Unit", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=4,columnspan=1)
    Label (top,text="Location", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=5,columnspan=1)    
    Label (top,text="Die Roll", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=6,columnspan=1)
    Label (top,text="Mod", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=7,columnspan=1)    
    Label (top,text="Result", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=8,columnspan=3)
    Label (top,text="Notes", font = 'Helvetica 12 bold',relief=RAISED).grid(row = event_row, column=11,columnspan=3)

    event_no = len(global_event_log)
    last_event_no = str(event_no)
    print(last_event_no)

    min_event = event_no - 10
    if min_event < 0: min_event = 0
    for num,each_event in enumerate(range(min_event,event_no + 1)):
        row_num = num + event_row + 1
        Label (top,text=each_event, font = 'Helvetica 12').grid(row = row_num, column=1,columnspan=1)        
        if each_event > 0:
            Label (top,text=global_event_log[each_event][0], font = 'Helvetica 12').grid(row = row_num, column=2,columnspan=1)
            Label (top,text=global_event_log[each_event][1], font = 'Helvetica 12').grid(row = row_num, column=3,columnspan=1)
            Label (top,text=global_event_log[each_event][2], font = 'Helvetica 12').grid(row = row_num, column=4,columnspan=1)
            Label (top,text=global_event_log[each_event][3], font = 'Helvetica 12').grid(row = row_num, column=5,columnspan=1)
            Label (top,text=global_event_log[each_event][4], font = 'Helvetica 12').grid(row = row_num, column=6,columnspan=1)
            Label (top,text=global_event_log[each_event][5], font = 'Helvetica 12').grid(row = row_num, column=7,columnspan=1)
            Label (top,text=global_event_log[each_event][6], font = 'Helvetica 12',relief=SUNKEN).grid(row = row_num, column=8,columnspan=3)
            Label (top,text=global_event_log[each_event][7], font = 'Helvetica 12').grid(row = row_num, column=11,columnspan=3)

        else:
            Label (top,text="Calm before the Storm", font = 'Helvetica 12').grid(row = row_num, column=2,columnspan=1)

def create_buttons():
    exit_button = Button(top, text="Exit", command = top.destroy, relief = RAISED)
    exit_button.grid(row = 100, column = 1, ipadx = 10, padx = 2, ipady = 5, pady = 5)  
    turn_button = Button(top, text="Turn +", command = increment_turn, relief = RAISED)
    turn_button.grid(row = 4, column = 3, ipadx = 10, padx = 2, ipady = 5, pady = 5)  


def action_window():
    action_window = Tk()
    action_window.title("Action Window")
    action_window.geometry("400x400")
    
    action_window.mainloop()


    

def initiative_window():
    init_window = Tk()
    init_window.title("Initiative Window")
    init_window.geometry("400x400")   

    def go_to_action():
        init_window.destroy()
        action_window()


    def init_roll():
        die_confederate = random.randrange(6)+1
        die_union = random.randrange(6)+1
        init_result = ""
        if die_union > die_confederate: init_result = "Union initiative" 
        else: init_result = "Confederate initiative"
        Label (init_window,text="Confederate Die:", font = 'Helvetica 12 bold').grid(row = 2, column=1,columnspan=1)
        Label (init_window,text="Union Die:", font = 'Helvetica 12 bold').grid(row = 3, column=1,columnspan=1) 
        Label (init_window,text="Winner:", font = 'Helvetica 12 bold').grid(row = 4, column=1,columnspan=1) 
        Label (init_window,text=str(die_confederate), font = 'Helvetica 12').grid(row = 2, column=2,columnspan=1)
        Label (init_window,text=str(die_union), font = 'Helvetica 12').grid(row = 3, column=2,columnspan=1) 
        Label (init_window,text=init_result, font = 'Helvetica 12 bold').grid(row = 4, column=2,columnspan=1) 
        add_event('Initiative','Union','None','None',die_union,'None',init_result,'None')
        add_event('Initiative','Confederate','None','None',die_confederate,'None',init_result,'None')
        # adds an event to the event_log
        # event: the name of the event
        # side: which side caused the event ("Union","Confederate" or "Both")
        # unit: unit involved in the action (could be a leader)
        # location: hex location of noted action
        # die_roll: result of one or two d6
        # die_roll_mod: modifier to the die roll
        # result: result of action
        # notes: misc notes adding explanation to action
        create_lables() 
        
    init_roll_button = Button(init_window, text="Roll Initiative", command = init_roll, relief = RAISED)
    init_roll_button.grid(row = 1, column = 1, ipadx = 10, padx = 2, ipady = 5, pady = 5)  
    
    action_button = Button(init_window, text="Go to Action", command = go_to_action, relief = RAISED)
    action_button.grid(row = 1, column = 2, ipadx = 10, padx = 2, ipady = 5, pady = 5)  

    init_exit_button = Button(init_window, text="Exit", command = init_window.destroy, relief = RAISED)
    init_exit_button.grid(row = 1, column = 10, ipadx = 10, padx = 2, ipady = 5, pady = 5)  
    

    init_window.mainloop()


def lt_window():
    global global_phase
    global_phase = 'Leader Transfer'
    lt_window = Tk()
    lt_window.title("Leader Transfer Window")
    lt_window.geometry("400x400")
    lt_img= PhotoImage(file='lee.gif')
    lee_label = Label (lt_window,image=lt_img)
    lee_label.image = lt_img
    lee_label.grid(row = 3,column=1,columnspan=3)
 
    
    def lt_conduct():
        pass
    
    def go_to_init():
        lt_window.destroy()
        initiative_window()
    
    lt_conduct_button = Button(lt_window, text="Conduct Leader Transfer", command = lt_conduct, relief = RAISED)
    lt_conduct_button.grid(row = 1, column = 1, ipadx = 10, padx = 2, ipady = 5, pady = 5)  
    
    init_button = Button(lt_window, text="Go to Initiative Activity", command = go_to_init, relief = RAISED)
    init_button.grid(row = 1, column = 2, ipadx = 10, padx = 2, ipady = 5, pady = 5)  

    lt_exit_button = Button(lt_window, text="Exit", command = lt_window.destroy, relief = RAISED)
    lt_exit_button.grid(row = 1, column = 10, ipadx = 10, padx = 2, ipady = 5, pady = 5)  

     

    lt_window.mainloop()




def random_event_window():
    global global_phase
    global_phase = 'Random Event'
    
    r_e_window = Tk()
    r_e_window.title("Random Event Window")
    r_e_window.geometry("800x400")
    
   
    def go_to_lt():
        r_e_window.destroy()
        lt_window()


        
    def r_e_roll():
        random_events_table = {
                2:"Rain (Current +2)",
                3:"Rain (Current +1)*",
                4:"No Effect**",
                5:"Rain (Current)*",
                6:"Union Command Paralysis",
                7:"Union Night March",
                8:"No Effect++",
                9:"Confederate Command Paralysis",
                10:"Confederate Command Paralysis",
                11:"No Effect++",
                12:"Rain (Current +1)"
                }

        die_one = random.randrange(6)+1
        die_two = random.randrange(6)+1
        die_total = die_one + die_two
        Label (r_e_window,text="Die One:", font = 'Helvetica 12 bold').grid(row = 2, column=1,columnspan=1)
        Label (r_e_window,text="Die Two:", font = 'Helvetica 12 bold').grid(row = 3, column=1,columnspan=1) 
        Label (r_e_window,text="Total:", font = 'Helvetica 12 bold').grid(row = 4, column=1,columnspan=1) 
        Label (r_e_window,text=str(die_one), font = 'Helvetica 12').grid(row = 2, column=2,columnspan=1)
        Label (r_e_window,text=str(die_two), font = 'Helvetica 12').grid(row = 3, column=2,columnspan=1) 
        Label (r_e_window,text=str(die_total), font = 'Helvetica 12 bold').grid(row = 4, column=2,columnspan=1) 
        Label (r_e_window,text=random_events_table[die_total], font = 'Helvetica 12 bold').grid(row = 5, column=2,columnspan=1)
        add_event('Random Event','Both','None','None',die_total,'None',random_events_table[die_total],'None')
        # adds an event to the event_log
        # event: the name of the event
        # side: which side caused the event ("Union","Confederate" or "Both")
        # unit: unit involved in the action (could be a leader)
        # location: hex location of noted action
        # die_roll: result of one or two d6
        # die_roll_mod: modifier to the die roll
        # result: result of action
        # notes: misc notes adding explanation to action
        
        
        create_lables() 
        
    r_e_roll_button = Button(r_e_window, text="Roll Random Event", command = r_e_roll, relief = RAISED)
    r_e_roll_button.grid(row = 1, column = 1, ipadx = 10, padx = 2, ipady = 5, pady = 5)  
    
    lt_button = Button(r_e_window, text="Go to Leader Transfer", command = go_to_lt, relief = RAISED)
    lt_button.grid(row = 1, column = 2, ipadx = 10, padx = 2, ipady = 5, pady = 5)  

    r_e_exit_button = Button(r_e_window, text="Exit", command = r_e_window.destroy, relief = RAISED)
    r_e_exit_button.grid(row = 1, column = 10, ipadx = 10, padx = 2, ipady = 5, pady = 5)  
    

    r_e_window.mainloop()


global_turn = 0
global_phase = 'Set-up'
global_event_log = {}
create_menus()
create_lables()
create_buttons()
top.after(5000,create_lables)
top.mainloop()