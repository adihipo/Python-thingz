numbers = [2, 3, 6, 9]
miscList = ["kutya", -5]

if 5 not in (numbers, miscList) and 5 is 5:
  print("OK")

if 5 not in (numbers, miscList) and 5 is not 5 or True is True:
  print("OK")