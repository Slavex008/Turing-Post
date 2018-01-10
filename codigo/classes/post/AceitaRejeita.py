class Rejeita:
    id = "rejeita"
    def __eq__(self, other):
        if (other == None):
            return False
    
        if(self.id == other.id):
            return True
    
        return False
    
class Aceita:
    id = "aceita"
    def __eq__(self, other):
        if(other == None):
            return False
        
        if(self.id == other.id):
            return True
    
        return False