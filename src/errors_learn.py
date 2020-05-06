class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    print('This method is a work-in-progress.')


ford_garage = Garage()
#ford_garage.cars.append("Ford fiesta")
#ford_garage.cars.append("Ford Figo")
ford_garage.add_car("Ford Figo")
print(ford_garage.cars)
