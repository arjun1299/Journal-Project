from tkinter import filedialog
from tkinter import *

root=Tk()
#widgets in the window
timePeriodLabel=Label(root,text="Time interval between screen grabs")
timePeriodLabel.pack(side=LEFT)
timePeriod= Entry(root,bd= 5)
timePeriod.pack(side=RIGHT)

print(timePeriod.get())


B.place(x = 50,y = 50)
B = Button(root, text = "Hello", command = exit)


'''root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
print(folder_selected)'''

root.mainloop()