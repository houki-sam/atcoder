if __name__ == "__main__":
    abck=input().split(" ")
    A,B,C,K =int(abck[0]),abck[1],abck[2],int(abck[3])
    first_sort=[]
    set_sort=[[],[],[]]
    for x in set_sort:
        stack=input().split(" ")
        for y in stack:
            x.append(int(y))
    compare_list=[]
    for x in set_sort[0]:
        for y in set_sort[1]:
            compare_list.append(x+y)
    compare_list.sort(reverse=True)
    compare_list2=[]
    if len(compare_list)>K:
        compare_list=compare_list[:K]
    for x in compare_list:
        for y in set_sort[2]:
            compare_list2.append(x+y)
    
    compare_list2.sort(reverse=True) 
    for x in compare_list2[:K]:
        print(x)
    
    