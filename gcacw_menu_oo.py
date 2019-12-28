#!/usr/bin/python
"""
Created on Sun Jul  7 15:28:06 2019

@author: sean
"""
import random
from tkinter import *
from playsound import playsound


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
    

     
    

class Welcome():
    def __init__(self,master):
        self.master=master
        self.master.geometry('604x425')
        self.master.title('Log Book for the Great Campaigns of the Civil War')
        
        self.label1=Label(self.master,text='Welcome to the Log Book for the GCACW battles',fg='red')
        self.label1.grid(row=0,column=2)

        banner_img= PhotoImage(file='battle.gif')
        self.label2=Label(self.master,image=banner_img)
        self.label2.image = banner_img
        self.label2.grid(row=1,column=0,columnspan=6)
        
        self.button1=Button(self.master,text='Begin a new Log',fg='blue',command=self.gotoDashboard).grid(row=6,column=1)
        self.button2=Button(self.master,text='Close the Logbook',fg='blue',command=self.finish).grid(row=6,column=3)
        
    def gotoDashboard(self):
        root2 = Toplevel(self.master)
        dashboard_screen = Dashboard(root2)
        
 

        
    def finish(self):
        self.master.destroy()
        
    def bugle(self):
        playsound('bugle.mp3')
        
        
class Dashboard():
    
    def __init__(self,master):



        self.master=master
        self.master.geometry('1400x700')
        self.master.title('Log Book for Bloody Spotsylvania')
        
