# Below we have a list of code covered in a mathematical operators overview taught in class, very straight forward.

"""

print('Addition')
print(100 + 42)

print('Subtraction')
print(100 - 42)

print('Division')
print(100 / 42)
print(100 / 38)

print('Floor Division')
print(100 // 42)
print(100 // 38)

print('Multiplication')
print(100 * 42)

# Modulus below: Modulus will give you the remainder. 50
print('Modulus')
print(100 % 42)

print('Exponents')
print(100 ** 42)

Assignment operator demonstration below

total = 100
total = total + 10
total += 10
total -= 10
total *= 10
total /= 10
total //= 10
total **= 10
total %= 10

from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.4

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty)

from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))

import math
loss = -20.25
product_cost = 89.99

print(abs(loss))
print(math.floor(product_cost))
print(math.ceil(product_cost))
print(abs(math.floor(loss)))
print(math.floor(loss))
print(round(product_cost))
print(math.sqrt(product_cost))
print(math.pow(5,4)) # pow returns a float 
print(5 ** 4) # exponent operator returns integer

"""