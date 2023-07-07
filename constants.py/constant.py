def create_btn(self, mode): 
        cmd = lambda: self.list.config(selectmode=mode) 
        return tk.Button(self, command=cmd, 
                         text=mode.capitalize()) 