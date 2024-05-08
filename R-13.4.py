def boyer_moore(text, pattern):
    def compute_last_occurrence(pattern):
        last = [-1] * 256  # Initialize all characters with -1 (not found)
        for i, char in enumerate(pattern):
            last[ord(char)] = i  # Store the rightmost occurrence of each character
        return last
    
    def boyer_moore_search(text, pattern):
        m = len(pattern)
        n = len(text)
        last = compute_last_occurrence(pattern)
        
        # Begin the search
        i = m - 1  
        j = m - 1  
        
        while i < n:
            if text[i] == pattern[j]:
                if j == 0:
                    # Match found
                    return i
                else:
                    # Continue matching
                    i -= 1
                    j -= 1
            else:
                # Mismatch, shift pattern to align with last occurrence of text[i] in pattern
                i += m - min(j, 1 + last[ord(text[i])])
                j = m - 1  # Reset j to the end of pattern
        
        return -1  # Pattern not found
    
    return boyer_moore_search(text, pattern)

# Test
text = "aaabaadaabaaa"
pattern = "aabaaa"
result = boyer_moore(text, pattern)
print("Pattern found at index:", result)
