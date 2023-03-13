from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.number import inverse
from math import gcd
import pyzipper
from tqdm import tqdm


p = 246325257494661642969237737341065048697
q = 290462691516423784421384996389947025379

n = p * q

assert n == 71548297280375560625291316608808454643552780385705940508145978735138929881163

c = 56645162280378610220851948686510890667443804414543658362818899623322581491486

phi = (p-1) * (q-1)

zip_file = "vault.zip"
for x in tqdm(range(48000000, 2, -1)):
    try:
        assert gcd(phi, x) == 1

        d = inverse(x, phi)

        m = pow(c, d, n)
        try:
            with pyzipper.AESZipFile('vault.zip', 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
                zf.extractall(pwd=str(m).encode())
                print("Zip file extracted successfully!")
                print(f"{x} - {m}")
                exit()
        except RuntimeError as e:
            if "Bad password" not in str(e):
                print(e)
            pass
    except Exception as e:
        if type(e) is not AssertionError:
            print(e)
            print(x, m)
