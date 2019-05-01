import math
if __name__ =="__main__":
    N = input()
    N = float(N)
    cap_min=10.0**16
    for x in range(5):
        a = input()
        cap_min = min(float(a),cap_min)
    time = math.ceil(N/cap_min)+4
    print(time)