import random
list = [1]
visited = [1]
certified = [1]
pointer = 1
counter = 0
prevCounter = 0
number = 4
addOn = 0
startLoop = 0
length = int(input("maze size "))
area = length**2
for i in range(area):
    list.append(i+1)
def up():
   global pointer
   global counter
   global addOn
   addOn = 0
   pointer = pointer - (length)
   counter = counter + 1
   visited.append(pointer)
   certified.append(pointer)
def down():
   global pointer
   global counter
   global addOn
   addOn = 0
   pointer = pointer + (length)
   counter = counter + 1
   visited.append(pointer)
   certified.append(pointer)
def left():
   global pointer
   global counter
   global addOn
   addOn = 0
   pointer = pointer - 1
   counter = counter + 1
   visited.append(pointer)
   certified.append(pointer)
def right():
   global pointer
   global counter
   global addOn
   addOn = 0
   pointer = pointer + 1
   counter = counter + 1
   visited.append(pointer)
   certified.append(pointer)
def traceback():
   global pointer
   certified.pop(-1)
   pointer = certified[-1]
while len(certified) != 1 or startLoop != 1:
   startLoop = 1
   if counter == prevCounter:
      if number == 1 and ((pointer + 1)not in visited):
         if pointer%length != 0:
            right()
            number = 2
         else:
            number = 2
            addOn = addOn + 1
      elif number == 2 and ((pointer -1)not in visited):
         if pointer%length != 1:
            left()
            number = 3
         else:
            number = 3
            addOn = addOn + 1
      elif number == 3 and ((pointer - length)not in visited):
         if  pointer - length > 0:
            up()
            number = 4
         else:
            number = 4
            addOn = addOn + 1
      elif number == 4 and ((pointer + length)not in visited):
         if pointer + length < area + 1:
            down()
            number = 1
         else:
            number = 1
            addOn = addOn + 1
      else:
         addOn = addOn + 1
         number = number + 1
         if number > 4:
            number = number - 4
         if addOn > 5:
            addOn = 0
            traceback()
   else:
      number = random.randint(1,4)
      prevCounter = counter

print(visited)