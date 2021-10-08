
print("Here you can check if any phrase you input can be composed out of the other one, by writting down two.")

# while True:
   
#  input1 = (input('Input your first phrase: ').upper())
#  input2 = (input('Input your second phrase: ').upper())

#  phrase1 = set()
#  phrase2 = set()

#  for element in input1: 
#     if element.isalpha():
#         phrase1.add(element)


#  for element in input2: 
#      if element.isalpha():
#         phrase2.add(element)

#  print('Letters from the first phrase: ', phrase1)
#  print('Letters from the second phrase: ', phrase2)

 



#  if phrase1.issuperset(phrase2):
#         print("Using this two you can form one from another")
#  else:
#         print("Using this two you cannot form one from another")


#  answer= input('Do you want to do that again? If you do, type Yes, and if not, type No:  ')
#  if answer == "Yes":
#         continue
#  elif answer== "No":
#         break

# print('Goodbye')


# while True:
#     phr1 = []
#     phr2 = []
#     x = str(input("Enter the first phrase: "))
#     alpha1 = "".join(p for p in x if p.isalpha())
#     #print(alpha1)
#     p1l = list(alpha1.lower())
#     p1u = list(alpha1.upper())
#     phr1 = p1l + p1u
#     uni1 = set(phr1)
#     #print(uni1)
#     y = str(input("Enter the second phrase: "))
#     alpha2 = "".join(t for t in y if t.isalpha())
#     p2l = list(alpha2.lower())
#     p2u = list(alpha2.upper())
#     phr2 = p2l + p2u
#     uni2 = set(phr2)
#     #print(uni2)
#     inter = len(uni2-uni1)
#     if inter == 0:
#         print('+++')
#     else:
#         print('---')