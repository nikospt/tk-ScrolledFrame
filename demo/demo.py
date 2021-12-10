import tkinter as tk
import sys
sys.path.insert(1, '../')
from tkScrolledFrame import ScrolledFrame

root = tk.Tk()
root.geometry('300x175')
root.title('tk-ScrolledFrame Demo')

title = tk.Label( root, text="Boundary Layer Calculator" )
# title.grid(column=0, row=0, sticky='ew' , padx=5, pady=5 )
title.pack(side='top', fill='both')

scrolledFrame = ScrolledFrame(root, axis = 'xy')#, width=100, height=120)
label = []
for i in range(10):
    # When adding widgets to the scrolled frame class, make sure they are added to the content object
    label.append( tk.Label(scrolledFrame.content, text='Label {}'.format(i+1)) )
    label[i].grid(sticky='ew') # or label[i].pack()

# Make sure to update content and grid the container frame when finished adding widgets to the scrolledFrame
# scrolledFrame.updateContent() # This is no longer needed with a Map binding added to the class
# scrolledFrame.container.grid()
# scrolledFrame.container.pack(side='bottom',fill='both')
# Can now call pack on the scrolledFrame object instead of containter member, which is more natural
scrolledFrame.pack(side='bottom',fill='both')

root.mainloop()