class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        org=x;
        rev=0
        while(x>0):
            num=x%10
            rev=num+rev*10
            x=x/10
        if rev==org:
            return True
        else:
            return False        