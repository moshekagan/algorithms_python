def bin_to_dec(bin, pos=-1):
    pass


print(bin_to_dec(0))            # 0
print(bin_to_dec(1))            # 1
print(bin_to_dec(10))           # 2
print(bin_to_dec(11))           # 3
print(bin_to_dec(100))          # 4
print(bin_to_dec(101))          # 5
print(bin_to_dec(10001))        # 7
print(bin_to_dec(10101111))     # 176

"""
0 -> 0
1 -> 1

pos: 10
     10 -> 2:
        1*2^1 + 0*2^0 = 1*2 + 1*0 = 2+0 = 2

pos: 10
     11 -> 3:
        1*2^1 + 1*2^0 = 1*2 + 1*1 = 2 + 1 = 3
    
110 -> 6:
    1*2^2 + 1*2^1 + 0*2^0
"""
