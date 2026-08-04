def demo_bitwise():
    """Bitwise AND, OR, XOR, NOT, shifts."""
    a = 0b1010  # 10
    b = 0b1100  # 12
    print(f"a = {a:04b}, b = {b:04b}")
    print(f"a & b = {a & b:04b}  ({a & b})")   # 1000 (8)
    print(f"a | b = {a | b:04b}  ({a | b})")   # 1110 (14)
    print(f"a ^ b = {a ^ b:04b}  ({a ^ b})")   # 0110 (6)
    print(f"~a = {~a} (two's complement)")
    print(f"a << 2 = {a << 2}")                # 40
    print(f"a >> 1 = {a >> 1}")                # 5

demo_bitwise()