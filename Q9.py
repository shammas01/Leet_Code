class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        str1=''
        for i in range(len(y)):
            str1 = y[i] + str1
        print(str1)
        if y == str1:
            return True
        return False
    
        # or


        z = str(x)
        y = [i for i in range(len(z)) if z[i] == z[len(z)-1-i]]
        if len(y)==len(z):
            return True
        return False

obj=Solution()

print(obj.isPalindrome(101))