from random import randint


def quick_mul(x, n, m):  # 快速幂
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = result * x % m
        x = x * x % m
        n = n // 2
    return result % m


def miller_rabin(p):  # 本题主函数
    random_time = 100  # 用一个很小的数亦可；这个数是随手打的
    if p < 3:
        return p == 2  # 先进行2判定
    q = p - 1
    t = 0
    while q % 2 == 0:  # 先把q和t求好
        q //= 2
        t += 1
    for i in range(1, random_time+1):  # 进行random_time次检测
        a = randint(2, p-1)
        v = quick_mul(a, q, p)
        if v == 1 or v == p-1:  # 进行1或-1判定
            continue
        for j in range(t+1):
            v = v*v % p
            if v == p-1:
                break
        else:
            return False
    return True


def main():
    p = int(input("p="))
    print(miller_rabin(p))


if __name__ == '__main__':
    main()
