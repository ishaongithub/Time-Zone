from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.title("Time Zones")
root.geometry("600x450")
clock_image=ImageTk.PhotoImage(Image.open("clock.jpg"))

india_label=Label(root, text="India")
india_label.place(relx=0.1, rely=0.05, anchor=CENTER)

india_clock=Label(root)
india_clock["image"]=clock_image
india_clock.place(relx=0.1, rely=0.35, anchor=CENTER)

india_time=Label(root)
india_time.place(relx=0.1, rely=0.65, anchor=CENTER)


usa_label=Label(root, text="USA")
usa_label.place(relx=0.5, rely=0.05, anchor=CENTER)

usa_clock=Label(root)
usa_clock["image"]=clock_image
usa_clock.place(relx=0.5, rely=0.35, anchor=CENTER)

usa_time=Label(root)
usa_time.place(relx=0.5, rely=0.65, anchor=CENTER)

_label=Label(root, text="Switzerland")
_label.place(relx=0.9, rely=0.05, anchor=CENTER)

_clock=Label(root)
_clock["image"]=clock_image
_clock.place(relx=0.9, rely=0.35, anchor=CENTER)

_time=Label(root)
_time.place(relx=0.9, rely=0.65, anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]=current_time
        india_time.after(200, self.times)
        
        
class USA():
    def times(self):
        home=pytz.timezone("US/Pacific")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]=current_time
        usa_time.after(200, self.times)
        
class switz():
    def times(self):
        home=pytz.timezone("CET")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        _time["text"]=current_time
        _time.after(200, self.times)
        
obj_india=India()
obj_us=USA()
india_btn=Button(root, text="Show Time", command=obj_india.times)
india_btn.place(relx=0.1, rely=0.8, anchor=CENTER)
us_btn=Button(root, text="Show Time", command=obj_us.times)
us_btn.place(relx=0.5, rely=0.8, anchor=CENTER)
obj_switz=switz()
s_btn=Button(root, text="Show Time", command=obj_switz.times)
s_btn.place(relx=0.9, rely=0.8, anchor=CENTER)
root.mainloop()