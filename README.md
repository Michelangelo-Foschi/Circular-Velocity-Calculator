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
