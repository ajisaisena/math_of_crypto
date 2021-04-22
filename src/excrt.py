def extended_gcd(a, mod):  # 扩展欧几里得算法
    if a[2] == 0:
        return mod[1]
    else:
        q = mod[2] // a[2]
        t1 = mod[0] - q * a[0]
        t2 = mod[1] - q * a[1]
        t3 = mod[2] - q * a[2]
        return extended_gcd([t1, t2, t3], a)


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# 本题为扩展中国剩余定理，当两个模数不互素的时候使用


def ex_crt(ls):
    m = ls[0][0]
    b = ls[0][1]
    for i in range(1, len(ls)):
        m_gcd = int(gcd(m, ls[i][0]))
        m_in_e = int(extended_gcd(
            [0, 1, int(m // m_gcd)], [1, 0, int(ls[i][0] // m_gcd)]))
        b = int(((m_in_e * int((ls[i][1] - b) // m_gcd))
                 * m + b) % int((m * ls[i][0]) // m_gcd))  # 关键公式
        m = int((m * ls[i][0]) // m_gcd)
    return [b, m]


def main():
    a1 = int(input("a1="))
    a2 = int(input("a2="))
    a3 = int(input("a3="))
    b1 = int(input("b1="))
    b2 = int(input("b2="))
    b3 = int(input("b3="))
    ls = [[a1, b1], [a2, b2], [a3, b3]]
    print("x = %d mod %d" % (ex_crt(ls)[0], ex_crt(ls)[1]))


if __name__ == '__main__':
    main()
