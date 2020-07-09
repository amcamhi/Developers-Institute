string = input("write a sentence: ")
char = input("which character would you like to count?")
def count_char(string, char):
  count = string.count(char)
  print(string)
  print(char)
  return count
print(count_char(string,char))
