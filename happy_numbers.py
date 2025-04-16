def sumsq(r):
        m=0
        while r:
            k=r%10
            m+=k**2
            r=r//10
        return m 

class Solution(object):

     

     def isHappy(self, n):
       l=[]
       while n not in l:
            l.append(n)
            n=sumsq(n)
            if n==1:
             return True
       return False     
          
      
