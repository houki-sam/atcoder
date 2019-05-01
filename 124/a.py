if __name__ == "__main__":
    button = input()
    button = button.split(" ")
    button1 ,button2 = int(button[0]),int(button[1])
    total = 0
    for x in range(2):
        if button1>button2:
            total+=button1
            button1-=1
        else:
            total+=button2
            button2-=1
    print(total)