#        background_image=PhotoImage(file='wallpaper.gif')
#        self.background_label = Label(self.master, image=background_image)
#        self.background_label.image = background_image
#        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.text_bg = 'sky blue'
                     
      
        self.banner_frame = Frame(self.master,borderwidth=5, width=100, height=500)
        self.banner_frame.grid(column=4,row=1,columnspan=7,sticky = (N,W))

        banner_img= PhotoImage(file='gcacw.gif')
        self.label_banner=Label(self.banner_frame,image=banner_img)
        self.label_banner.image = banner_img
        self.label_banner.grid(row=1,column=0)        

        self.action_button_frame = Frame(self.master,borderwidth=1)
        self.action_button_frame.grid(column=15,row=10,rowspan=5,columnspan=5)

        self.build_action_buttons()
        
        self.action_window()

        
        
        # creating a menu instance
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create the file object
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.helloCallBack)
        filemenu.add_command(label="Save", command=self.helloCallBack)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.leave)
        menubar.add_cascade(label="File", menu=filemenu)

        eventmenu = Menu(menubar, tearoff=0)
        eventmenu.add_command(label="Start a New Turn", command=self.increment_turn)
        eventmenu.add_command(label="Random Event Phase", command=self.helloCallBack)
        eventmenu.add_command(label="Leader Transfer Phase", command=self.helloCallBack)
        eventmenu.add_command(label="Initiative", command=self.helloCallBack)
        eventmenu.add_command(label="Action", command=self.helloCallBack)
        eventmenu.add_command(label="Recovery Phase", command=self.helloCallBack)
        eventmenu.add_command(label="Rollback a Turn", command=self.helloCallBack)
        menubar.add_cascade(label="Event", menu=eventmenu)
    
        reportmenu = Menu(menubar, tearoff=0)
        reportmenu.add_command(label="Unit Report", command=self.helloCallBack)
        reportmenu.add_command(label="Location Report", command=self.helloCallBack)
        reportmenu.add_command(label="Event Log", command=self.dump_event_log)
        menubar.add_cascade(label="Report", menu=reportmenu)
    
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.helloCallBack)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.update_stuff()

    def build_action_buttons(self):
        self.button_turn=Button(self.action_button_frame,text='New Turn',fg='blue',command=self.increment_turn,width=15)
        self.button_turn.grid(row = 1,column=1,pady=4,sticky=(N))
        self.button_random=Button(self.action_button_frame,text='Random Event',command=self.random_event,width=15)
        self.button_random.grid(row=2,column=1,pady=4,sticky=(NW))
        self.button_leader=Button(self.action_button_frame,text='Leader Transfer',command=self.leader_transfer,width=15)
        self.button_leader.grid(row=3,column=1,pady=4,sticky=(NW))
        self.button_initiative=Button(self.action_button_frame,text='Initiative',command=self.roll_initiative,width=15)
        self.button_initiative.grid(row=4,column=1,pady=4,sticky=(NW))
        self.button_activation=Button(self.action_button_frame,text='Ldr Activation',command=self.leader_activation,width=15)
        self.button_activation.grid(row=5,column=1,pady=4,sticky=(NW))
        self.button_march=Button(self.action_button_frame,text='Roll for March',command=self.roll_for_march,width=15)
        self.button_march.grid(row=6,column=1,pady=4,sticky=(NW))
        self.button_march=Button(self.action_button_frame,text='Extended March',command=self.roll_for_extended_march,width=15)
        self.button_march.grid(row=7,column=1,pady=4,sticky=(NW))
        self.button_march=Button(self.action_button_frame,text='Force March',command=self.roll_for_force_march,width=15)
        self.button_march.grid(row=8,column=1,pady=4,sticky=(NW))
        self.button_march=Button(self.action_button_frame,text='March',command=self.move_location,width=15)
        self.button_march.grid(row=9,column=1,pady=4,sticky=(NW))
        self.button_march=Button(self.action_button_frame,text='Cav Retreat',command=self.roll_for_cav_retreat,width=15)
        self.button_march.grid(row=10,column=1,pady=4,sticky=(NW))
        self.button_comment=Button(self.action_button_frame,text='Comment',command=self.comment,width=15)
        self.button_comment.grid(row=20,column=1,pady=4,sticky=(NW))
        
       
    def update_stuff(self):
        global global_turn
        global global_phase 
        global global_event_log  
        
        date_turn = (' ','May 8','May 9','May 10','May 11','May 12','May 13','May 14','May 15','May 16')
        
        self.status_frame = Frame(self.master, borderwidth=5, relief="sunken")
        self.status_frame.grid(column=1,row=1,columnspan=3)
        
        self.event_frame = Frame(self.master,borderwidth=5, width=900, height=500, relief="sunken")
        self.event_frame.grid_propagate(0)
        self.event_frame.grid(column=1,row=10,rowspan=20,columnspan=10,sticky=(N),padx=10,pady=10)

          

      
        
        self.button_frame = Frame(self.master)
        self.button_frame.grid(column=1, row=40, columnspan=10,sticky = (S),pady=10)
        

        
        
        banner_row = 1
        status_row = 1
        event_row = 1
        button_row = 1
        event_no = len(global_event_log)
        last_event_no = str(event_no)
        turn_text = str(global_turn) + ':  ' + date_turn[global_turn]
        
        Label (self.status_frame,text="Scenario:", font = 'Helvetica 12 bold').grid(row = status_row, column=1,columnspan=1)
        Label (self.status_frame,text="Bloody Spotsylvania", font = 'Helvetica 12').grid(row = status_row, column=2,columnspan=2)  
    
        Label (self.status_frame,text="Turn:", font = 'Helvetica 12 bold').grid(row = status_row + 1, column=1,columnspan=1)
        self.turn_label = Label (self.status_frame,text=turn_text, font = 'Helvetica 12').grid(row = status_row + 1, column=2,columnspan=1)
        
        
        Label (self.status_frame,text="Phase:", font = 'Helvetica 12 bold').grid(row = status_row + 2, column=1,columnspan=1)
        Label (self.status_frame,text=global_phase, font = 'Helvetica 12').grid(row = status_row + 2, column=2,columnspan=1)
        
        
        
    
        # event: the name of the event
        # side: which side caused the event ("Union","Confederate" or "Both")
        # unit: unit involved in the action (could be a leader)
        # location: hex location of noted action
        # die_roll: result of one or two d6
        # die_roll_mod: modifier to the die roll
        # result: result of action
        # notes: misc notes adding explanation to action
        
        header_font = 'Helvetica 12 bold'
        detail_font = 'Helvetica 10'
    
        Label (self.event_frame,text="#", font = header_font,relief=RAISED,width=4).grid(row = event_row, column=1,columnspan=1)    
        Label (self.event_frame,text="Event Type", font = header_font,relief=RAISED,width=12).grid(row = event_row, column=2,columnspan=1)
        Label (self.event_frame,text="Side", font = header_font,relief=RAISED,width=8).grid(row = event_row, column=3,columnspan=1)    
        Label (self.event_frame,text="Unit", font = header_font,relief=RAISED,width=6).grid(row = event_row, column=4,columnspan=1)
        Label (self.event_frame,text="Location", font = header_font,relief=RAISED).grid(row = event_row, column=5,columnspan=1)    
        Label (self.event_frame,text="Roll", font = header_font,relief=RAISED).grid(row = event_row, column=6,columnspan=1)
        Label (self.event_frame,text="Mod", font = header_font,relief=RAISED).grid(row = event_row, column=7,columnspan=1)    
        Label (self.event_frame,text="Result", font = header_font,relief=RAISED,width=15).grid(row = event_row, column=8,columnspan=3)
        Label (self.event_frame,text="Notes", font = header_font,relief=RAISED,width=26).grid(row = event_row, column=11,columnspan=3)
    
        itera = 0
        max_rows = 18
        next_row=event_no - max_rows
        if next_row < 1: next_row = 1
        last_row=event_no + 1
        if event_no > 0:
            for loop_row in range(next_row,last_row):
                this_event_no = event_no - itera
                this_row = loop_row + 1
                itera += 1
                Label (self.event_frame,text=this_event_no, font = detail_font).grid(row = this_row, column=1,columnspan=1)
                Label (self.event_frame,text=global_event_log[this_event_no][0], font = detail_font).grid(row = this_row, column=2,columnspan=1)
                Label (self.event_frame,text=global_event_log[this_event_no][1], font = detail_font).grid(row = this_row, column=3,columnspan=1)
                Label (self.event_frame,text=global_event_log[this_event_no][2], font = detail_font).grid(row = this_row, column=4,columnspan=1)
                Label (self.event_frame,text=global_event_log[this_event_no][3], font = detail_font).grid(row = this_row, column=5,columnspan=1)
                Label (self.event_frame,text=global_event_log[this_event_no][4], font = detail_font).grid(row = this_row, column=6,columnspan=1)
                Label (self.event_frame,text=global_event_log[this_event_no][5], font = detail_font).grid(row = this_row, column=7,columnspan=1)
                Label (self.event_frame,text=global_event_log[this_event_no][6], font = detail_font, fg = 'blue').grid(row = this_row, column=8,columnspan=3)
                Label (self.event_frame,text=global_event_log[this_event_no][7], font = detail_font).grid(row = this_row, column=11,columnspan=3)




                
       
        self.button_exit=Button(self.button_frame,text='Close this Log',fg='blue',command=self.leave).grid(row = button_row,column=2)

        
    def roll_dice(self,num_dice):
        die_list = []
        die_total = 0
        for each_die in range(1,num_dice+1):
            die_result = random.randrange(6)+1
            die_list.append(die_result)
            die_total += die_result    
            
        return(die_total,die_list)
   
    def dump_event_log(self):
        print(global_event_log)
        
    def helloCallBack(self):
        self.msg = messagebox.showinfo( "Coming Soon", "This feature has not been built yet")
        
    def leave(self):
        self.master.destroy()
        
    def random_event(self):
        global global_phase
        
        self.action_window()
        
        random_events_table = {
        2:"Rain (Current +2)",
        3:"Rain (Current +1)*",
        4:"No Effect**",
        5:"Rain (Current)*",
        6:"Union Paralysis",
        7:"Union Night March",
        8:"No Effect++",
        9:"Confederate Paralysis",
        10:"Confederate Paralysis",
        11:"No Effect++",
        12:"Rain (Current +1)"
        }

        text_bg = 'sky blue'
        confirm = False
        
        die_results = self.roll_dice(2)
        die_total = die_results[0]
        die_one = die_results[1][0]
        die_two = die_results[1][1]

        
        Label (self.action_frame,text="Die One:", font = 'Helvetica 12 bold',bg=text_bg).grid(row = 2, column=1,columnspan=1)
        Label (self.action_frame,text="Die Two:", font = 'Helvetica 12 bold',bg=text_bg).grid(row = 3, column=1,columnspan=1) 
        Label (self.action_frame,text="Total:", font = 'Helvetica 12 bold',bg=text_bg).grid(row = 4, column=1,columnspan=1) 
        Label (self.action_frame,text=str(die_one), font = 'Helvetica 12',bg=text_bg).grid(row = 2, column=2,columnspan=1)
        Label (self.action_frame,text=str(die_two), font = 'Helvetica 12',bg=text_bg).grid(row = 3, column=2,columnspan=1) 
        Label (self.action_frame,text=str(die_total), font = 'Helvetica 12 bold',bg=text_bg).grid(row = 4, column=2,columnspan=1) 
        Label (self.action_frame,text=random_events_table[die_total], font = 'Helvetica 12 bold',bg=text_bg).grid(row = 5, column=2,columnspan=1)
        
        
        add_event('Random Event','Both','-','-',die_total,'-',random_events_table[die_total],'-')


        global_phase='Random Events'
        self.update_stuff()
        
    def leader_transfer(self):
        
        def do_it():
            side_num = choice.get()
            leader_value = leader_entry.get()
            location_value = location_entry.get()
            unit_value = unit_entry.get()
            
            if side_num == 1: side_value = 'Union'
            else: side_value = 'Confederate'
    
            add_event('Leader Transfer',side_value,leader_value,location_value,'-','-','-',unit_value)
            self.action_window()
            self.update_stuff()
        
        self.action_window()
        
        choice = IntVar()
        choice.set(1)
        Label(self.action_frame, text="Side:").grid(row=1,column =1,sticky=W)
        Radiobutton(self.action_frame,text="Union",padx=20,variable=choice,value=1,bg='sky blue').grid(row=2,column=1,sticky=W)
        Radiobutton(self.action_frame,text="Confederate",padx=20,variable=choice,value=2).grid(row=3,column=1,sticky=W)

        Label(self.action_frame, text="Leader:").grid(row=4,column =1,sticky=W)
        leader_entry = Entry(self.action_frame)
        leader_entry.grid(row=4,column=2,pady=4)
        
        Label(self.action_frame, text="New Location:").grid(row=5,column=1,sticky=W)
        location_entry = Entry(self.action_frame)
        location_entry.grid(row=5,column=2,pady=4)
        
        Label(self.action_frame, text="Unit Attached to:").grid(row=6,column=1,sticky=W)
        unit_entry = Entry(self.action_frame)
        unit_entry.grid(row=6,column=2,pady=4,padx=4)
        
        
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=10, column=1, sticky=W, padx=4)
        Button(self.action_frame, text='OK', command=do_it).grid(row=10, column=2, sticky=W, padx=4)

        
    def roll_initiative(self):
        global global_phase
        
        self.action_window()

        
        die_results = self.roll_dice(2)
        die_total = die_results[0]
        die_confederate = die_results[1][0]
        die_union = die_results[1][1]
        
        
        
        init_result = ""
        if die_union > die_confederate: init_result = "Union initiative" 
        else: init_result = "Confederate initiative"
        Label (self.action_frame,text="Confederate Die:", font = 'Helvetica 12',bg=self.text_bg).grid(row = 2, column=1,columnspan=1)
        Label (self.action_frame,text="Union Die:", font = 'Helvetica 12',bg=self.text_bg).grid(row = 3, column=1,columnspan=1) 
        Label (self.action_frame,text="Winner:", font = 'Helvetica 12 bold',bg=self.text_bg).grid(row = 4, column=1,columnspan=1) 
        Label (self.action_frame,text=str(die_confederate), font = 'Helvetica 12',bg=self.text_bg).grid(row = 2, column=2,columnspan=1)
        Label (self.action_frame,text=str(die_union), font = 'Helvetica 12',bg=self.text_bg).grid(row = 3, column=2,columnspan=1) 
        Label (self.action_frame,text=init_result, font = 'Helvetica 12 bold',fg='dark blue',bg=self.text_bg).grid(row = 4, column=2,columnspan=1) 
        add_event('Initiative','Union','-','-',die_union,'-',init_result,'-')
        add_event('Initiative','Confederate','-','-',die_confederate,'-',init_result,'-')
        # adds an event to the event_log
        # event: the name of the event
        # side: which side caused the event ("Union","Confederate" or "Both")
        # unit: unit involved in the action (could be a leader)
        # location: hex location of noted action
        # die_roll: result of one or two d6
        # die_roll_mod: modifier to the die roll
        # result: result of action
        # notes: misc notes adding explanation to action

        
        global_phase='Initiative'
        
        self.update_stuff()


        
    def leader_activation(self):
        
        def do_it():
            side_num = choice.get()
            leader_value = leader_entry.get()
            dice_value = int(dice_entry.get())
            mod_value = int(mod_entry.get())
            unit_value = unit_entry.get()
            
            if side_num == 1: side_value = 'Union'
            else: side_value = 'Confederate'
            
            dice_result = self.roll_dice(dice_value)
            dice_total = dice_result[0]
            event_value = dice_total+mod_value
            
    
            add_event('Activation',side_value,leader_value,'-',dice_total,mod_value,event_value,unit_value)
            self.update_stuff()
            self.action_window()
    
            alabel,blabel,clabel,dlabel,dice_value,result_value = self.die_window(dice_result,mod_value)
            alabel
            blabel
            clabel
            dlabel           
                        
        
        self.action_window()
        
        choice = IntVar()
        choice.set(1)
        Label(self.action_frame, text="Side:").grid(row=1,column =1,sticky=W)
        Radiobutton(self.action_frame,text="Union",padx=20,variable=choice,value=1).grid(row=2,column=1,sticky=W)
        Radiobutton(self.action_frame,text="Confederate",padx=20,variable=choice,value=2).grid(row=3,column=1,sticky=W)
        
        

        Label(self.action_frame, text="Leader:").grid(row=4,column =1,sticky=W)
        leader_entry = Entry(self.action_frame)
        leader_entry.grid(row=4,column=2,pady=4)
        
        Label(self.action_frame, text="Units:").grid(row=5,column=1,sticky=W)
        unit_entry = Entry(self.action_frame)
        unit_entry.grid(row=5,column=2,pady=4)
        
        Label(self.action_frame, text="# Dice").grid(row=6,column=1,sticky=W)
        dice_entry = Entry(self.action_frame)
        dice_entry.grid(row=6,column=2,pady=4,padx=4)
        
        Label(self.action_frame, text="Mod").grid(row=7,column=1,sticky=W)
        mod_entry = Entry(self.action_frame)
        mod_entry.grid(row=7,column=2,pady=4,padx=4)
        
        
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=10, column=1, sticky=W, padx=4, pady = 10)
        Button(self.action_frame, text='OK', command=do_it).grid(row=10, column=2, sticky=W, padx=4, pady=10)       
        
    def roll_for_march(self):

