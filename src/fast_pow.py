def fast_pow(x, n, m):  # 本题主函数
    result = 1
    while n > 0:
        if n % 2 == 1:  # 对n进行二进制转换时，遇1需要乘上去
            result = result * x % m
        x = x * x % m
        n = n // 2
    result = result % m
    print(result)
    return result


def main():
    x = int(input("x="))
    n = int(input("n="))
    m = int(input("m="))
    fast_pow(x, n, m)


if __name__ == "__main__":
    main()
