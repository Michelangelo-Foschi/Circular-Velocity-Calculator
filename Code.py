import math
planet = input("What planet will your sat be orbiting? Available: Mercury, Venus, Earth and Mars -> ")
altitude = input("What's the height of your sat over the surface? In KM:  ") 
converted_altitude = float(altitude)

def mars():
    mars = [3396, 6.419 * (10 ** 23), 6.674 * (10 ** -11), altitude]
    totalRadius = mars[0] + converted_altitude
    result_mm = math.sqrt((mars[2] * mars[1]) / totalRadius * 1000)
    result_m = result_mm / 1000
    print("Your sat is orbiting mars with a circular velocity of",result_m,"m/s")
def venus():
    venus = [6051, 4.867 * (10 ** 24), 6.674 * (10 ** -11), altitude]
    totalRadius = venus[0] + converted_altitude
    result_mm = math.sqrt((venus[2] * venus[1]) / totalRadius * 1000)
    result_m = result_mm / 1000
    print("Your sat is orbiting venus with a circular velocity of",result_m,"m/s")
def mercury():
    mercury = [2439, 3.285 * (10 ** 23), 6.674 * (10 ** -11), altitude]
    totalRadius = mercury[0] + converted_altitude
    result_mm = math.sqrt((mercury[2] * mercury[1]) / totalRadius * 1000)
    result_m = result_mm / 1000
    print("Your sat is orbiting mercury with a circular velocity of",result_m,"m/s")
def earth():
    earth = [6371, 5.9736 * (10 ** 24), 6.674 * (10 ** -11), altitude]
    totalRadius = earth[0] + converted_altitude
    result_mm = math.sqrt((earth[2] * earth[1]) / totalRadius * 1000)
    result_m = result_mm / 1000
    print("Your sat is orbiting earth with a circular velocity of",result_m,"m/s")
def run_func():
    if planet == "Mars":
        mars()
    elif planet == "Venus":
        venus()  
    elif planet == "Mercury":
        mercury()
    elif planet == "Earth":
        earth()    
run_func()
