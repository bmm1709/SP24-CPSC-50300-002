def find_duplicates(elements: List[int]):
    seen = set()
    for num in elements:
        if num in seen:
            return True
        seen.add(num)
    return False