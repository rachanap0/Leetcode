#Correct
#Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# for signed int, the max is (2^31)-1 and the min is -2^31


def reverse(x):
   max = 2**31-1
   min = -2**31

   reverse = 0
   sign = -1 if x<0 else 1

   x = abs(x)

   while x!=0:
      if reverse > max/10 or reverse <min /10:
         return 0
      
      digit = x%10
      reverse = reverse *10 + digit
      print (reverse)
      x= x //10 #x = math.trunc(x / 10) can use this also but need to import math
   reverse *= sign

   return reverse

num = -123
print(reverse(num))


