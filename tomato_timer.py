#!/usr/bin/env python3

import time
from tkinter import ttk
from tkinter import Tk, StringVar, Entry, Label, Button
from tkinter import messagebox
from playsound import playsound

DEFAULT_MINS = 25

class TomatoTimer:

    def __init__(self, title = "Tomato Timer", frameSize="360x240"):
        self._root = Tk()
        self._style = ttk.Style()
        self._style.theme_use('alt')
        # Define the geometry of the window
        self._root.geometry(frameSize)

        #define title
        self._root.title(title)

        # set background color
        #self._root.config(bg='green')

        # declaration of variables
        self._hour=StringVar()
        self._minute=StringVar()
        self._second=StringVar()

        self.init_ui()
        self._started = False

    def set_time(self, hour=0, min=DEFAULT_MINS, sec=0):
        self._hour.set("{0:2d}".format(hour))
        self._minute.set("{0:2d}".format(min))
        self._second.set("{0:2d}".format(sec))

    def create_time_box(self, label):
        return Entry(self._root, width=4,font=("Arial",18,""), justify='center', textvariable=label)

    def init_ui(self):

        self.set_time()
        x_value = 90
        y_value = 80
        x_step = 60
        # Using Entry class to take input from the user
        hour_box = self.create_time_box(self._hour)
        hour_box.place(x=x_value, y=y_value)

        x_value += x_step
        mins_box = self.create_time_box(self._minute)
        mins_box.place(x=x_value,y=y_value)

        x_value += x_step
        sec_box = self.create_time_box(self._second)
        sec_box.place(x=x_value,y=y_value)

        #Create a Label
        label = Label(self._root, text= "Focus on righ now",font=('Helvetica bold', 20))
        #label.grid(column=0, row=0, padx=20, pady=20,  sticky='w')
        label.pack(pady=20)
        # button widget
        y_value += 40
        btnStart = Button(self._root, text='Start', bd='5', fg="green", command= self.countdown)
        btnStart.place(x = 80,y = y_value)

        btnStop = Button(self._root, text='Stop', bd='5', fg="blue", command= self.pause)
        btnStop.place(x = 140,y = y_value)

        btnReset = Button(self._root, text='Reset', bd='5', fg="red", command= self.reset)
        btnReset.place(x = 200,y = y_value)

    def stay_on_top(self):
        self._root.lift()
        self._root.after(2000, self.stay_on_top)

    def run(self):
        #Make the window jump above all
        self.stay_on_top()
        self._root.mainloop()


    def reset(self):
        self._started = False
        self.set_time()

    def pause(self):
        self._started = False

    def countdown(self):
        self._started = True
        try:
            # store the user input
            left_seconds = int(self._hour.get())*3600 + int(self._minute.get())*60 + int(self._second.get())
        except:
            messagebox.showwarning('', 'Invalid Input!')
        while self._started:
            
            # divmod(firstvalue = left_seconds//60, secondvalue = left_seconds%60)
            mins,secs = divmod(left_seconds,60)

            # Converting the input entered in mins or secs to hours,
            hours=0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            self.set_time(hours, mins, secs)

            # updating the GUI window
            self._root.update()
            time.sleep(1)

            if (left_seconds == 0):
                #messagebox.showinfo("Time Countdown", "Time Over")
                print("It is time")
                playsound('starlet.wav', block = False)
                break

            left_seconds -= 1


if __name__ == '__main__':
    timer = TomatoTimer()
    timer.run()

