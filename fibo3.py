
def input_n():
    return int(input("Enter the number of Fibonacci numbers to be displayed: "))

def fibonacci(n):
    i = n + 1
    num1, num2, next_num = 0, 1, None
    while(i := i-1):
        next_num, num1, num2 = num1, num2, num1 + num2
        yield next_num

def main():
    n = input_n()
    for i in (x**2 for x in fibonacci(n)):
        print(i)

if __name__ == "__main__":
    main()
