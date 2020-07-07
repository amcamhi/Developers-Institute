birthday = "23/03/1993"
print(birthday)

i=0
for char in birthday:
  print(i, char)
  i+=1

birth_year = birthday[6:10]
print(birth_year)

years_old = 2020 - int(birth_year)
candles = str(years_old)[-1]
top = "___"+"i"*int(candles)+"___"
print("      "+top+"   ")
print('''  
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~ ''')