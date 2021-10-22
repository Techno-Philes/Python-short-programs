n= int(input(Enter the number))
try:
  if(n<0):
    raise ValueError("Number should not be negative")
  elif(n<=20):
    raise ValueError("Number should be above 20")
  else:
    res = 1
    while(n>0):
      res = resn
      n = n-1
    print(res)

except Exception as e:
  print(e)