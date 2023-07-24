class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
       return self.capacity - len(self.passengers)

    def add_passanger(self, name):
      if not self.open_seats():
        return False
      else:
        self.passengers.append(name)
        return True


people = ['John', 'Martnalia', 'Dominique', 'Pablo']
f = Flight(3)

for person in people:
  if (f.add_passanger(person)):
    print(f"{person} was added to the flight")
  else:
    print(f"no available seats for {person}")
  
   
