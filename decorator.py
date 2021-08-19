from functools import wraps

def decorator(func):
    @wraps(func)
    def print_args_value(*args, **kwargs):
        for ele in args:
            print(ele)
        for ele in kwargs.values():
            print(ele)
        x = func(*args, **kwargs)
        return x

    return print_args_value
        

@decorator
def decorate(*args, **kwargs):
    print("Do some work")
    return "Completed"

def main():
    print(decorate(1, 2, c=3, d=4))

if __name__ == "__main__":
    main()
