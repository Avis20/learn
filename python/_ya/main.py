from itertools import permutations

# str1 = set(input().strip())
# str2 = set(input().strip())

str1 = "hello"
str2 = "helel"

is_same = 0
for comb in permutations(str1):
    print("".join(comb))
    if "".join(comb) == str2:
        is_same = 1
        break

print(is_same)
