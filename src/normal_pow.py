def normal_mul(x, n, m):  # 本题主函数
    result = x
    for i in range(1, n):
        result = ((result % m) * x) % m
    print(result)
    return result

# 该代码文件为普通幂取模运算


def main():
    x = int(input("x= "))
    n = int(input("n= "))
    m = int(input("m= "))
    normal_mul(x, n, m)


if __name__ == "__main__":
    main()
