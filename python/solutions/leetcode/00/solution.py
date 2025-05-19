
def rank(citations):
    n = len(citations)
    # Step 1: Create the count array
    count = [0] * (n + 1)

    # Step 2: Populate the count array
    for citation in citations:
        if citation >= n:
            count[n] += 1
        else:
            count[citation] += 1

    # Step 3: Calculate the cumulative sum from the end
    cumulative = 0
    for i in range(n, -1, -1):
        cumulative += count[i]
        if cumulative >= i:
            return i
    return 0  # This case happens if no valid R is found
