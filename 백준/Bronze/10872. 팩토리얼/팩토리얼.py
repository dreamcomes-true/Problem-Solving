import sys
input = sys.stdin.readline
n = int(input())
res = 1
if n == 0:
  print(1)
else:
  for i in range(1, n+1):
    res *= i
  print(res)