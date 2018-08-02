class Solution:
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        max_length = 0
        palindromic = ''
        if len(s) == 1:
            return s,len(s)
        for i in range(l):
            for j in range(i + 1, l):#从第二个字符开始进行比较回文
                is_palindromic = True
                #如果这一段字符左右不对称则跳出循环
                for k in range(i, int((i + j) / 2) + 1):
                    if s[k] != s[j - k + i]:
                        is_palindromic = False
                        break
                #判断当前回文是否是最长的
                if is_palindromic and (j - i + 1) > max_length:
                    max_length = j - i + 1
                    palindromic = s[i:j + 1]
        if palindromic == '':
            palindromic = s[0]
        return palindromic,max_length

str1=input()

solution=Solution
str2,length=solution.longestPalindrome(str1)

print(length)