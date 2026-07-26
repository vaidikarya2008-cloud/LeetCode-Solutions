class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    final = j - i - 1
                    if final != distance[ord(s[i]) - ord('a')]:
                        return False
                    break
        return True