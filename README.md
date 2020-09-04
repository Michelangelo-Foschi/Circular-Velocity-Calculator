# Circular-Velocity-Calculator
Wouldn't it be cool to get the Circular Velocity of an orbit, with your input and the script's output?

# Importing Packages
We just need to import the math package to use the square root function.

``` python
import math
```
**math allows us to use different mathematical operations.**

``` python
planet = input("What planet will your sat be orbiting? Available: Mercury, Venus, Earth and Mars -> ")
altitude = input("What's the height of your sat over the surface? In KM:  ") 
converted_altitude = float(altitude)
```
**Let's get some user inputs so that we can insert these values in our formula.**

``` python
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
   ```

**We created a function for all 4 planets (Mercury, Venus, Earth and Mars) and we inserted their radius and mass in their proper array.
The array also consists of Newton's Universal Gravitational Constant.
We also add up the planet's radius with the altitude of the satellite, so that we get the total distance between M1 and M2.**