#        def enable_dice_options():
#            Label(self.action_frame, text="# Dice").grid(row=8,column=1,sticky=W)
#            dice_entry = Entry(self.action_frame,state=DISABLED if activation.get() else NORMAL)
#            dice_entry.grid(row=8,column=2,pady=4,padx=4)
#            
#            Label(self.action_frame, text="Mod").grid(row=9,column=1,sticky=W)
#            mod_entry = Entry(self.action_frame,state=DISABLED if activation.get() else NORMAL)
#            mod_entry.grid(row=9,column=2,pady=4,padx=4)


        
        def do_it():
            side_num = choice.get()
            location_value = "-"

            unit_value = unit_entry.get()
            route_value= "-"
            active_num = 0
            


            dice_num = int(dice_entry.get())
            mod_value = int(mod_entry.get())
            march_text = 'Unit March Roll'
            dice_result = self.roll_dice(dice_num)
            dice_value = dice_result[0]
            result_value = dice_value + mod_value
            self.action_window()

            alabel,blabel,clabel,dlabel,dice_value,result_value = self.die_window(dice_result,mod_value)
            alabel
            blabel
            clabel
            dlabel           
                     
       
            if side_num == 1: side_value = 'Union'
            else: side_value = 'Confederate'
            

            add_event(march_text,side_value,unit_value,location_value,dice_value,mod_value,result_value,route_value)

            self.update_stuff()
        
        self.action_window()
        
        choice = IntVar()
        choice.set(1)
        Label(self.action_frame, text="Side:").grid(row=1,column =1,sticky=W)
        Radiobutton(self.action_frame,text="Union",padx=20,variable=choice,value=1).grid(row=2,column=1,sticky=W)
        Radiobutton(self.action_frame,text="Confederate",padx=20,variable=choice,value=2).grid(row=3,column=1,sticky=W)
        
        Label(self.action_frame, text="Unit").grid(row=4,column=1,sticky=W)
        unit_entry = Entry(self.action_frame)
        unit_entry.grid(row=4,column=2,pady=4)
        
