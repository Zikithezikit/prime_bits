def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

    Parameters:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two integers.

    Parameters:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The LCM of a and b.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def euler_totient(n):
    """
    Calculate Euler's Totient Function φ(n), which counts the integers from 1 to n
    that are coprime with n.

    Parameters:
        n (int): The input integer.

    Returns:
        int: The value of φ(n).
    """
    if n <= 0:
        return 0
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result