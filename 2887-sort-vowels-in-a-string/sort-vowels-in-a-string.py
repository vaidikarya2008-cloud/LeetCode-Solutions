class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        ind = []

        vow = ['a','i','o','e','u','A','O','I','E','U']

        for i in range(len(s)):
            if s[i] in vow:
                vowels.append(s[i])
                ind.append(i)

        vowels.sort()

        lst = list(s)

        for j in range(len(vowels)):
            lst[ind[j]] = vowels[j]

        return "".join(lst)