print("Choose a Vehicle")
print("-----------------")
vehicle = int(input(" choose a vheicle\n1.Car\n2.bike\n1 or 2:"))
if vehicle == 1:
    type = int(input("choose a car type\n1.electirc\n2.petrol\nenter your choice"))
    if type == 1:
        print("you have chosen an electirc car\n it is fast and eco friendly")
    elif type == 2:
        print("you have chosen a petorl car\n it is relible and cheap")
elif vehicle == 2:
    type = int(input("choose a bike type\n1.mountian bike\n2.manual bike\nenter you chioice:"))
    if type == 1:
        print("you have chosen a mountin bike\n it is good for rough roads and trails")
    elif type == 2: 
        print("you have chosen a manual bike\n it is good for everyday life and esay to maintain")
    else:
        print("invalid chioice choose \n 1.car or \n 2.bike")
