

test_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

res = []
for lists in test_list:
    for number in lists:
        res.append(str(number))
# return ", ".join(res)
print(", ".join(res))
    # >>> 1;2;3;4;
    # >>> 5;6;7;8;

print(", ".join(str(number) for lists in test_list for number in lists))
# >>> 1, 2, 3, 4, 5, 6, 7, 8