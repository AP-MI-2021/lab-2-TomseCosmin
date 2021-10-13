def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    '''
    Test pentru is_prime
    '''
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(29) == True


test_is_prime()


def get_largest_prime_below(n):
    if n == 3:
        print("2")
        return 2
    else:
        for m in range(n - 1, 1, -1):
            if is_prime(m) == True:
                print(m)
                return (m)
                break


def test_get_largest_prime_below():
    '''
    Test pentru get_largest_prime_below
    '''
    assert get_largest_prime_below(12) == 11
    assert get_largest_prime_below(14) == 13


test_get_largest_prime_below()


def get_n_choose_k(n: int, k: int) -> int:
    produs1 = 1
    produs2 = 1
    produs3 = 1
    i: int
    for i in range(1, n + 1):
        produs1 = produs1 * i
    for j in range(1, k + 1):
        produs2 = produs2 * j
    for l in range(1, n - k + 1):
        produs3 = produs3 * l
    print(produs1 / (produs3 * produs2))


def get_base_16_from_2(n: str) -> str:
    v = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101",
         "1110", "1111"]
    z = ""
    if len(n) % 4 != 0:
        n = (4 - len(n) % 4) * "0" + n
    while n != "":
        i = v.index(n[-4:])
        if i < 10:
            z += str(i)
        elif i == 10:
            z += "A"
        elif i == 11:
            z += "B"
        elif i == 12:
            z += "C"
        elif i == 13:
            z += "D"
        elif i == 14:
            z += "E"
        elif i == 15:
            z += "F"
        n = n[:-4]

    return z


def test_get_base_16_from_2():
    '''
    functie test pt get_base_16_from_2
    '''
    a=str("11")
    b=str("10001")
    assert get_base_16_from_2(a) == "3"
    assert get_base_16_from_2(b) == "11"

test_get_base_16_from_2()


def main():
    print("1. Determinati cel mai mare nr prim mai mic decat un nr dat")
    print("2. Calculati combinari de n luate cate k")
    print("3.convertiti din baza 2 in baza 16")
    print("x. Iesire")
    while True:
        optiune = input("dati optiune: ")
        if optiune == "1":
            x = int(input("Dati nr.:"))
            get_largest_prime_below(x)
            main()
        if optiune == "2":
            x = int(input("Dati nr.elemente:"))
            y = int(input("Dati nr. elemente luate cate:"))
            get_n_choose_k(x, y)
            main()
        if optiune == "3":
            print("scrieti un nr multiplu de 4 de 0 si 1")
            x = input()
            x = get_base_16_from_2(x)
            print("nr dat in baza 16 este", x[::-1])
            main()
        if optiune == "x":
            print("interfata de tip consola a fost inchisa")
            return False
        else:
            return False
            print("optiune gresita")


main()


