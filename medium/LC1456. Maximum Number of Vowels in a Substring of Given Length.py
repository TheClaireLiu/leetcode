class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_count = 0
        current_count = 0

        s1 = 'aeiouAEIOU'

        for i in range(k):
            if s[i] in s1:
                current_count += 1
        max_count = current_count

        for i in range(k, len(s)):
            if s[i - k] in s1:
                current_count -= 1
            if s[i] in s1:
                current_count += 1
            max_count = max(max_count, current_count)
        return max_count