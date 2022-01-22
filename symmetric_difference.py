
M = int(input())
mset = set(map(int,input().split()))


N = int(input())
nset = set(map(int,input().split()))

lst=list(mset.union(nset) - mset.intersection(nset)) 
lst.sort()

for i in lst :
  print(i,end='\n')
