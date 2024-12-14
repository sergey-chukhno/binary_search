"""
Implementation of binary search algorithm

we will prove that binary search is faster than naive search!

naive search:   scan entire list and ask if its equal to the target 

if yes, return the index 
if no, return - 1
"""
import random, time

#We create the function for naive search 

def naive_search(list, target): 
  for i in range(len(list)): 
    if list[i] == target: 
      return i
  return -1
"""
binary search - let's divide and conquer 
we leverage the fact that the list is ordered

"""

def binary_search(list, target, low=None, high=None): 
  if low is None: 
    low = 0

  if high is None: 
    high = len(list)-1
  
  midpoint = (low + high)//2 
  
  if high < low: 
    return -1

  if list[midpoint] == target: 
    return midpoint
  
  elif target < list[midpoint]:
    return binary_search(list, target, low, high=midpoint-1)
  
  else: 
    target > list[midpoint]
    return binary_search(list, target, low=midpoint+1, high=high)
  
if __name__ == '__main__':
  list = [1, 3, 5, 10, 12]
  target = 10 
  print(naive_search(list, target)) 
  print(binary_search(list, target)) 

  length = 10000
  #build an unsorted list of length 10000

  sorted_list = set()
  while len(sorted_list) < length: 
    sorted_list.add(random.randint(-3*length, 3*length))
  
  sorted_list = sorted(sorted_list)

  starttime = time.time()
  for target in sorted_list:
    naive_search(sorted_list, target)
  endtime = time.time()

  print('Naive search time is : ', starttime - endtime, " seconds")

  starttime = time.time()
  for target in sorted_list:
    binary_search(sorted_list, target)
  endtime = time.time()

  print('Binary search time is : ', starttime - endtime, " seconds")
  