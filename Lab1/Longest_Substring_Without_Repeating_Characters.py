class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        left = 0
        sub = set()
        maxlen = 0

        for right in range(len(s)):
            if s[right] not in sub:
               sub.add(s[right])
               maxlen = max(maxlen, right - left + 1)
            else:
                while s[right] in sub:
                    sub.remove(s[left])   
                    left += 1
                sub.add(s[right])
                        
            print(sub)
        return(maxlen)


            




    print(lengthOfLongestSubstring("pwwkew"))