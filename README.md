# tkScrolledFrame
A scrolled frame for Tkinter on python. <br>
tkScrolledFrame is a python class that supports vertical scrolling. The class acts similary to a tk Frame. Widgets can be added to the ScrolledFrame content frame with either grid or pack.  tkScrolledFrame supports mousewheel.

## Including the ScrolledFrame class in your script
Simply import tkScrolledFrame.py into your python script or copy the ScrolledFrame class into your script.
### Importing a Class from a File with Import
At the top of your script type
```
from tkScrolledFrame import ScrolledFrame
```
The import command does not require the .py extension to be added to import. If you place tk-ScrolledFrame in a different directory, then include that directory to the path first.
```
import sys
sys.path.insert(1, '/path/to/')
from tkScrolledFrame import ScrolledFrame
```

## Using Scrolled Frame
### Initializing
Initialize your scrolled frame with the ScrolledFrame class. The first two arguments are required. The first argument is the parent frame. The second argument is the root window. The root window is used to determine the windowing system and how to handle mousewheel events.
```
scrolledFrame = ScrolledFrame(parent, root)
```
Optional arguments are applied to the frame containing the scrolled frame. Here you can pass any argument you would pass to a tk Frame class. The ScrolledFrame's geometry can be defined.
```
scrolledFrame = ScrolledFrame(parent, root, width=100, height=100)
```
### Adding Widgets
To add widgets to the scrolled frame, simply create a widget with the ScrolledFrame's content object as the parent frame.
```
widgetInScrolledFrame = tk.Label( scrolledFrame.content, text='Label inside the scrolled frame')
widgetInScrolledFrame.grid() # or widgetInScrolledFrame.grid()
```
### Displaying the ScrolledFrame Widget
After all widgets have been added the scrolled frame, the scrolled frame needs to be updated and grided placed in the window.
```
scrolledFrame.updateContent()
scrolledFrame.container.grid() # or scrolledFrame.container.pack()
```
