
class Vehicle():

  def __init__(self, v_type="vehicle", color="red"):
    self.name = "Vehicle"
    self.v_type = v_type
    self.color = color
    self.is_transformed = False

  # definition of a vehicle
  def add_wheels(self, wheels_num):
    self.wheels = wheels_num

  def _add_rockets(self, num):
    self.rockets = num

  def transformerize(self, bot_name, rocket_num):
    self.wheels = 0
    self.is_transformed = True
    self._add_rockets(rocket_num)
    self.bot_name = bot_name

  def __str__(self):
    return f"This vehicle's name is {self.name}"


car = Vehicle("sedan", "blue")
# hovercraft = Vehicle()

car.add_wheels(4)
# hovercraft.add_wheels(0)
print("car's name", car.color)

car.transformerize("Dumbledoor", 5)
print("Transformed?", car.is_transformed, car.bot_name)


