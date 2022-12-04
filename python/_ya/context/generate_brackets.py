

# def get_sequence(n, k)

def check(s: str) -> bool:
    stack = []

    for c in s:
        if c == "(":
            stack.append(")")
        elif stack and stack[-1] == c:
            stack.pop(0)
    return True if not stack  else False 

ans = []
def gen(n, co=0, cc=0, res=""):
    if co + cc == n:
        print(res)
        # ans.append(res)
        return
    if co < n:
        gen(n, co + 1, cc, res + "(")
    if cc < co:
        gen(n, co, cc + 1, res + ")")
    


if __name__ == '__main__':
    
    # s = "(())"
    # print(check(s))
    gen(2)
    # print(len(ans))
    # print(ans)