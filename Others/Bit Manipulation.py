def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def swap(a, b):
    return b, a

def toggle_ith_bit(n, i):
    return n ^ (1 << i)

def clear_ith_bit(n, i):
    return n & ~(1 << i)

def set_ith_bit(n, i):
    return n | (1 << i)

def main():
    print("Count of set bits in 5:", count_set_bits(5))
    print("Is 16 a power of two?", is_power_of_two(16))
    a, b = 5, 10
    print("Before swap:", a, b)
    a, b = swap(a, b)
    print("After swap:", a, b)
    print("Toggle 1st bit of 5:", toggle_ith_bit(5, 1))
    print("Clear 2nd bit of 5:", clear_ith_bit(5, 2))
    print("Set 0th bit of 5:", set_ith_bit(5, 0))

if __name__ == "__main__":
    main()