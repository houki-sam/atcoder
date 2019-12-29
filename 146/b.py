num2alpha = lambda c: chr(c+64)
alpha2num = lambda c: ord(c) - ord('A') + 1

length = int(input())
string=input()
num_list=[(alpha2num(x)+length)%26 if (alpha2num(x)+length)%26 =!0 else 26 for x in string]
converted = "".join([num2alpha(x) for x in num_list])
print(converted)






