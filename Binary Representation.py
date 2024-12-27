# Read a number from input and print its binary representation.

try:
  num = int(input("Input binary value: "), 2)
  print("num (decimal format):", num)
  print("num (binary format):", bin(num))  
except ValueError:
  print("Please input only binary value...")
