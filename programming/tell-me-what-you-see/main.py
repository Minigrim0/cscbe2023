from pwn import *

dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

def to_string(number):
    """Iterate through the number and return a string
    e.g.: 11 -> "two ones"

    Args:
        number (_type_): _description_
    """
    number = str(number)
    result = ""
    i = 0
    while i  < len(number):
        # Get the number of times the digit is repeated before changing
        count = 1
        while i + 1 < len(number) and number[i] == number[i + 1]:
            count += 1
            i += 1
        # Get the digit
        digit = number[i]
        # Get the word
        count = dict[str(count)]
        word = dict[digit]
        # Add the word to the result
        result += f"{count} {word}"
        # Add a space if it's not the last word
        if i + 1 < len(number):
            result += " "
        i += 1
    return result

conn = remote("54.194.215.82", 5000)
truc = conn.recvuntil(b"favourite number:")
print(truc)
conn.send(b"54\n")
truc = conn.recvuntil(b"see here: ")
print(truc)
while True:
    data = conn.recv().strip().decode()
    print(f"Data: {data}", end=" ")
    val = to_string(data)
    print(f"sending: {val}")
    conn.send(f"{val}\n".encode())
    # for x in range(10):
    stuff = conn.recvuntil(b": ")
    print(stuff)
