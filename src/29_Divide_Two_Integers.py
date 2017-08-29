import sys  

claSolution ss():
    def divide(self, dividend, divisor):
        if not divisor:
            raise ZeroDivisionError

        positive = (dividend > 0) == (divisor > 0)

        dividend, divisor = abs(dividend), abs(divisor)

        result = 0

        while dividend >= divisor:
            i = divisor
            count = 1
            while dividend >= i:
                dividend -= i
                result += count
                count *= 2
                i <<= 1
        
        if not positive:
            result *= -1


        if result < sys.maxint and result > -1-sys.maxint:
            return result
        else:
            return sys.maxint if result > sys.maxint else -1-sys.maxint

        

a = Solution()   
print a.divide(-2147483648,-1)
