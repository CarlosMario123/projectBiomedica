class ControllerView:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.view = None

    def run(self):
        self.view.mainloop()

    def change_view(self, new_view):
        if self.view is not None:
            print("sin vista")
            self.view.destroy()
        
        self.view = new_view
        
        self.view.mainloop()