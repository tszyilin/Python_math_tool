# Calculate the slope
def slope(x1, y1, x2, y2):
    a = (y2-y1) / (x2-x1)
    b = y1 - (a*x1)
    return a

def cof(x1, y1, x2, y2):
    a = (y2-y1) / (x2-x1)
    b = y1 - (a*x1)
    return b

print("請輸入兩點X、Y座標")
X1 = float(input("X1 座標: "))
Y1 = float(input("Y1 座標: "))
X2 = float(input("X2 座標: "))
Y2 = float(input("Y2 座標: "))


slope_result = slope(X1, Y1, X2, Y2)
cof_result = cof(X1, Y1, X2, Y2)

print("公式為 y = {0}x+{1}".format(slope_result, cof_result))

exit_para = 0
while exit_para == 0:
    x_input = float(input("X 座標"))
    y_result = slope_result * x_input;

    print("Y 座標為: {0}".format(y_result))
    exit_para = int(input("繼續請輸入0，離開請輸入1\n"))


    
