class My_calc:

    def add(*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def multiply(*args):
        mul = 1
        for i in args:
            mul *= i
        return mul
    
    def subtraction(x , *args):
       sub = x
       for i in args:
           sub -= i
       return sub
    
    def division(x, *args):
        quo = x/1
        for i in args:
            # try:
            quo = quo/i
            # except Exception:
            #     print("ERROR: cannot divide by 0")
        return quo

           
        

