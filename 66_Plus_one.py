# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

#123 => 124
#129 => 130

def plusOne(self, digits):
    if not digits:
        return 0
    
    for i in range(len(digits)-1,-1,-1): #starting from the last
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i]+1
            return digits
    return [1] + digits

digits = [9,9,9]
print(plusOne(None, digits))  # Output: [1, 0, 0, 0]