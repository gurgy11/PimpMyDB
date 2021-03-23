class Form():
    
    def __init__(self, name, fields=None):
        self.name = name
        self.fields = fields
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_fields(self):
        return self.fields
    
    def set_fields(self, fields):
        self.fields = fields