#Importa libreria
import math

def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

#Datos:
arr1 = [3,9,2,4]

#Imprime:
print("LCM of arr1 elements:", LCMofArray(arr1))
