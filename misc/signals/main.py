signals = [
    "01101000",
    "11101000",
    "01101000",
    "11111100",  # Should be 123 => 1111011
    "00101110",
    "00110110",
    "11001100",
    "01101100",
    "10100110",
    "11100100",
    "01111110",
    "01110110",
    "10001100",
    "01101100",
    "11111010",
    "10001100",
    "11101100",
    "11111010",
    "01100110",
    "10101010",
    "01110110",
    "00001100",
    "10111110"
]

# string = ""
# for sig in signals:
#     # print(sig[::-1])
#     # print(int(sig[::-1], 2))
#     string += chr(int(sig[::-1], 2))
# print()
# print(string)

# Move bits to be in this order
# 0, 5, 2, 7, 4, 1, 6, 3
string = ""
for sig in signals:
    byte = ""
    for index in [0, 5, 2, 7, 4, 1, 6, 3]:
        byte += sig[::-1][index]
    print(byte)
    string += chr(int(byte, 2))

print(string)
