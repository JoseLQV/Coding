

# Object Oriented Programming:


# Class
class Dog: 
    
    # Constructor : Creation of the object with its attributes
    def __init__(self,Breed ,Color, Gender):
        self.Breed = Breed
        self.Color = Color
        self.Gender = Gender
        
    
        
    # Getters and Setters: 
    def set_Gender(self, Gender):
        self.Gender = Gender

    def set_Breed(self, Breed):
        self.Breed = Breed

    def set_Color(self, Color):
        self.Color = Color
    
    

    # Functions : Methods inside the Class
    def description(self):
        return [self.Breed, self.Gender, self.Color]
    
    
    

Pet = Dog("Rottweiler", "Black", "Male")
desc = Pet.description()

print (desc)
    

    
    
    