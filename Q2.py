def is_palindrome(numbers_list):
    # Initialize pointers for the start and end of the list
    start = 0
    end = len(numbers_list) - 1
    
    # continue to iterate till the start pointer passes the end pointer
    while start < end:
        # If the elements at the current positions don't match, return False
        if numbers_list[start] != numbers_list[end]:
            return False
        
        # Move the pointers towards the center
        start += 1
        end -= 1
    
    # If the loop completes without finding a mismatch, the list is a palindrome
    return True
