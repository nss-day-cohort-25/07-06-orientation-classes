from car import Car
from color_picker import ColorPicker

# Stuff to test our code
tesla = Car("90,000", 12)
tesla_colors = ColorPicker("red", interior="black", pinstripe="goldenrod")
color_scheme = tesla_colors.get_colors()
print("tesla colors scheme", color_scheme)
tesla.color_scheme = color_scheme
print("our colored car", tesla.color_scheme)
print(tesla.calc_payments(60, "7%"))
print("tesla vehicle type", tesla.v_type)
