#        activation = IntVar()
#        Checkbutton(self.action_frame, text="Part of Leader Activation", variable=activation,
#                    command=enable_dice_options).grid(row=7,column=1)
        
        Label(self.action_frame, text="# Dice").grid(row=8,column=1,sticky=W)
        dice_entry = Entry(self.action_frame)
        dice_entry.grid(row=8,column=2,pady=4,padx=4)
        
        Label(self.action_frame, text="Mod").grid(row=9,column=1,sticky=W)
        mod_entry = Entry(self.action_frame)
        mod_entry.grid(row=9,column=2,pady=4,padx=4)


      
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=10, column=1, sticky=W, padx=4, pady = 10)
        Button(self.action_frame, text='OK', command=do_it).grid(row=10, column=2, sticky=W, padx=4, pady=10)         


    def roll_for_extended_march(self):

        
        def do_it():
            side_num = choice.get()
            location_value = "-"

            unit_value = unit_entry.get()
            route_value= "-"
            dice_num = 1
            mod_value = int(mod_entry.get())
            march_text = 'Extended March'
            dice_result = self.roll_dice(dice_num)
            dice_value = dice_result[0]
            result_value = dice_value + mod_value
            self.action_window()

            alabel,blabel,clabel,dlabel,dice_value,result_value = self.die_window(dice_result,mod_value)
            alabel
            blabel
            clabel
            dlabel           
                     
            
            if side_num == 1: side_value = 'Union'
            else: side_value = 'Confederate'
            

            add_event(march_text,side_value,unit_value,location_value,dice_value,mod_value,result_value,route_value)

            self.update_stuff()
        
        self.action_window()
        
        choice = IntVar()
        choice.set(1)
        Label(self.action_frame, text="Side:").grid(row=1,column =1,sticky=W)
        Radiobutton(self.action_frame,text="Union",padx=20,variable=choice,value=1).grid(row=2,column=1,sticky=W)
        Radiobutton(self.action_frame,text="Confederate",padx=20,variable=choice,value=2).grid(row=3,column=1,sticky=W)
        
        Label(self.action_frame, text="Unit").grid(row=4,column=1,sticky=W)
        unit_entry = Entry(self.action_frame)
        unit_entry.grid(row=4,column=2,pady=4)
        
              
        Label(self.action_frame, text="Mod").grid(row=9,column=1,sticky=W)
        mod_entry = Entry(self.action_frame)
        mod_entry.grid(row=9,column=2,pady=4,padx=4)


      
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=10, column=1, sticky=W, padx=4, pady = 10)
        Button(self.action_frame, text='OK', command=do_it).grid(row=10, column=2, sticky=W, padx=4, pady=10)   
        
        
    def roll_for_force_march(self):

