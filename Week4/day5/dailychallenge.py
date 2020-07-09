def integernumber(n, bit_size):
    bin_number = bin(n)
    reverse_number = bin_number[-1:1:-1]
    reverse_number = reverse_number + (bit_size - len(reverse_number))*'0'
    print("Reverse Bits ::>", int(reverse_number, 2))
    print(bin(int(reverse_number, 2)))


# Driver program
if __name__ == "__main__":
    n = int(input("Enter Number ::>"))
    bit_size = int(input("Enter Bit Size ::>"))
    integernumber(n, bit_size)
