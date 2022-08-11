def Rectangle(x, y):
    A = x*y
    return A

def Trapezoid(x, y, z):
    A = ((x + y) * z)/2
    return A

def Triangle (X, Y):
    A = (X * Y) / 2
    return A
    

exit_para = 0;
while exit_para == 0:
    print("請輸入要計算的形狀")
    print("長方形請輸入1\n梯形請輸入2\n三角形請輸入3")
    number = int(input())

    if number == 1:
        x1 = float(input("請輸入長: "))
        x2 = float(input("請輸入寬: "))
        result = Rectangle(x1, x2)
        print("長方形面積為： {0}".format(result))
        
    elif number == 2:
        x1 = float(input("請輸入上底: "))
        x2 = float(input("請輸入下底: "))
        x3 = float(input("請輸入高: "))
        result = Trapezoid(x1, x2, x3)
        print("梯形上底、下底、高、面積為: {0}, {1}, {2}, {3}".format(x1, x2, x3, result))
    elif number == 3:
        x1 = float(input("請輸入底: "))
        x2 = float(input("請輸入高: "))
        result = Triangle(x1, x2)
        print("三角形面積為: {0}".format(result))
        
    print("繼續請輸入0，離開請輸入1")
    exit_para = int(input())    
    
