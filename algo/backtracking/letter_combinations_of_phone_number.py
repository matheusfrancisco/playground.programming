

# Given a phone number that contains digits 2-9, find all possible letter combinations the phone
# number could translate to.

def get_letters(digit):
    if digit == "2":
        return ["a", "b", "c"]
    if digit == "3":
        return ["d", "e", "f"]
    if digit == "4":
        return ["g", "h", "i"]
    if digit == "5":
        return ["j", "k", "l"]
    if digit == "6":
        return ["m", "n", "o"]
    if digit == "7":
        return ["p", "q", "r", "s"]
    if digit == "8":
        return ["t", "u", "v"]
    if digit == "9":
        return ["w", "x", "y", "z"]


KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

## space complexity O(4^n)
def letter_combinations_of_phone_number(digits):
    res = []

    def dfs(start, path):
        if start == len(digits):
            res.append("".join(path))
            return

        # for letter in get_letters(digits[start]):
        next_digit = digits[start]
        for letter in KEYBOARD[next_digit]:
            path.append(letter)
            dfs(start + 1, path)
            path.pop()

    dfs(0, [])
    return res


print(letter_combinations_of_phone_number("56"))
