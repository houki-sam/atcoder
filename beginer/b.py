if __name__ == "__main__":
    first = {'A','T'}
    second = {'C','G'}

    N = input()

    for x in [first,second]:
        if len(x - {N}) == 1:
            print(list(x-{N})[0])