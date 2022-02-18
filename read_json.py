import json


def read_file(file_path):
    """
    Return a file
    """
    with open(file_path, 'r', encoding = 'utf-8') as rea_file:
        data = json.load(rea_file)
    try:
        if type(data) is list:
            num = int(input(f"Please choose index of dictionary in list from 0 to {len(data)-1}: "))
            if num>len(data)-1:
                print("Wrong answer")
                exit()
            return data[int(num)]
        elif type(data) is dict:
            return data
    except TypeError or AttributeError:
        print("Wrong answer")
        exit()

def all_keys(file):
    """
    Return all keys in given dictionary
    """
    key_list = []
    for key in file.keys():
        key_list.append(key)
    return key_list


def main(file_path):
    data = read_file(file_path)
    print(all_keys(data))
    while True:
        input_key = input("Choose a key from list: ")
        if not input_key:
            break
        data = data[input_key]
        if type(data) == list:
            print(f'Number of elements in list: {len(data)}')
            if len(data) == 0:
                break
        elif type(data) == dict:
            print(f'Dict keys are: {list(data.keys())}')
        else:
            print(f'Value is: {data}')
            break

main()
