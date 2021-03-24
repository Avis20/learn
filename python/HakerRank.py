


'''
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == '__main__':
    str_ = "ABCDCDC"
    sub_str = 'CDC'
    result_str = count_substring(str_, sub_str)
    print(result_str)
'''

'''
def mutate_string(string, position, character):
    l = list(string)
    try:
        l[position] = character
    except IndexError:
        l
    return "".join(l)

if __name__ == '__main__':
    str_ = 'hello'
    result_str = mutate_string(str_, 100, 'o')
    print(result_str)
'''

'''
def split_and_join(line):
    return "-".join(line.split(" "))

if __name__ == '__main__':
    str_ = 'HackerRank.com presents "Pythonist 2".'
    result_str = split_and_join(str_)
    print(result_str)

'''

'''
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    str_ = 'HackerRank.com presents "Pythonist 2".'
    result_str = swap_case(str_)
    print(result_str)
'''
