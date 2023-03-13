with open("a.txt") as f:
    for line in f.readlines():
        print(line.split(":")[3])

# Save result to a file

command = 'bash -c "hashcat --status --hash-type 1000 --attack-mode 3 ./codes.txt ?a?a?a?a"'
