Class Node:
    def __int__(self, data):
        self.data = data
        self.next = None       #initialize the next node to None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next        #set the next node to the new node

