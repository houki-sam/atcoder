if __name__ == "__main__":
    NQ = input().split(" ")
    N ,Q = int(NQ[0]),int(NQ[1])

    S = input()
    stack =[]
    for x in range(Q):
        lr = input()
        lr = lr.split(" ")
        l ,r = int(lr[0]),int(lr[1])
        target = S[l-1:r]
        stack.append((r-l+1-len(target.replace("AC"," "))))

    for x in stack:
        print(x)
