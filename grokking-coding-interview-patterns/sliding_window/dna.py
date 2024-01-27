


# hashing function
# h = c1 a^(k-1) + c2 a^(k-2) + ... + ck a^0

def hash_function(nums, k):
    base = 4
    h = 0
    for i in range(k):
        h += nums[i] * (base ** (k - i - 1))
    return h

def find_repeated_sequences_1(s,k):
    window_size = k
    if len(s) <= window_size:
        return set()
    base = 4
    hi_place_value = pow(base, window_size - 1)
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(mapping.get(s[i]))
    hashing = 0
    substring_hashes, output = set(), set()
    for start in range(len(s) - window_size + 1):
        if start != 0:
            hashing = (hashing - numbers[start - 1] * hi_place_value) * base \
                + numbers[start + window_size - 1]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        if hashing in substring_hashes:
            output.add(s[start:start + window_size])
        substring_hashes.add(hashing)
    return output

def find_repeated_sequences(s, k):
    map = {"A": 1, "C": 2, "G": 3, "T": 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(map[s[i]])

    base = 4
    n = len(s)
    if n < k:
        return []

    hash_value = 0
    prev = 0
    hash_set , output = set(), set()

    for i in range(n - k + 1):
        if i == 0:
            for j in range(k):
                hash_value += numbers[j] * (base ** (k - j - 1))
        else:
            prev = hash_value
            hash_value = ((prev - numbers[i - 1]
                * (base ** (k -1))) * 4) + numbers[i + k - 1]

        if hash_value in hash_set:
            output.add(s[i : i + k])

        hash_set.add(hash_value)
        #print("\tHash value of ", s[i : i + k], ":", hash_value, 
        #      "\n\tHash set: ", hash_set, 
        #      "\n\tOutput: ", output, 
        #      "\n")
    print("\toutput: ", output)


def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i + 1, ".\tInput sequence:",inputs_string[i], 
                     "\n\tk:", inputs_k[i],
                     "\n\n\tRepeated sequences:", find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)

main()
