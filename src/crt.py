def extended_gcd(M, m):  # 扩展欧几里得算法
    if M[2] == 0:
        result = m[1]
        return result
    else:
        q = m[2] // M[2]
        t1 = m[0] - q * M[0]
        t2 = m[1] - q * M[1]
        t3 = m[2] - q * M[2]
        return extended_gcd([t1, t2, t3], M)


def get_Mi(m1, m2, m3):  # 获取中国剩余定理中的Mi及m
    m = m1 * m2 * m3
    return [m2*m3, m1*m3, m1*m2, m]


def get_in_e(M1, M2, M3, m1, m2, m3):  # 获取每个Mi的逆元
    A1 = [0, 1, M1]
    B1 = [1, 0, m1]
    A2 = [0, 1, M2]
    B2 = [1, 0, m2]
    A3 = [0, 1, M3]
    B3 = [1, 0, m3]
    e1 = extended_gcd(A1, B1)
    e2 = extended_gcd(A2, B2)
    e3 = extended_gcd(A3, B3)
    return [int(e1), int(e2), int(e3)]


def crt(b1, b2, b3, m1, m2, m3):  # 本题主函数
    M1, M2, M3, m = get_Mi(m1, m2, m3)
    e1, e2, e3 = get_in_e(M1, M2, M3, m1, m2, m3)
    x = (M1*e1*b1+M2*e2*b2+M3*e3*b3) % m
    print("x = % d mod % d" % (x, m))
    return x


def main():
    a1 = int(input("a1="))
    a2 = int(input("a2="))
    a3 = int(input("a3="))
    b1 = int(input("b1="))
    b2 = int(input("b2="))
    b3 = int(input("b3="))
    crt(b1, b2, b3, a1, a2, a3)


if __name__ == '__main__':
    main()
