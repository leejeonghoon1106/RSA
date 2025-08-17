import math
import numpy as np
from math import gcd

def relative_primes(n):
    result = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            result.append(i)
        if len(result) >= 4000:
            break
    return result

def encryption(text, p, q, e):
    n = p * q
    print(f"공개키 = {n}")
    phi = (p - 1) * (q - 1)
    d = pow(e , -1, phi)
    print(f"개인키(유출금지) = {d}")

    encrypted_num = []
    for i in text:
        character = ord(i)
        m = pow(character, e, n)
        encrypted_num.append(m)
    print(f"암호화된 숫자: {encrypted_num}")
    binary_text = []
    for j in encrypted_num:
        binary_text.append(bin(j)[2:])
    binary_text = ' '.join(binary_text)        
    print(f"2진수 암호화 문자 : ", end="")
    return binary_text

def decryption(text, n, d):
    decrypted_text = []
    binary_to_int = []
    text_without_space = text.split()
    for _ in text_without_space:
        binary_to_int.append(int(_, 2))
        print(binary_to_int)

    for i in binary_to_int:
        m = pow(i, d, n)
        decrypted_text.append(m)

    print(f"복호화된 숫자: {decrypted_text}")
    num_to_char = []
    for j in decrypted_text:
        num_to_char.append(chr(j))
    decrypted_str = ''.join(num_to_char)
    print(f"복호화된 문자열: ", end="")
    return decrypted_str

mode = input("암호화를 할지 복호화를 할지 선택하세요 (암호화/복호화): ")
if mode == "암호화":
    p, q = map(int, input("두 소수를 입력하세요: ").split())
    print(relative_primes((p-1) * (q-1)))
    e = int(input(f"공개키를 입력하세요(e) [단 e < {(p-1)*(q-1)}]: "))
    if gcd(e, (p-1)*(q-1)) != 1:
        print("잘못된 공개키입니다. e와 (p-1)*(q-1)의 최대공약수가 1이어야 합니다.")
        exit()
    text = input("암호화할 문자열을 입력하세요: ").lower()
    print(encryption(text, p, q, e))

if mode == "복호화":
    n, d = map(int, input("공개키 n, 개인키 d를 입력하세요: ").split())
    text = input("복호화할 문자열을 입력하세요: ").lower()
    print(decryption(text, n, d))