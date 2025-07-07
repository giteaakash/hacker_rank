if __name__ == '__main__':
    print("running..")
    n = int(input())
    s=[]
    for i in range(1,n+1):
        i = str(i)
        s.append(i)
    result = ''.join(s)
    print(result)
    