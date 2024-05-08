def brute_force_pattern_matching(text, pattern):
    comparisons = []
    text_length = len(text)
    pattern_length = len(pattern)
    
    for i in range(text_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break
        comparisons.append((i, match))
    
    return comparisons

def draw_comparisons(text, pattern, comparisons):
    print("Text:", text)
    print("Pattern:", pattern)
    print("\nComparison Steps:")
    for i, (index, match) in enumerate(comparisons):
        print("  Text:   ", text)
        print("  Pattern:", " " * index + pattern)
        if match:
            print("  Match:  ", " " * index + "!" * len(pattern))
        else:
            print("  Match:  ", " " * index + "x" * len(pattern))
        if i < len(comparisons) - 1:
            print()

text = "aaabaadaabaaa"
pattern = "aabaaa"
comparisons = brute_force_pattern_matching(text, pattern)
draw_comparisons(text, pattern, comparisons)
