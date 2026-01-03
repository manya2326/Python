def sum_all(arr):
  sm = 0
  for i in range(len(arr)):
    sm = sm + arr[i]
  return sm 

arr = [1,4,6,74,6,8,4,3,6]
result = sum_all(arr)
print(result)
  