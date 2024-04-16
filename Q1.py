def is_sum_equal(L, total):
 # Initialize the running sum to 0
 running_sum = 0
 
 # Iterate through the list
for num in L:
running_sum += num
 
 # If the running sum equals the total, return True
 if running_sum == total:
 return True
 
  #if no match is found after a loop is completed it return False
return False
