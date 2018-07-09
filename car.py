from vehicle import Vehicle

class Car(Vehicle):

  def __init__(self, price, ab_count, material="cloth"):
    self.price = price
    self.seat_material = material
    self.airbag_count = ab_count
    super().__init__("car")

  def calc_payments(self, months, rate):
    return f'Your payments for a purchase price of ${self.price} over {months} at {rate} would be too high. Buy something cheaper.'



