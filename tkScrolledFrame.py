import tkinter as tk

class ScrolledFrame():
    def __init__( self, parent, axis='y', *args, **kwargs):
        self.container = tk.Frame(parent)
        self.canvas = tk.Canvas( self.container, *args, **kwargs )
        self.content = tk.Frame(self.canvas)
        self.parent = parent
        self.xscrollbar = None
        self.yscrollbar = None
        if axis == 'y' or axis == 'xy' or axis == 'yx' or axis == 'both':
            self.yscrollbar = tk.Scrollbar( self.container, orient='vertical', command=self.canvas.yview)
        if axis == 'x' or axis == 'xy' or axis == 'yx' or axis == 'both':
            self.xscrollbar = tk.Scrollbar( self.container, orient='horizontal', command=self.canvas.xview)
        self.root = parent.winfo_toplevel()
        self.canvas.create_window( (0,0), window=self.content, anchor='nw')
        if self.yscrollbar != None:
            # Dont bind scroll wheel unless y is an axis of this scrollframe
            self.BindMouseWheel(self.content)
            self.BindMouseWheel(self.canvas)
            self.BindMouseWheel(self.container)
        self.content.bind("<Map>",self.BindMap)
        self.root.bind("<Configure>", self.resize)

    def BindMap(self,event):
        # No Longer need to call update content.
        # This bind will do it automatically
        self.content.update()

        if self.yscrollbar != None:
            # Dont bind scroll wheel unless y is an axis of this scrollframe
            self.bindChildren( self.content)

        if self.yscrollbar != None:
            self.yscrollbar.pack( side='right',  fill='y' )
            # self.canvas.configure( yscrollcommand=self.yscrollbar.set, scrollregion="0 0 0 %s" % self.content.winfo_height() )
            self.canvas.configure( yscrollcommand=self.yscrollbar.set, scrollregion=self.canvas.bbox("all") )

        if self.xscrollbar != None:
            # self.canvas.configure( xscrollcommand=self.xscrollbar.set, scrollregion="0 0 %s 0" % self.content.winfo_width() ) 
            self.canvas.configure( xscrollcommand=self.xscrollbar.set, scrollregion=self.canvas.bbox("all") ) 
            self.xscrollbar.pack( side='bottom', fill='x' )
        
        self.canvas.pack( side='top', fill='both' )

    def updateContent(self):
        self.content.update()
        if self.yscrollbar != None:
            # Dont bind scroll wheel unless y is an axis of this scrollframe
            self.bindChildren( self.content)

        if self.yscrollbar != None:
            self.yscrollbar.pack( side='right',  fill='y' )
            # self.canvas.configure( yscrollcommand=self.yscrollbar.set, scrollregion="0 0 0 %s" % self.content.winfo_height() )
            self.canvas.configure( yscrollcommand=self.yscrollbar.set, scrollregion=self.canvas.bbox("all") )

        if self.xscrollbar != None:
            # self.canvas.configure( xscrollcommand=self.xscrollbar.set, scrollregion="0 0 %s 0" % self.content.winfo_width() )
            self.canvas.configure( xscrollcommand=self.xscrollbar.set, scrollregion=self.canvas.bbox("all") )
            self.xscrollbar.pack( side='bottom', fill='x' )


        self.canvas.pack( side='top', fill='both' )

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

    def grid(self,*args, **kwargs):
        self.container.grid(*args,**kwargs)

    def pack(self,*args, **kwargs):
        self.container.pack(*args,**kwargs)

    def resize(self,*args):
        height = min( [self.content.winfo_height(), self.parent.winfo_height()-10 ] )
        self.canvas.configure(height=height )