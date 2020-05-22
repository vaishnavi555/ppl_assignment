class Dog:
	
	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispDog(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Dog("Dog",4,"bark")
obj.dispDog()  	 
 
class Cat:
    	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispCat(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Cat("cat",4,"meow")
obj.dispCat()  	 

class Cow:
	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispCow(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Cow("Cow",4,"moo")
obj.dispCow()  	 

class Tiger:
    	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispTiger(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Tiger("Tiger",4,"roar")
obj.dispTiger()  	 

class Elephant:
	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispElephant(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Elephant("elephant",4,"trumpet")
obj.dispElephant()
  	 
class Hen:
    	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispHen(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Hen("Hen",2,"cluck")
obj.dispHen()  	 

class Camel:
    	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispCamel(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Camel("Camel",4,"grunt")
obj.dispCamel()  	 

class Bear:
    	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispBear(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Bear("Bear",2,"growl")
obj.dispBear()  	 


class Frog:
	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispFrog(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Frog("Frog",4,"croak")
obj.dispFrog() 

class Pig:
	def __init__(self, name, sound, legs): 
		# public data mambers  
		self.Name = name
		self.Sound = sound
		self.Legs = legs 
  
	       
	def dispPig(self): 
        	# accessing public data member 
        	print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))
			 
obj = Pig("Pig",4,"squeak")
obj.dispPig() 

class Circle:
	__name = None
	__area = None
	
	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayCircle(self): 
            
           # accessing private data members 
        	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessCircle(self):  
             
           	# accesing private member function 
           	self.__displayCircle()   
  
# creating object     
obj = Circle("Circle","pi * radius^2") 
  
# calling public member function of the class 
obj.accessCircle() 

class Square:
	name = None
	area = None
	
	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displaySquare(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessSquare(self):  
             
           # accesing private member function 
           	self.__displaySquare()   
  
# creating object     
obj = Square("Square","side^2") 
  
# calling public member function of the class 
obj.accessSquare() 

class Rectangle:
	name = None
	area = None

	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayRectangle(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessRectangle(self):  
             
           # accesing private member function 
           	self.__displayRectangle()   
  
# creating object     
obj = Rectangle("Rectangle","length * width") 
  
# calling public member function of the class 
obj.accessRectangle() 

class Triangle:
	name = None
	area = None

	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayTriangle(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessTriangle(self):  
             
           # accesing private member function 
           	self.__displayTriangle()   
  
# creating object     
obj = Triangle("Triangle","1/2 * base * height") 
  
# calling public member function of the class 
obj.accessTriangle() 

class Parallelogram:
	name = None
	area = None

	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayParallelogram(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessParallelogram(self):  
             
           # accesing private member function 
           	self.__displayParallelogram()   
  
# creating object     
obj = Parallelogram("Parallelogram","breadth * height") 
  
# calling public member function of the class 
obj.accessParallelogram() 

class Trapezium:
	name = None
	area = None

	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayTrapezium(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessTrapezium(self):  
             
           # accesing private member function 
           	self.__displayTrapezium()   
  
# creating object     
obj = Trapezium("Trapezium","1/2 * (side1 + side2) * height") 
  
# calling public member function of the class 
obj.accessTrapezium() 

class Ellipse:
	name = None
	area = None

	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayEllipse(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessEllipse(self):  
             
           # accesing private member function 
           	self.__displayEllipse()   
  
# creating object     
obj = Ellipse("Ellipse","pi * a * b") 
  
# calling public member function of the class 
obj.accessEllipse() 

class Cube:
	name = None
	area = None
	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayCube(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessCube(self):  
             
           # accesing private member function 
           	self.__displayCube()   
  
# creating object     
obj = Cube("Cube","6 * a^2") 
  
# calling public member function of the class 
obj.accessCube() 

class Sphere:
	name = None
	area = None

	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displaySphere(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessSphere(self):  
             
           # accesing private member function 
           	self.__displaySphere()   
  
# creating object     
obj = Sphere("Sphere","4 * pi * r^2") 
  
# calling public member function of the class 
obj.accessSphere() 

class Hemisphere:
	name = None
	area = None

	def __init__(self, name, area):   
        	self.__name = name 
        	self.__area = area 
         
  
     # private member function   
	def __displayHemisphere(self): 
            
           # accessing private data members 
           	print("Name: {} Area : {}".format(self.__name, self.__area))  
     
     # public member function 
     	def accessHemisphere(self):  
             
           # accesing private member function 
           	self.__displayHemisphere()   
  
# creating object     
obj = Hemisphere("Hemisphere","3 * pi * r^2") 
  
# calling public member function of the class 
obj.accessHemisphere() 








