class Solution(object):
    def plusOneUnoptimized(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        first = True
        carry = 1
        counter = 1
        digit_len = len(digits)
        while carry and counter <= digit_len:
            digits[counter*-1] = digits[counter*-1] + carry
            if digits[counter*-1] == 10:
                digits[counter*-1] = 0
            else:
                carry = 0
            
            counter += 1
            
        if carry:
            digits.insert(0, carry)
            
        return digits
        
    def plusOneOptimized(self, digits):
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return [int(i) for i in str(num+1)]