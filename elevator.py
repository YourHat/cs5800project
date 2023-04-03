import time
import tkinter as tk
from threading import *


button_pushed = [0,0,0,0,0,0,0,0] # button for 1 ~ 8 floors
power_on_off = False
current_state = 0
state_list = ["Idle","Move Up", "Move Down","Stop","Stop","Open Door","Open Door","Close Door","Close Door"]
current_floor = 1
movement = "idle"
pow = False

def elevator():
    global t1    
    t1 = Thread(target = fsm)
    t1.start()
    create_gui() 


def fsm():
    global current_state, state_list, button_pushed, movement, current_floor,label_1,label_floor
    global canvas3, state_idel_c,state_md_c,state_mu_c
    global state_u_stop_c, state_u_open_c, state_u_close_c
    global state_d_stop_c, state_d_open_c, state_d_close_c

    while(True):
        if(power_on_off):
            if current_state == 0:
                if 1 in [x for x in button_pushed[current_floor:]]:
                    current_state = 1
                    canvas3.itemconfig(state_idel_c, fill="WHITE")
                    canvas3.itemconfig(state_mu_c, fill= "ORANGE")
                elif 1 in [x for x in button_pushed[:current_floor]]:
                    current_state = 2
                    canvas3.itemconfig(state_idel_c, fill="WHITE")
                    canvas3.itemconfig(state_md_c, fill= "ORANGE")
            elif current_state == 1:
                if button_pushed[current_floor-1] == 1:
                    b_l[current_floor-1].configure(highlightbackground="WHITE")
                    b_u[current_floor-1].configure(highlightbackground="WHITE")
                    b_d[current_floor-1].configure(highlightbackground="WHITE")
                    current_state = 3
                    canvas3.itemconfig(state_mu_c, fill="WHITE")
                    canvas3.itemconfig(state_u_stop_c, fill= "ORANGE")
                else:
                    button_pushed[current_floor-1] = 0
                    current_floor+=1
            elif current_state == 2:
                if button_pushed[current_floor-1] == 1:
                    b_l[current_floor-1].configure(highlightbackground="WHITE")
                    b_u[current_floor-1].configure(highlightbackground="WHITE")
                    b_d[current_floor-1].configure(highlightbackground="WHITE") 
                    current_state = 4
                    canvas3.itemconfig(state_md_c, fill="WHITE")
                    canvas3.itemconfig(state_d_stop_c, fill= "ORANGE")
                else:
                    button_pushed[current_floor-1] = 0
                    current_floor-=1
            elif current_state == 3:
                time.sleep(1)
                current_state = 5
                canvas3.itemconfig(state_u_stop_c, fill="WHITE")
                canvas3.itemconfig(state_u_open_c, fill= "ORANGE")
            elif current_state == 4:
                time.sleep(1)
                current_state = 6
                canvas3.itemconfig(state_d_stop_c, fill="WHITE")
                canvas3.itemconfig(state_d_open_c, fill= "ORANGE")

            elif current_state == 5:
                time.sleep(2)
                current_state = 7
                canvas3.itemconfig(state_u_open_c, fill="WHITE")
                canvas3.itemconfig(state_u_close_c, fill= "ORANGE")

            elif current_state == 6:
                time.sleep(2)
                current_state = 8
                canvas3.itemconfig(state_d_open_c, fill="WHITE")
                canvas3.itemconfig(state_d_close_c, fill= "ORANGE")

            elif current_state == 7:
                if 1 in [x for x in button_pushed[current_floor:]]:
                    current_state = 1
                    current_floor+=1
                    canvas3.itemconfig(state_u_close_c, fill="WHITE")
                    canvas3.itemconfig(state_mu_c, fill= "ORANGE")
                elif 1 in [x for x in button_pushed[:current_floor+1]]:
                    current_state = 2
                    current_floor-=1                    
                    canvas3.itemconfig(state_u_close_c, fill="WHITE")
                    canvas3.itemconfig(state_md_c, fill= "ORANGE")
                else:
                    current_state = 0
                    canvas3.itemconfig(state_u_close_c, fill="WHITE")
                    canvas3.itemconfig(state_idel_c, fill= "ORANGE")

            elif current_state == 8:
                if 1 in [x for x in button_pushed[:current_floor+1]]:
                    current_state = 2
                    current_floor-=1
                    canvas3.itemconfig(state_d_close_c, fill="WHITE")
                    canvas3.itemconfig(state_md_c, fill= "ORANGE")
                elif 1 in [x for x in button_pushed[current_floor:]]:
                    current_state = 1
                    current_floor+=1                    
                    canvas3.itemconfig(state_d_close_c, fill="WHITE")
                    canvas3.itemconfig(state_mu_c, fill= "ORANGE")
                else:
                    current_state = 0
                    canvas3.itemconfig(state_d_close_c, fill="WHITE")
                    canvas3.itemconfig(state_idel_c, fill= "ORANGE")


            print(button_pushed)
            print(current_floor)
            label_1.configure(text=state_list[current_state])
            label_floor.configure(text = current_floor)
            time.sleep(1)
        

    

