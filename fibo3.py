
def input_n():
    return int(input("Enter the number of Fibonacci numbers to be displayed: "))

def fibonacci(n):
    num1, num2 = 0, 1
    while(n):
        yield num1
        num1, num2 = num2, num1 + num2
        n -= 1

def main():
    n = input_n()
    for i in (x**2 for x in fibonacci(n)):
        print(i)

if __name__ == "__main__":
    main()