#        def enable_dice_options():
#            Label(self.action_frame, text="# Dice").grid(row=8,column=1,sticky=W)
#            dice_entry = Entry(self.action_frame,state=DISABLED if activation.get() else NORMAL)
#            dice_entry.grid(row=8,column=2,pady=4,padx=4)
#            
#            Label(self.action_frame, text="Mod").grid(row=9,column=1,sticky=W)
#            mod_entry = Entry(self.action_frame,state=DISABLED if activation.get() else NORMAL)
#            mod_entry.grid(row=9,column=2,pady=4,padx=4)


        
        def do_it():
            side_num = choice.get()
            location_value = "-"

            unit_value = unit_entry.get()
            route_value= "-"
            active_num = 0
            


            dice_num = int(dice_entry.get())
            mod_value = int(mod_entry.get())
            march_text = 'Force March'
            dice_result = self.roll_dice(dice_num)
            dice_value = dice_result[0]
            result_value = dice_value + mod_value
            self.action_window()
            
            alabel,blabel,clabel,dlabel,dice_value,result_value = self.die_window(dice_result,mod_value)
            alabel
            blabel
            clabel
            dlabel           
        
        

        
            if side_num == 1: side_value = 'Union'
            else: side_value = 'Confederate'
            

            add_event(march_text,side_value,unit_value,location_value,dice_value,mod_value,result_value,route_value)

            self.update_stuff()
        
        self.action_window()
        
        choice = IntVar()
        choice.set(1)
        Label(self.action_frame, text="Side:").grid(row=1,column =1,sticky=W)
        Radiobutton(self.action_frame,text="Union",padx=20,variable=choice,value=1).grid(row=2,column=1,sticky=W)
        Radiobutton(self.action_frame,text="Confederate",padx=20,variable=choice,value=2).grid(row=3,column=1,sticky=W)
        
        Label(self.action_frame, text="Unit").grid(row=4,column=1,sticky=W)
        unit_entry = Entry(self.action_frame)
        unit_entry.grid(row=4,column=2,pady=4)
        
