def gcd(a, b):  # 本题主函数
    return a if b == 0 else gcd(b, a % b)  # 递归求法


def main():
    a = int(input("a="))
    b = int(input("b="))
    print(gcd(a, b))


if __name__ == "__main__":
    main()
