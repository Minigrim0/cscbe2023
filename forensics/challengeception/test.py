# Pour trouver le drapeau : lisez la première lettre du recto, puis le premier caractère du verso, puis le deuxième du recto, et ainsi de suite. Répétez 4 fois.
string = list("Fenk xpaaowLi .lzm ei Agc iWPspneGhuTek8isah3tbh!Vg  pT:eee MkeSm{ d  #MNkEoCC DcZ}GaOcS")

for x in range(4):
    for i in range(len(string)):
        if i % 2 == 0:
            string[i] = string[i // 2]
        else:
            string[i] = string[(len(string) - ((i-1) // 2)) -1]
        print("".join(string))
