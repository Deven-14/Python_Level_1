
def input_concatinated_string():
    return input("Enter a concatinated string: ");

def concatinated_string_to_list_of_tuples(concatinated_string):
    return [(*string.split('='), ) for string in concatinated_string.split(';')]

if __name__ == "__main__":
    concatinated_string = input_concatinated_string()
    list_of_tuples = concatinated_string_to_list_of_tuples(concatinated_string)
    print(list_of_tuples)
