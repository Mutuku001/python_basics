print(" ---------------Basic calc--------------")

while True:
    function= int(input('''
    press 1 for addition
    press 2 for subtraction
    press 3 for  division
    press 4 for  multiplication
    press 0 to quit
    '''))
    if function==0:
      break
    if function>4:
      print("press 1 ,2 ,3, or 4 as per instructions")
      continue
    a= float (input("enter a number:"))
    b= float (input("enter another number:"))

    if function==1:
      print(a+b)
    elif function==2:
      print(a-b)
    elif function==3:
      print(a*b)
    elif function==4:
      print(a/b)
    else:
      print("I dont umderstand that")



