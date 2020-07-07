# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You
input1 = input("write a sentence: ")
output1 = []
print(input1)

input1 = list(input1.split(" "))

length = len(input1)


for i in range(length-1,-1,-1):
  output1.append(input1[i])
 
print(" ".join(output1))