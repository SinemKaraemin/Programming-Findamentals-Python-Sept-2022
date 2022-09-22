divisior=int(input())
boundary=int(input())

for current_num in range(boundary,divisior,-1):
    if current_num%divisior==0:
        break
print(current_num)