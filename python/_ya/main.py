

test_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

for lists in test_list:
    for number in lists:
        print(number, end=";")
    print()
    # >>> 1;2;3;4;
    # >>> 5;6;7;8;

print(", ".join(str(number) for lists in test_list for number in lists))
# >>> 1, 2, 3, 4, 5, 6, 7, 8