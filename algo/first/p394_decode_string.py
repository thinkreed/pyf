class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def helper(s, i):
            res = ''

            while i < len(s):
                if not s[i].isdigit():
                    res += s[i]
                    i += 1
                elif s[i].isdigit():
                    n = 0
                    while i < len(s) and s[i].isdigit():
                        n = n * 10 + ord(s[i]) - ord('0')
                        i += 1

                    i += 1
                    extracted = helper(s, i)

                    while n > 0:
                        res += extracted
                        n -= 1
                elif s[i] == ']':
                    i += 1
                    return res

        return helper(s, 0)

print(Solution().decodeString("3[a2[c]]"))
