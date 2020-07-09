# Excercise 1 
import random

def get_random_temp():
  n = random.randint(-10,40)
  return n

def main():
  temperature = get_random_temp()
  print(f'the temperature right now is: {temperature} degrees Celsius')
  if temperature<0:
    print("Brr, that´s freezing! Wear some extra layers today")
  elif 0<=temperature<16:
    print("Quite chilly! Don’t forget your coat”")
  elif 16<=temperature<23:
    print("Nice weather right?")
  else:
    print("it´s super hot today, you should go to the beach!")
main()
