from functools import reduce

numbers=[]
for i in range(2):
  numbers.append(int(input()))
  
for op in ['+','-','*']:
  output=reduce(lambda x,y : eval('x'+ op +'y') ,numbers)
  print(output)  
