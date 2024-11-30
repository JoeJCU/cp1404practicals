"""
CP 1404 Practical 4, Joe David Mathew, silver service taxi test
"""
from silver_service_taxi import Silverservicetaxi

test_car = Silverservicetaxi("test_car", 100, 4)

# print(test_car)
test_car.start_fare()
test_car.drive(18)

print(f"The fare was {test_car.get_fare()}")
assert abs(test_car.get_fare() - 48.78) < 0.1, f"Assertion Failed!"
