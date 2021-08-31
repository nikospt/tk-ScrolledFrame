import tkinter as tk
class ScrolledFrame():
    def __init__(self,parent,root, *args, **kwargs):
        self.container = tk.Frame(parent)
        self.canvas = tk.Canvas( self.container, *args, **kwargs )
        self.content = tk.Frame(self.canvas)
        self.scrollbar = tk.Scrollbar( self.container, orient='vertical', command=self.canvas.yview)
        self.root = root
        self.canvas.create_window( (0,0), window=self.content, anchor='nw')
        self.BindMouseWheel(self.content)
        self.BindMouseWheel(self.canvas)
        self.BindMouseWheel(self.container)

    def updateContent(self):
        self.content.update()
        self.bindChildren(self.content)
        self.canvas.configure(yscrollcommand=self.scrollbar.set, scrollregion="0 0 0 %s" % self.content.winfo_height() )
        self.canvas.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')

    def BindMouseWheel(self,widget):
        if self.root.call('tk', 'windowingsystem') == 'x11':
            widget.bind('<Button-4>',self.scrolldown)
            widget.bind('<Button-5>',self.scrollup)
        else:
            widget.bind('<MouseWheel>',self.scrollMouseWheel)

    def scrollMouseWheel(self,event):
        self.canvas.yview_scroll(-1*event.delta, 'units')

    def scrolldown(self,event):
        self.canvas.yview_scroll(-4, 'units')

    def scrollup(self,event):
        self.canvas.yview_scroll(4, 'units')

    def bindChildren(self,widget):
        children = widget.winfo_children()
        if len(children) != 0:
            for child in enumerate(children):
                self.BindMouseWheel(child[1])
                self.bindChildren(child[1])