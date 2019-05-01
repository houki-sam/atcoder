if __name__ =="__main__":
    kyori = []
    for x in range(5):
        kyori.append(input())
    
    k = input()

    max_length=int(kyori[4])-int(kyori[0])

    if max_length <= int(k):
        print("Yay!")
    else:
        print(":(")