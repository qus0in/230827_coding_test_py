x_right, y_up = int(input()) > 0, int(input()) > 0
if x_right and y_up:
    print(1)
elif not x_right and y_up:
    print(2)
elif not x_right and not y_up:
    print(3)
else:
    print(4)
