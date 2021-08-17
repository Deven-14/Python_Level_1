
class Fibonacci:

    def __init__(self, n):
        self.n = n
        if self.n <= 0:
            raise ValueError

    def __iter__(self):
        self.num1, self.num2 = 0, 1
        self.i = 1
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        
        temp, self.num1, self.num2 = self.num1, self.num2, self.num1 + self.num2
        self.i += 1
        return temp

def main():
    x = Fibonacci(15)
    for i in x:
        print(i)

if __name__ == "__main__":
    main()
