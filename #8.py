h=int(input("How tall are you in feet? Round down to the nearest foot: "))
i=int(input("And how many inches over that are you?"))
hcm = h * 30.48
icm = i *2.54
cm = hcm + icm
print("Your height is",cm,"cm")
