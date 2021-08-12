
def input_n():
    return int(input("Enter the number of Fibonacci numbers to be displayed: "))

def fibonacci(n):
    if n < 0:
        return None
    
    yield 0
    yield 1
    num1, num2, next_num = 0, 1, 1
    for _ in range(2, n):
        next_num = num1 + num2
        yield next_num
        num1, num2 = num2, next_num

def main():
    n = input_n()
    for i in fibonacci(n):
        print(i)

if __name__ == "__main__":
    main()
