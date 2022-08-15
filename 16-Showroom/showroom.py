class Car:
  def __init__(self, identification, name, brand, price, active):
    self.identification = identification
    self.name = name
    self.brand = brand
    self.price = price
    self.active = active

class Node:
  def __init__(self, data):
    self.data = data
    self.nextNode = None 
    self.prevNode = None 

class LinkedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def clean(self):
    self.head = None
  
  def push(self,car):
    newNode = Node(car)
    #pokud neni zadny jiny Node
    if not self.head:
      self.head = newNode
      return
    else: #pridani node do seznamu, ktery uz nody obsahuje
      current = self.head
      #scenar, kdy je nova hodnota nizsi nez head
      if car.price < self.head.data.price:
        newNode.nextNode = current
        self.head = newNode
        current.prevNode = newNode
        return
      #scenar vsunuti mezi nody
      while current.nextNode != None: 
        if car.price < current.nextNode.data.price:
          newNode.nextNode = current.nextNode
          newNode.prevNode = current
          current.nextNode = newNode
          return 
        current = current.nextNode
      #pridani na posledni misto
      current.nextNode = newNode
      newNode.prevNode = current
      newNode.nexNode = None #nemuselo by byt, pisu pro svoji prehlednost

  def upgradeName(self,identification,name):
    current = self.head
    while current != None: 
        if current.data.identification == identification:
            current.data.name = name
            return
        current = current.nextNode
        
  def upgradeBrand(self,identification,brand):
    current = self.head
    while current != None: 
        if current.data.identification == identification:
            current.data.brand = brand
            return
        current = current.nextNode
  
  def activateDeactivate(self,identification, active):
    current = self.head
    while current != None: 
        if current.data.identification == identification:
            current.data.active = active
            return
        current = current.nextNode
        
  def getActiveSum(self):
    current = self.head
    priceForAll = 0
    while current != None: 
        if current.data.active == True:
            priceForAll += current.data.price
            
        current = current.nextNode
    return priceForAll
    
db = LinkedList()

def init(cars):
  for car in cars:
    db.push(car)

def add(car):
  db.push(car)

def clean(): #reseni pomoci smazani prvni reference
  db.clean()

def getDatabase():
  return db

def getDatabaseHead():
  return db.head
  
def updateName(identification, name):
    return db.upgradeName(identification,name)

def updateBrand(identification, brand):
    return db.upgradeBrand(identification,brand)

def activateCar(identification):
    return db.activateDeactivate(identification, True)
    
def deactivateCar(identification):
    return db.activateDeactivate(identification, False)
    
def calculateCarPrice():
    return db.getActiveSum()
    

if __name__ == '__main__':
  car1 = Car(1,"Octavia","Skoda",40,False)
  car2 = Car(2,"Fabia","Skoda",39,False)
  car3 = Car(3,"Octavia","Skoda",44,True)
  car4 = Car(4,"Fabia","Skoda",43,False)
  car5 = Car(5,"Clio","Renault",38,False)
  cars = [car1, car2, car3, car4, car5]
  init(cars)
  print(getDatabase())
  #clean()
  print(getDatabaseHead())
  #clean()
  updateName(1,'Enzo') 
  updateBrand(1,'Ferrari') 
  activateCar(1)
  activateCar(2)
  activateCar(4)
  deactivateCar(3)
  print(calculateCarPrice())
