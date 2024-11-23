"""Taxi Test"""


from taxi import Taxi

new_taxi = Taxi(name = "Prius 1", fuel=100, price_per_km=1.23) #new object

new_taxi.drive(40)  #drive function in taxi.py

print(new_taxi)
print(new_taxi.get_fare())

new_taxi.start_fare()


