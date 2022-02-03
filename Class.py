class Cats:
    
    __age = None
    __name = None
    ___breed = None
    
    def __init__(self, age, name, breed):
        
        self.age = age
        self.name = name
        self.breed = breed
    
    def get_info(self):
        
        print("Вік кота у місяцях -", self.age, ", його звати -", self.name, ", порода -", self.breed)
        

class Abyssinian(Cats):
    
    __eyes = None
    
    def __init__(self, age, name, breed, eyes):
        super(Abyssinian, self).__init__(age, name, breed)
        self.eyes = eyes
    
    def get_info(self):
        super().get_info()
        print("колір очей -", self.eyes)


class Persian(Cats):
    
    __fur = None
    
    def __init__(self, age, name, breed, fur):
        super(Persian, self).__init__(age, name, breed)
        self.fur = fur
    
    def get_info(self):
        super().get_info()
        print("колір шерсті -", self.fur)


cat2 = Abyssinian(1,'marta','Abyssinian', 'green')
cat2.get_info()

cat1 = Persian(2, 'Nik', 'Persian', 'black')
cat1.get_info()
