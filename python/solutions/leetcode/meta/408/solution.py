class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        count = 0
        # i12
        while i < len(abbr):
            if abbr[i] == '0' or count >= len(word):
                return False

            number = ''
            # handle number
            while i < len(abbr) and abbr[i].isdigit():
                number += abbr[i]
                i += 1

            if number:
                count += int(number)
            else:
                if abbr[i] != word[count]:
                    return False
                count += 1
                i += 1

        return count == len(word)


class Solution2:

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        word_idx = abbr_idx = 0
        abbr_length = len(abbr)
        word_length = len(word)

        while word_idx < word_length:
            if abbr_idx >= abbr_length:
                return False

            if word[word_idx] == abbr[abbr_idx]:
                word_idx += 1
                abbr_idx += 1
                continue
            if not abbr[abbr_idx].isdigit():
                return False
            number_start_index = abbr_idx
            while abbr_idx < abbr_length and abbr[abbr_idx].isdigit():
                abbr_idx += 1
            number_str = abbr[number_start_index:abbr_idx]
            if number_str[0] == "0":
                return False
            word_idx += int(number_str)
        return word_idx == word_length and abbr_idx == abbr_length


class Solution3:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                steps = 0
                if abbr[abbr_ptr] == '0':
                    return False

                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    steps = steps * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                word_ptr += steps
            else:
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                word_ptr += 1
                abbr_ptr += 1
        return len(word) == word_ptr and len(abbr) == abbr_ptr


obj = Solution()
print(obj.validWordAbbreviation("internationalization", "i12iz4n") == True)

obj = Solution2()
print(obj.validWordAbbreviation("internationalization", "i12iz4n") == True)

obj = Solution3()
print(obj.validWordAbbreviation("internationalization", "i12iz4n") == True)
