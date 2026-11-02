a1 = int(input("P1 enter a number " ))
a2 = int(input("P1 enter another number " ))
c1 = int(input("P2 enter a number " ))
c2 = int(input("P2 enter another number " ))
p1 = a1 / a2
p2 = c1 / c2
if p1 > p2:
    print("P1 wins!")
elif p1 < p2:
    print("P2 wins!")
elif p1 == p2:
    print("It's a tie time to go again!")
    a1 = int(input("P1 enter a number " ))
    a2 = int(input("P1 enter another number " ))
    c1 = int(input("P2 enter a number " ))
    c2 = int(input("P2 enter another number " ))
else:
    print("Error: 404 not found go again")
    a1 = int(input("P1 enter a number " ))
    a2 = int(input("P1 enter another number " ))
    c1 = int(input("P2 enter a number " ))
    c2 = int(input("P2 enter another number " ))

