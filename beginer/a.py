if __name__ =="__main__":
    first_input = input()
    second_input = input()
    third_input = input()
    
    a = int(first_input)
    stack = second_input.split(" ")
    b, c = int(stack[0]), int(stack[1])
    
    total = a + b + c
    print(str(total) + " " +third_input)