def count(string):
    checker = [char for char in string if char.isupper()]
    return 1 + len(checker)

if __name__ == '__main__':
    string = input()
    print(count(string))