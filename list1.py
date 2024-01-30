def operation(dic, op, *args):
    if op == 'insert':
        dic.insert(int(args[0][0]), int(args[0][1]))
    elif op == 'print':
        print(dic)
    elif op == 'remove':
        dic.remove(int(args[0][0]))
    elif op == 'append':
        dic.append(int(args[0][0]))
    elif op == 'sort':
        dic.sort()
    elif op == 'pop':
        dic.pop()
    elif op == 'reverse':
        dic.reverse()
    return dic


if __name__ == '__main__':
    N = int(input())
    dic = [1,2,3,4,5,6,7,8,9,10,11,12]
    for _ in range(N):
        op = input()
        op = op.split()
        operation(dic, op[0], op[1:])
    print(dic)
