#correct

def isPalindrome(x):

    temp = x
    reversed = 0
    if x < 0:
        return False
    
    while temp !=0:
        digit = temp % 10 #taking the last digit by taking the remainder
        reversed = reversed *10 + digit #at first the val of digit is stored and because we want to add another number on the side, we shift the intial number
        temp //= 10 #we divide temp by 10 to remove that last digit used

    if reversed == x:
        return True

x = 120   
print(isPalindrome(x))

        

