ttime = int(input("Enter a number of seconds: "))
seconds = 1
minutes = 60
hours = 60*60
days = 60*60*24

d = 0
h = 0
m= 0
s = 0

time =[days, hours, minutes, seconds]
i=0
while i < len(time):
  if ttime - time[i] < 0:
    i+=1
  else:
    ttime = ttime - time[i]
    if time[i] == time[0]:
      d+=1
    elif time[i] == time[1]:
      h+=1
    elif time[i] == time[2]:
      m+=1
    elif time[i] == time[3]:
      s=+1
    if ttime > 0:
      pass
    else:
      break 


print("%02d" % d+":"+"%02d" % h+":"+ "%02d" % m+":"+ "%02d" % s) 
#credit to Sarvesh Chitko for the two digit display on stack overflow https://stackoverflow.com/questions/3505831/in-python-how-do-i-convert-a-single-digit-number-into-a-double-digits-string
