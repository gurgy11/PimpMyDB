class Field():
    
    def __init__(self, name, data_type, value=None, min_length=None, max_length=None):
        self.name = name
        self.data_type = data_type
        self.value = value
        self.min_length = min_length
        self.max_length = max_length
        
    ''' Getters and Setters '''
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_data_type(self):
        return self.data_type
    
    def set_data_type(self, data_type):
        self.data_type = data_type
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
    def get_min_length(self):
        return self.min_length
    
    def set_min_length(self, min_length):
        self.min_length = min_length
        
    def get_max_length(self):
        return self.max_length
    
    def set_max_length(self, max_length):
        self.max_length = max_length
    
    ''' Helper Methods '''
    
    def min_length_is_valid(self):
        if len(self.value) < self.min_length:
            return False
        else:
            return True
        
    def max_length_is_valid(self):
        if len(self.value) > self.max_length:
            return False
        else:
            return True
        
    def value_is_empty(self):
        if self.value is None or self.value == '':
            return True
        else:
            return False
