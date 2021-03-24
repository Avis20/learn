

if __name__ == '__main__':
    N = int(input())
    array = []
    for i in range(N):
        params = str(input()).split(' ')
        command = params[0]
        del params[0]
        params = list(map(int, params))

        if command == 'insert':
            array.insert(int(params[0]), params[1])
        elif 'print' == command:
            print(array)
        elif 'remove' == command:
            array.remove(params[0])
        elif command == 'append':
            array.append(params[0])
        elif command == 'sort':
            array.sort()
        elif command == 'pop':
            array.pop()
        elif command == 'reverse':
            array.reverse()
