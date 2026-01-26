A = [3, 2, 1]
B = []
C = []
count = 0

def towers_of_hanoi(A,B,C,n):

  a = {
    'A': A,
    'B': B,
    'C': C,
    'n': n
  }

  print(a)

  global count
  if n == 1:
    disk = A.pop()
    C.append(disk)
    count +=1
  else:
    towers_of_hanoi(A,C,B,n-1) # 2x
    towers_of_hanoi(A,B,C,1)
    towers_of_hanoi(B,A,C,n-1)

  print({ 'count': count })
  return count

print(towers_of_hanoi(A,B,C,len(A)))
