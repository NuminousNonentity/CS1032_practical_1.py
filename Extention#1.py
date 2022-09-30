coins = [2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
Change=int(input("Enter the total amount of pennies you have: "))
change=Change
total=""
i=0
while i < len(coins):
  if change - coins[i] < 0:
    i+=1 
  else:
    change=change-coins[i]
    if coins[i] == coins[0]:
      total = total+" £20"
    elif coins[i] == coins[1]:
      total = total+" £10"
    elif coins[i] == coins[2]:
      total = total+" £5"
    elif coins[i] == coins[3]:
      total = total+" £2"
    elif coins[i] == coins[4]:
      total = total+" £1"
    elif coins[i] == coins[5]:
      total = total+" 50p"
    elif coins[i] == coins[6]:
      total = total+" 20p"
    elif coins[i] == coins[7]:
      total = total+" 10p"
    elif coins[i] == coins[8]:
      total = total+" 5p"
    elif coins[i] == coins[9]:
      total = total+" 2p"
    elif coins[i] == coins[10]:
      total = total+" 1p"
    if change > 0:
      pass
    else:
      break    

print("you have",total)
