try:
  f = open("demmoo.txt","xt")
except:
  print("A file exists with same name!")
else:
  f = open("demo.txt","wt")
  x = input("enter a number to write in the file from 1 - 10 : ")
  y = int(x)
  if y < 0 or y > 10:
    raise Exception("invalid input!")
  else:
    f.write(x)
  f.close()