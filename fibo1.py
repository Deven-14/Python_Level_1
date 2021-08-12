
class Fibonacci:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.num1, self.num2, self.next_num = 0, 1, 1
        self.i = 1
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
            
        if self.i == 1:
            self.i += 1
            return 0
        elif self.i == 2:
            self.i += 1
            return 1
            
        if self.i > self.n:
            raise StopIteration
            
        self.next_num = self.num1 + self.num2
        self.num1, self.num2 = self.num2, self.next_num
        self.i += 1
        return self.next_num

def main():
    x = Fibonacci(15)
    for i in x:
        print(i)

if __name__ == "__main__":
    main()
