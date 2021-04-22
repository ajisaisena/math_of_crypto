def extended_gcd(a, b):  # 本题主函数
    if a[2] == 0:
        print("%d %d %d" % (b[1], b[0], b[2]))
    else:  # 使用矩阵进行不断的行变化
        q = b[2] // a[2]
        t1 = b[0] - q * a[0]
        t2 = b[1] - q * a[1]
        t3 = b[2] - q * a[2]
        extended_gcd([t1, t2, t3], a)  # 递归求法


def main():
    a = int(input("a="))
    b = int(input("b="))
    extended_gcd([0, 1, a], [1, 0, b])


if __name__ == "__main__":
    main()
