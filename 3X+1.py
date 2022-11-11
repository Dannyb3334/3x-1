"""
This is the Collatz Conjecture test
"""
def function():
    num = (float(eval(input("Enter a number to test: "))))
    try:
        while num != 1:
            if (num % 2) == 0:
                num = num / 2
            else:
                num = (num * 3) + 1
            print(int(num))
    except:
        function()

function()