def convert():
    binary = input('Enter Binary number: ')
    length = len(binary)
    decimal = 0
    decimal2 = 0
    for i in range(length):
        bit = int(binary[i])
        power = length-i-1
        decimal += bit*(2**i)
        if binary[i] == '.':
            for j in range(length):
                bit = int(binary[j])
                power2 = length + j + 1
                decimal2 += bit*(2**j)  
    print(f'The Binary number Converted into Decimal is : {decimal}.{decimal2}')
convert()