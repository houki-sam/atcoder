def amari(num):
    if num%10 ==0:
        return 10
    return num%10

if __name__ =="__main__":
    S = []
    for x in range(5):
        S.append(int(input()))
    max_num = min(S,key=amari)
    S.remove(max_num)
    total=0
    for x in S:
        if x%10 == 0:
            total += x
        else:
            total+=(int(x/10)+1)*10
    print(total+max_num)
    
    