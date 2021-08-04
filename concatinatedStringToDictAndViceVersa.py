
def input_concatinated_string():
    return input("Enter a concatinated string: ");

def concatinated_string_to_dict(concatinated_string):
    return {str1: str2 for str1, str2 in (string.split('=') for string in concatinated_string.split(';'))}

def dict_to_concatinated_string(dict_):
    return ';'.join(['='.join(ele) for ele in dict_.items()])

if __name__ == "__main__":
    concatinated_string = input_concatinated_string()
    dict_ = concatinated_string_to_dict(concatinated_string)
    print(dict_)
    concatinated_string = dict_to_concatinated_string(dict_)
    print(concatinated_string)