#        activation = IntVar()
#        Checkbutton(self.action_frame, text="Part of Leader Activation", variable=activation,
#                    command=enable_dice_options).grid(row=7,column=1)
        
        Label(self.action_frame, text="# Dice").grid(row=8,column=1,sticky=W)
        dice_entry = Entry(self.action_frame)
        dice_entry.grid(row=8,column=2,pady=4,padx=4)
        
        Label(self.action_frame, text="Mod").grid(row=9,column=1,sticky=W)
        mod_entry = Entry(self.action_frame)
        mod_entry.grid(row=9,column=2,pady=4,padx=4)


      
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=10, column=1, sticky=W, padx=4, pady = 10)
        Button(self.action_frame, text='OK', command=do_it).grid(row=10, column=2, sticky=W, padx=4, pady=10)         
        
        


    def move_location(self):
        
        def do_it():
            side_num = choice.get()
            unit_value = unit_entry.get()
            location_value = location_entry.get()
            route_value = route_entry.get()
            
            if side_num == 1: side_value = 'Union'
            else: side_value = 'Confederate'
    
            add_event('March',side_value,unit_value,location_value,'-','-','-',route_value)
            self.action_window()
            self.update_stuff()
        
        self.action_window()
        
        choice = IntVar()
        choice.set(1)
        Label(self.action_frame, text="Side:").grid(row=1,column =1,sticky=W)
        Radiobutton(self.action_frame,text="Union",padx=20,variable=choice,value=1,bg='sky blue').grid(row=2,column=1,sticky=W)
        Radiobutton(self.action_frame,text="Confederate",padx=20,variable=choice,value=2).grid(row=3,column=1,sticky=W)

        Label(self.action_frame, text="Unit:").grid(row=4,column =1,sticky=W)
        unit_entry = Entry(self.action_frame)
        unit_entry.grid(row=4,column=2,pady=4)
        
        Label(self.action_frame, text="New Location:").grid(row=5,column=1,sticky=W)
        location_entry = Entry(self.action_frame)
        location_entry.grid(row=5,column=2,pady=4)
        
        Label(self.action_frame, text="Route:").grid(row=6,column=1,sticky=W)
        route_entry = Entry(self.action_frame)
        route_entry.grid(row=6,column=2,pady=4,padx=4)
        
        
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=10, column=1, sticky=W, padx=4)
        Button(self.action_frame, text='OK', command=do_it).grid(row=10, column=2, sticky=W, padx=4)
        
        
    def roll_for_cav_retreat(self):

       
        def do_it():
            side_num = choice.get()
            location_value = location_entry.get()

            unit_value = unit_entry.get()
            route_value= route_entry.get()
           
            dice_num = 1
            mod_value = int(mod_entry.get())
            march_text = 'Cav Retreat'
            dice_result = self.roll_dice(dice_num)


            self.action_window()

            alabel,blabel,clabel,dlabel,dice_value,result_value = self.die_window(dice_result,mod_value)
            alabel
            blabel
            clabel
            dlabel
        
            if side_num == 1: side_value = 'Union'
            else: side_value = 'Confederate'
            

            add_event(march_text,side_value,unit_value,location_value,dice_value,mod_value,result_value,route_value)

            self.update_stuff()
        
        self.action_window()
        
        choice = IntVar()
        choice.set(1)
        Label(self.action_frame, text="Side:").grid(row=1,column =1,sticky=W)
        Radiobutton(self.action_frame,text="Union",padx=20,variable=choice,value=1).grid(row=2,column=1,sticky=W)
        Radiobutton(self.action_frame,text="Confederate",padx=20,variable=choice,value=2).grid(row=3,column=1,sticky=W)
        
        Label(self.action_frame, text="Unit").grid(row=4,column=1,sticky=W)
        unit_entry = Entry(self.action_frame)
        unit_entry.grid(row=4,column=2,pady=4)
        
        Label(self.action_frame, text="Mod").grid(row=5,column=1,sticky=W)
        mod_entry = Entry(self.action_frame)
        mod_entry.grid(row=5,column=2,pady=4,padx=4)
        
        Label(self.action_frame, text="Final location").grid(row=6,column=1,sticky=W)
        location_entry = Entry(self.action_frame)
        location_entry.grid(row=6,column=2,pady=4,padx=4)
        
        Label(self.action_frame, text="Route").grid(row=7,column=1,sticky=W)
        route_entry = Entry(self.action_frame)
        route_entry.grid(row=7,column=2,pady=4,padx=4)


      
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=10, column=1, sticky=W, padx=4, pady = 10)
        Button(self.action_frame, text='OK', command=do_it).grid(row=10, column=2, sticky=W, padx=4, pady=10)    
        



    def comment(self):
        
        def show_it():
            union_num = union.get()
            confed_num= confed.get()
            comment_entry = p_comment.get()
            if (union_num == 1) and (confed_num ==1):
                event_side = 'Both'
            elif union_num == 1:
                event_side = 'Union'
            elif confed_num == 1:
                event_side = 'Confederate'
            else: event_side = 'None'
    
            add_event('Comment',event_side,'-','-','-','-',comment_entry,'-')
            self.action_window()
            self.update_stuff()
        
        self.action_window()
        union = IntVar()
        confed = IntVar()
        Checkbutton(self.action_frame, text="Union", variable=union).grid(row=1,column=1)
        Checkbutton(self.action_frame, text="Confederate", variable=confed).grid(row=1,column=2)
        Label(self.action_frame, text="Comment:").grid(row=2,column =1,sticky=W,pady=4)
        p_comment = Entry(self.action_frame)
        p_comment.grid(row=2,column=2)
        Button(self.action_frame, text='Cancel', command=self.action_window).grid(row=3, column=1, sticky=W, padx=4)
        Button(self.action_frame, text='OK', command=show_it).grid(row=3, column=2, sticky=W, padx=4)
        

        
    def action_window(self):
        try:
            self.action_frame.destroy()
        except:
            print('First Run')
        self.action_frame = Frame(self.master,width=300,height=300,relief="sunken",bg='skyblue',bd=1)
        self.action_frame.grid(column=20,row=10,columnspan=10,rowspan=10,sticky = (N,W),padx=10)
        self.action_frame.grid_propagate(0)
        
        
    def increment_turn(self):
        global global_turn
        global global_phase
        
        self.action_window()
        
        global_turn += 1
        global_phase = 'Starting New Turn'        
        add_event('New Turn','Both','-','-','-','-','Turn #' + str(global_turn),'-')
                 
        self.update_stuff()
        
    
    def die_window(self,dice_result,mod_value):    
        for die_num,each_die in enumerate(dice_result[1]):
            die_num_text = 'Die Roll #' + str(die_num+1) + ': '
            Label (self.action_frame,text=die_num_text, font = 'Helvetica 12 bold',bg=self.text_bg).grid(row = die_num, column=1,columnspan=1) 
            Label (self.action_frame,text=each_die, font = 'Helvetica 12 bold',bg=self.text_bg).grid(row = die_num, column=2,columnspan=1) 
                                
        dice_value = dice_result[0]
        result_value = dice_value + mod_value
        alabel = Label (self.action_frame,text="Total Die Roll:", font = 'Helvetica 12 bold',bg=self.text_bg).grid(row = 5, column=1,columnspan=1) 
        blabel = Label (self.action_frame,text=dice_value, font = 'Helvetica 12 bold',fg='dark blue',bg=self.text_bg).grid(row = 5, column=2,columnspan=1) 
        clabel = Label (self.action_frame,text="Total after Mod:", font = 'Helvetica 12 bold',bg=self.text_bg).grid(row = 6, column=1,columnspan=1) 
        dlabel = Label (self.action_frame,text=result_value, font = 'Helvetica 12 bold',fg='dark blue',bg=self.text_bg).grid(row = 6, column=2,columnspan=1) 
        return(alabel,blabel,clabel,dlabel,dice_value,result_value)
        
        
        
        

def main():
    root = Tk()
    welcome_screen = Welcome(root)
    root.mainloop()
    
    
# Set Global Variables to be used to track progress
global_turn = 0
global_phase = 'Set-up'
global_event_log = {}    

if __name__ == '__main__':
    main()
