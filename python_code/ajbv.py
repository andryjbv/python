# importing the module
import math

# function to calculate LCM
def lcmCalc(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

  data=[2,4,8,16,32,64,7]

  print(lcmCalc(data))
