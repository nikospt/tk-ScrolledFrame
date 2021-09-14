import tkinter as tk
class ScrolledFrame():
    def __init__( self, parent, root, axis='y', *args, **kwargs):
        self.container = tk.Frame(parent)
        self.canvas = tk.Canvas( self.container, *args, **kwargs )
        self.content = tk.Frame(self.canvas)
        if axis == 'y' or axis == 'xy' or axis == 'yx' or axis == 'both':
            self.yscrollbar = tk.Scrollbar( self.container, orient='vertical', command=self.canvas.yview)
        if axis == 'x' or axis == 'xy' or axis == 'yx' or axis == 'both':
            self.xscrollbar = tk.Scrollbar( self.container, orient='horizontal', command=self.canvas.xview)
        self.root = root
        self.canvas.create_window( (0,0), window=self.content, anchor='nw')
        self.BindMouseWheel(self.content)
        self.BindMouseWheel(self.canvas)
        self.BindMouseWheel(self.container)

    def updateContent(self):
        self.content.update()
        self.bindChildren(self.content)
        self.canvas.configure(yscrollcommand=self.yscrollbar.set, scrollregion="0 0 0 %s" % self.content.winfo_height() )
        print('check what scrollregion is')
        self.canvas.configure(xscrollcommand=self.xscrollbar.set, scrollregion="0 0 %s 0" % self.content.winfo_width() )
        self.yscrollbar.pack(side='right', fill='y')
        self.xscrollbar.pack(side='bottom', fill='x')
        self.canvas.pack(side='left')


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