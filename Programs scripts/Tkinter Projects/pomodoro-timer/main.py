from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.30
LONG_BREAK_MIN = 0.50
reps= 0
my_timmer = None

# ---------------------------- TIMER RESET ------------------------------- #

def timer_rest ():
    window.after_cancel(my_timmer)
    my_canvas.itemconfig(timmer,text="00:00")
    check_label.config(fg=GREEN,bg=YELLOW)
    timmer_label.config(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timmer_button_Start ():
    global  reps
    reps += 1

    work_sec = WORK_MIN*60
    SHORT_BREAK_sec=SHORT_BREAK_MIN*60
    LONG_BREAK_sec=LONG_BREAK_MIN*60


    if  reps % 8 == 0 :
        timmer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_sec)
    elif reps % 2 == 0 :
        timmer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_sec)
    else:
       timmer_label.config(text="Work", fg=GREEN)
       count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global my_timmer
    count_minute= math.floor(count/60)
    count_second= count % 60
    if count_second < 10:
        count_second =f"0{count_second}"
    my_canvas.itemconfig(timmer,text=f"{count_minute}:{count_second}")
    if count > 0 :
        my_timmer = window.after(1000,count_down,count-1)
    else:
        timmer_button_Start()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range (work_sessions):
            marks += "✔"
        check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO TECHNIQUE APP")
window.config(padx=150,pady=75,bg=YELLOW)


my_canvas = Canvas(width= 200,height=223,bg=YELLOW,highlightthickness=0)
img_path = PhotoImage(file="tomato.png")
my_canvas.create_image(100,110,image=img_path)
timmer = my_canvas.create_text(100,130,text="00:00",font =(FONT_NAME,35,"bold"),fill="white")
my_canvas.grid(column=1,row=1)


timmer_label= Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
timmer_label.grid(column=1,row=0)

check_label = Label(fg=GREEN,bg=YELLOW)
check_label.grid(column=1,row=3)

start_button= Button(text="Start",highlightthickness=0,command=timmer_button_Start)
start_button.grid(column=0,row=2)

rest_button= Button(text="Reset",highlightthickness=0,command = timer_rest)
rest_button.grid(column=2,row=2)



window.mainloop()