def press_button(arg,bk):
    global button_pushed
    
    button_pushed[arg-1] = 1
    match bk:
        case 0:
            b_l[arg-1].configure(highlightbackground="PINK")
        case 1:
            b_u[arg-1].configure(highlightbackground="PINK")
        case 2:
            b_d[arg-1].configure(highlightbackground="PINK")

def onof():
    global power_on_off
    if(not power_on_off):
        power_on_off = True
        bof.configure(highlightbackground="GREEN")
    else:
        power_on_off = False
        bof.configure(highlightbackground="RED")

def create_gui():
    global current_state, state_list, button_pushed, moveu, label_1, label_floor 
    #main window
    window = tk.Tk()
    window.config(bg = "GRAY")
    window.geometry("1400x800")
    window.title("elevator simulator")

    #title
    frame_title = tk.Frame(window, width = 1200, bg = "WHITE")

    title_label = tk.Label(frame_title, bg="WHITE", fg = "BLACK", font=("Arial", 32), text = "elevator simulator")

    title_label.pack()

    #floor buttons
    canvas1 = tk.Canvas(window,bg = "WHITE", width= 150, height=600)

    b1u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(1,1))
    b1d = tk.Button(window, highlightbackground="WHITE",text = "\u25BC", command = lambda: press_button(1,2))
    b2u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(2,1))
    b2d = tk.Button(window, highlightbackground="WHITE",text = "\u25BC", command = lambda: press_button(2,2))
    b3u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(3,1))
    b3d = tk.Button(window, highlightbackground="WHITE",text = "\u25BC", command = lambda: press_button(3,2))
    b4u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(4,1))
    b4d = tk.Button(window, highlightbackground="WHITE",text = "\u25BC", command = lambda: press_button(4,2))
    b5u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(5,1))
    b5d = tk.Button(window, highlightbackground="WHITE",text = "\u25BC", command = lambda: press_button(5,2))
    b6u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(6,1))
    b6d = tk.Button(window, highlightbackground="WHITE",text = "\u25BC", command = lambda: press_button(6,2))
    b7u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(7,1))
    b7d = tk.Button(window, highlightbackground="WHITE",text = "\u25BC", command = lambda: press_button(7,2))
    b8u = tk.Button(window, highlightbackground="WHITE",text = "\u25B2", command = lambda: press_button(8,1))
    b8d = tk.Button(window,highlightbackground="WHITE", text = "\u25BC", command = lambda: press_button(8,2))
    label_1st = tk.Label(window, padx = 7, pady = 17, text = "1", anchor=tk.W)
    label_2st = tk.Label(window, padx = 6, pady = 17, text = "2", anchor=tk.W)
    label_3st = tk.Label(window, padx = 5, pady = 17, text = "3", anchor=tk.W)
    label_4st = tk.Label(window, padx = 5, pady = 17, text = "4", anchor=tk.W)
    label_5st = tk.Label(window, padx = 6, pady = 17, text = "5", anchor=tk.W)
    label_6st = tk.Label(window, padx = 5, pady = 17, text = "6", anchor=tk.W)
    label_7st = tk.Label(window, padx = 6, pady = 17, text = "7", anchor=tk.W)
    label_8st = tk.Label(window, padx = 5, pady = 17, text = "8", anchor=tk.W)
    
    global b_u, b_d
    b_u = [b1u,b2u,b3u,b4u,b5u,b6u,b7u,b8u]
    b_d = [b1d,b2d,b3d,b4d,b5d,b6d,b7d,b8d]


    canvas1.create_window(73,518, anchor=tk.W, window=b1u)
    canvas1.create_window(73,544, anchor=tk.W, window=b1d)
    canvas1.create_window(50,531, anchor=tk.W, window=label_1st)
    canvas1.create_window(73,448, anchor=tk.W, window=b2u)
    canvas1.create_window(73,474, anchor=tk.W, window=b2d)
    canvas1.create_window(50,461, anchor=tk.W, window=label_2st)
    canvas1.create_window(73,378, anchor=tk.W, window=b3u)
    canvas1.create_window(73,404, anchor=tk.W, window=b3d)
    canvas1.create_window(50,391, anchor=tk.W, window=label_3st)
    canvas1.create_window(73,308, anchor=tk.W, window=b4u)
    canvas1.create_window(73,334, anchor=tk.W, window=b4d)
    canvas1.create_window(50,321, anchor=tk.W, window=label_4st)
    canvas1.create_window(73,238, anchor=tk.W, window=b5u)
    canvas1.create_window(73,264, anchor=tk.W, window=b5d)
    canvas1.create_window(50,251, anchor=tk.W, window=label_5st)
    canvas1.create_window(73,168, anchor=tk.W, window=b6u)
    canvas1.create_window(73,194, anchor=tk.W, window=b6d)
    canvas1.create_window(50,181, anchor=tk.W, window=label_6st)
    canvas1.create_window(73,98, anchor=tk.W, window=b7u)
    canvas1.create_window(73,124, anchor=tk.W, window=b7d)
    canvas1.create_window(50,111, anchor=tk.W, window=label_7st)
    canvas1.create_window(73,28, anchor=tk.W, window=b8u)
    canvas1.create_window(73,54, anchor=tk.W, window=b8d)
    canvas1.create_window(50,41, anchor=tk.W, window=label_8st)

    #elevator
    global canvas2, b1, b2, b3, b4, b5, b6, b7, b8,bof
    canvas2 = tk.Canvas(window,bg = "WHITE", width= 500, height=600)

    b1 = tk.Button(window, pady= 15, highlightbackground="WHITE",padx = 10, text = "1", command = lambda: press_button(1,0))
    b2 = tk.Button(window, pady = 15, highlightbackground="WHITE",padx = 10,text = "2", command = lambda: press_button(2,0))
    b3 = tk.Button(window, pady = 15, highlightbackground="WHITE",padx = 10, text = "3", command = lambda: press_button(3,0))
    b4 = tk.Button(window, pady = 15, highlightbackground="WHITE",padx = 10, text = "4", command = lambda: press_button(4,0))
    b5 = tk.Button(window, pady = 15, highlightbackground="WHITE",padx =10, text = "5", command = lambda: press_button(5,0))
    b6 = tk.Button(window, pady = 15, highlightbackground="WHITE",padx =10, text = "6", command = lambda: press_button(6,0))
    b7 = tk.Button(window, pady = 15, highlightbackground="WHITE",padx =10, text = "7", command = lambda: press_button(7,0))
    b8 = tk.Button(window, pady = 15, highlightbackground="WHITE",padx =10, text = "8", command = lambda: press_button(8,0))
    bo = tk.Button(window, pady = 15, highlightbackground="WHITE",padx =5, text = "<>")
    bc = tk.Button(window, pady = 15, highlightbackground="WHITE",padx =5, text = "><")
    bof = tk.Button(window, pady = 15, highlightbackground="RED",padx =5, text = "power", command = onof)
    label_1 = tk.Label(window, width= 30, padx = 65, pady = 5, text = "Power off ...", anchor=tk.W)
    label_floor = tk.Label(window, padx = 10, pady = 10,  font=("Arial", 32), text = "1", anchor=tk.W)

    canvas2.create_window(430,490, anchor=tk.W, window=b1)
    canvas2.create_window(350,490, anchor=tk.W, window=b2)
    canvas2.create_window(430,420, anchor=tk.W, window=b3)
    canvas2.create_window(350,420, anchor=tk.W, window=b4)
    canvas2.create_window(430,350, anchor=tk.W, window=b5)
    canvas2.create_window(350,350, anchor=tk.W, window=b6)
    canvas2.create_window(430,280, anchor=tk.W, window=b7)
    canvas2.create_window(350,280, anchor=tk.W, window=b8)
    canvas2.create_window(430,560, anchor=tk.W, window=bo)
    canvas2.create_window(350,560, anchor=tk.W, window=bc)
    canvas2.create_window(20,560,anchor=tk.W, window=bof)
    canvas2.create_window(50,50, anchor=tk.NW, window=label_1)
    canvas2.create_window(50,120, anchor=tk.NW, window=label_floor)
    global b_l
    b_l = [b1,b2,b3,b4,b5,b6,b7,b8]

    #FSM
    global state_idel_c, state_md_c, state_mu_c,canvas3
    global state_u_stop_c,state_u_open_c,state_u_close_c,state_d_stop_c,state_d_open_c,state_d_close_c

    canvas3 = tk.Canvas(window, bg ="WHITE", width=500, height=600)
   
    state_idel_c = canvas3.create_oval(200,20,300,80, outline = "black", fill = "Orange", width = 2)
    state_md_c = canvas3.create_oval(80,120,180,180, outline = "black", fill = "WHITE", width = 2)
    state_d_stop_c = canvas3.create_oval(80,320,180,380, outline = "black", fill = "WHITE", width = 2)
    state_d_open_c = canvas3.create_oval(80,420,180,480, outline = "black", fill = "WHITE", width = 2)
    state_d_close_c = canvas3.create_oval(80,520,180,580, outline = "black", fill = "WHITE", width = 2)
    state_mu_c = canvas3.create_oval(320,120,420,180, outline = "black", fill = "WHITE", width = 2)
    state_u_stop_c = canvas3.create_oval(320,320,420,380, outline = "black", fill = "WHITE", width = 2)
    state_u_open_c = canvas3.create_oval(320,420,420,480, outline = "black", fill = "WHITE", width = 2)
    state_u_close_c = canvas3.create_oval(320,520,420,580, outline = "black", fill = "WHITE", width = 2)

    label_idle = tk.Label(window, text = "Idle", fg= "black", bg = "WHITE", anchor=tk.W)
    label_md = tk.Label(window, text = "Move Down", fg = "black",bg = "WHITE", anchor=tk.W)
    label_mu = tk.Label(window, text = "Move Up", fg="black", bg = "WHITE", anchor=tk.W)
    label_d_stop = tk.Label(window, text = "Stop", fg = "black",bg = "WHITE", anchor=tk.W)
    label_d_open = tk.Label(window, text = "Open Door", fg="black", bg = "WHITE", anchor=tk.W)
    label_d_close = tk.Label(window, text = "Close Door", fg= "black", bg = "WHITE", anchor=tk.W)
    label_u_stop = tk.Label(window, text = "Stop", fg="black", bg = "WHITE", anchor=tk.W)
    label_u_open = tk.Label(window, text = "Open Door", fg= "black", bg = "WHITE", anchor=tk.W)
    label_u_close = tk.Label(window, text = "Close Door", fg = "black",bg = "WHITE", anchor=tk.W)

    canvas3.create_window(240,40, anchor=tk.NW, window=label_idle)
    canvas3.create_window(95,140, anchor=tk.NW, window=label_md)
    canvas3.create_window(340,140, anchor=tk.NW, window=label_mu)
    canvas3.create_window(95,340, anchor=tk.NW, window=label_d_stop)
    canvas3.create_window(95,440, anchor=tk.NW, window=label_d_open)
    canvas3.create_window(95,540, anchor=tk.NW, window=label_d_close)
    canvas3.create_window(340,340, anchor=tk.NW, window=label_u_stop)
    canvas3.create_window(340,440, anchor=tk.NW, window=label_u_open)
    canvas3.create_window(340,540, anchor=tk.NW, window=label_u_close)


    # organize and pack
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
