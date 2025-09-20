class Solution:
    def myAtoi(self, s):
        sign = 1
        num = 0

        started = False
        max = 2**31-1
        min = 2**31*-1
        for char in s:
            
            if char == " " or char == "+" or char == '-':
                if started:
                    break
                else:
                    if char == "+":
                        started = True
                    elif char == '-':
                        sign = -1
                        started = True
                    continue
            if char == '1':
                num = num*10 + 1 
            elif char == '2':
                num = num*10 + 2
            elif char == '3':
                num = num*10 + 3
            elif char == '4':
                num = num*10 + 4
            elif char == '5':
                num = num*10 + 5
            elif char == '6':
                num = num*10 + 6
            elif char == '7':
                num = num*10 + 7
            elif char == '8':
                num = num*10 + 8
            elif char == '9':
                num = num*10 + 9
            elif char == '0':
                num = num*10 + 0
            else:
                break
            started = True
        ans = num*sign
        if sign > 0 and ans > max:
            return max
        elif sign < 0 and ans < min:
            return min
        return ans
                        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # Code here
        # sign=1
        # number=0
        # max = 2**31-1
        # min = 2**31*-1
        # for char in s:
        #     if char in ['','+']:
        #         continue
        #     if char == '-':
        #         sign=-1
        #         continue
        #     if char in '1':
        #         num = 1
        #     elif char in '2':
        #         num = 2
        #     elif char in '3':
        #         num = 3
        #     elif char in '4':
        #         num = 4
        #     elif char in '5':
        #         num = 5
        #     elif char in '6':
        #         num = 6
        #     elif char in '7':
        #         num = 7
        #     elif char in '8':
        #         num = 8
        #     elif char in '9':
        #         num = 9
        #     elif char in '0':
        #         num = 0
        #     else:
        #         break
    
        #     if number > 214748364 or (number == 214748364 and (num > 7 or (num > 8 and sign < 0))):
        #         if sign > 0:
        #             return max
        #         return min
        #     number = num + number*10
        # return number*sign