import time
import tkinter as tk
from threading import *


button_pushed = [0,0,0,0,0,0] # button for 1 ~ 6 floors
power_on_off = False
current_state = 0
state_list = ["idle","move up", "move down"]
current_floor = 1
movement = "idle"
pow = False

def elevator():
    global t1    
    t1 = Thread(target = fsm)
    t1.start()
    create_gui() 


def fsm():
    global current_state, state_list, button_pushed, movement, current_floor,label_1, label_floor
    while(True):
        if(power_on_off):
            if current_state == 0:
                if cs() == "up":
                    current_state = 1
                    current_floor+=1
                elif cs() == "down":
                    current_state = 2
                    current_floor-=1
            
            elif current_state == 1:
                if cs() == "down":
                    current_state = 2
                    current_floor-=1
                elif cs() == "idle":
                    current_state = 0
                else:
                    current_floor+=1

            elif current_state == 2:
                if cs() == "up":
                    current_state = 1
                    current_floor+=1
                elif cs() == "idle":
                    current_state = 0
                else:
                    current_floor-=1
            print(state_list[current_state])
            button_pushed[current_floor-1] = 0
            print(current_floor)
            print(button_pushed)
            label_1.configure(text=state_list[current_state])
            label_floor.configure(text = current_floor)
            time.sleep(2)
        
        
def cs():
    global button_pushed, current_floor, movement
    if  current_state == 0 or current_state == 1:
        if 1 in [x for x in button_pushed[current_floor:]]:
            return "up"
        elif 1 in [x for x in button_pushed[:current_floor]]:
            return "down"
        else:
            return "idle" 
    elif  current_state == 2:
        if 1 in [x for x in button_pushed[:current_floor]]:
            return "dwon"
        elif 1 in [x for x in button_pushed[current_floor:]]:
            return "up"
        else:
            return "idle"
    

def press_button(arg):
    global button_pushed
    button_pushed[arg-1] = 1

def onof():
    global power_on_off
    if(not power_on_off):
        power_on_off = True
    else:
        power_on_off = False

def create_gui():
    global current_state, state_list, button_pushed, moveu, label_1, label_floor 
    window = tk.Tk()
    window.config(bg = "GRAY")
    window.geometry("1400x800")
    window.title("elevator simulator")

    #title
    frame_title = tk.Frame(window, width = 1200, bg = "WHITE")
    title_label = tk.Label(frame_title, bg="WHITE", fg = "BLACK", font=("Arial", 32), text = "elevator simulator")
    title_label.pack()

    #floor buttons
    canvas1 = tk.Canvas(window,bg = "WHITE", width= 200, height=600)
    b1 = tk.Button(window, pady= 5, padx = 20, text = "^", command = lambda: press_button(1))
    b2 = tk.Button(window, text = "2", command = lambda: press_button(2))
    b3 = tk.Button(window, text = "3", command = lambda: press_button(3))
    b4 = tk.Button(window, text = "4", command = lambda: press_button(4))
    b5 = tk.Button(window, text = "5", command = lambda: press_button(5))
    b6u = tk.Button(window, text = "\u25B2", command = lambda: press_button(6))
    b6d = tk.Button(window, text = "\u25BC", command = lambda: press_button(6))

    label_6st = tk.Label(window, padx = 5, pady = 17, text = "6", anchor=tk.W)

    canvas1.create_window(50,200, anchor=tk.W, window=b1)
    canvas1.create_window(10,150, anchor=tk.W, window=b2)
    canvas1.create_window(10,290, anchor=tk.W, window=b3)
    canvas1.create_window(10,330, anchor=tk.W, window=b4)
    canvas1.create_window(10,470, anchor=tk.W, window=b5)
    
    canvas1.create_window(73,28, anchor=tk.W, window=b6u)
    canvas1.create_window(73,54, anchor=tk.W, window=b6d)
    canvas1.create_window(50,41, anchor=tk.W, window=label_6st)

    #elevator
    canvas2 = tk.Canvas(window,bg = "WHITE", width= 500, height=600)
    b1 = tk.Button(window, pady= 15, padx = 10, text = "1", command = lambda: press_button(1))
    b2 = tk.Button(window, pady = 15, padx = 10,text = "2", command = lambda: press_button(2))
    b3 = tk.Button(window, pady = 15, padx = 10, text = "3", command = lambda: press_button(3))
    b4 = tk.Button(window, pady = 15, padx = 10, text = "4", command = lambda: press_button(4))
    b5 = tk.Button(window, pady = 15, padx =10, text = "5", command = lambda: press_button(5))
    bo = tk.Button(window, pady = 15, padx =5, text = "<>", command = lambda: press_button(5))
    bc = tk.Button(window, pady = 15, padx =5, text = "><", command = lambda: press_button(5))
    bof = tk.Button(window, pady = 15, padx =5, text = "power", command = onof)
    label_1 = tk.Label(window, width= 30, padx = 65, pady = 5, text = "Power off ...", anchor=tk.W)
    label_floor = tk.Label(window, padx = 10, pady = 10, text = "1", anchor=tk.W)

    canvas2.create_window(430,490, anchor=tk.W, window=b1)
    canvas2.create_window(350,490, anchor=tk.W, window=b2)
    canvas2.create_window(430,420, anchor=tk.W, window=b3)
    canvas2.create_window(350,420, anchor=tk.W, window=b4)
    canvas2.create_window(430,350, anchor=tk.W, window=b5)
    canvas2.create_window(430,560, anchor=tk.W, window=bo)
    canvas2.create_window(350,560, anchor=tk.W, window=bc)
    canvas2.create_window(20,560,anchor=tk.W, window=bof)
    canvas2.create_window(50,50, anchor=tk.NW, window=label_1)
    canvas2.create_window(50,150, anchor=tk.NW, window=label_floor)



    #FSM
    canvas3 = tk.Canvas(window, bg ="GREEN", width=500, height=600)
   
    label_2 = tk.Label(window, text = "alphabet", bg = "GREEN", anchor=tk.W)
    button_2 = tk.Button(window, text = "button",highlightbackground="GREEN", anchor=tk.W)
    canvas3.create_window(50,50, anchor=tk.NW, window=label_2)
    canvas3.create_window(150,150, anchor=tk.NW, window=button_2)

    frame_title.grid(row = 0, column =0, columnspan = 3, sticky="snew")
    canvas1.grid(row = 1, column = 0, sticky="")
    canvas2.grid(row=1,column=1, sticky="")
    canvas3.grid(row=1,column=2,sticky="")

    window.grid_rowconfigure(0,weight=1)
    window.grid_rowconfigure(1, weight=8)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1,weight=3)
    window.grid_columnconfigure(2,weight=3)
    window.mainloop()






if __name__ == "__main__":
    elevator()
