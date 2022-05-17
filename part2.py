"""
******
PART 2
******
Define a function celsius that takes a single float parameter, the temperature in fahrenheit. The function RETURNS (not print) the celsius reading of the temperature

The formula for converting from fahrenheit to celsius:
C = (F - 32) * 5/9
"""

def celsius(f):
  f = float(f)# do not change this line
  f = (f-32)*5/9  # delete the word pass when you start writing your code
  return f