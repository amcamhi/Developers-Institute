# def display_message():
#     print("We are learning python functions")

# display_message()

# # Excercise 2
# def favorite_book(title):
#   print("one of my favorite books is: "+title)

# favorite_book("1Q84")

#Excercise 3
# def make_shirt(size = "L", text="I love python"):
#   print("the size is: "+str(size)+", the message is: "+text)
  
# make_shirt("XL", "All you need is love")
# make_shirt(text="All you need is love", size = "XL")
# make_shirt()

# make_shirt("L")
# make_shirt("M")
# make_shirt(text="Hello")

# # Excercise 4

# magicians = ["Gandalf", "Merlin", "Harry Potter", "David Copperfield"]

# def show_magicians():
#     for magician in magicians:
#         print(magician)
# def make_great():
#     for i in range(len(magicians)):
#         magicians[i]+=" the Great"

# make_great()
# show_magicians()

# Excercise 5
# def describe_city(city, country="somewhere"):
#   print(f"{city} is in {country}")

# describe_city("Santiago", "Chile")
# describe_city("Tel Aviv", "Israel")
# describe_city("Lima", "Peru")
# describe_city("Zen Dong")

# Excercise 6
from datetime import date 
  
def get_age(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) <  (birthDate.month, birthDate.day)) 
  
    return age 

print(get_age(date(1991, 12, 6)), "years") 


def can_retire(gender, age):
   if gender == "female" and age>62:
     return True
   elif gender == "male" and age >67:
     return True
   else:
     return False

print(can_retire("male",68))