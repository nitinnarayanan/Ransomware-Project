import os
import rsa
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA

Fls=[]

for fls in os.listdir():
	if os.path.isfile(fls):
   		if fls.endswith(".txt"):       
      			Fls.append(fls)

pvKey="""
-----BEGIN RSA PRIVATE KEY-----
MIIG7gIBAAKCAYEApTyPqTs2QLaktSMabc7Ao7I6v7TQPYqRUs2Z47kHJEnW50gN
pCnOL5+LheVNBeK4LsgWA5J7WqWzhZis/ZSZRGELSW7Ma2kIQY8o/xofEp7cBlVC
4DuVGoqA5AR/rPNbgNhpiArXMd276UeR2NjX46iSKZ773LCNSbn83KD25NaBdUlX
66lnR2jXwcuk4jsDwhtNxxT9pDB3W8e08gHeo0TEC+vD6szW5VS4DqV+p0WO1pDK
aiClDAUttA0/4WnLp6F83wxqtZUdPRim9wrlz8+4ivawkEI1IF5xtKokWAtYNSxF
H+Hn7gsPT6psKRb6BWB7/IFN9t+AUaRnym8QC+pI//K4EK46jGHPyJEK4Eqch8Jd
Ww1i1q8pfRnAB89Y4/Kx5vMzAtQ9wTxRoUp3WOZBo43K1CSHj9h8oVtI4auyXF2T
Mb4OGXHp7MYgj6dWySGV9BCqsCpwjebI0U53Qk/z39A8IrP+29MGaOXv4L2eN1pl
jD3ckymiZP+hJEYZAgMBAAECggGASWGw51Y9jNXQJgWV6ihE0y4G+zZguMP+MAjR
DBoS+uG0B/iu3jYWtH2lZ+xinXeHlncTl7iJAcPPC0i3otJIkt6KNa14KUd2/C6I
5WoDXLCiREm/LngniqbyANGipftZqsnxbBJsaV/w4PQA6I28qwUlDEjnz6W0yYZI
ru7pVs2QprbQzf7ouATutMksy6+rxpt7mitPTYicqWzyhfuglV+ntSeaVX9s/GH4
b8C9k6nHerDIdzwxV82WaXD2NhoH9DQqHYybwWYVd0vhvKl0xDnhDIJvMeHr1eOF
6vZpEiWUwpEXBrXAmjG2QaDxtObcsW4ONLFvRb7nVUfVCpZd/zDuX6zInUkshAYn
ovgkTVeaCxh4fVXndMBFW+xbIIKGfi4BR4rL6fWreGO7Al3rj0mnIR/BpzLLoiaQ
4sUjmC2OzZE7yWR1gI0uF3f/fy9pYV9CJ011epMzQD2PYwj7TRpEleQ8kZ5yD011
1Bml4mqkfzHuWU01wcQLuIS9/toBAoHNAKzhosBVYE4SFxpYkG5X1pcgz7yzG985
n5ekennxAJftPr6btfTVqawoROBDYh3qRUZ+jFnukNuB1Qk9BpyHDGnbggzLljsS
OZX1P5SN3ho2dk8fvXu/XebDQPS+JO532dM46+OelRd0wh+3nRVbTskXON/06mUP
ID+X1+dF7piloS+r4O1gb2ty9Zu625YfbdTeNd7EyPCk39Db/LG2k0AgWz4futwJ
nFx+LHG92Cfbw3gm2g2MCMq/Ms+d8z1/sza8INecXCD6KvW2WQKBtQD0rf7H/TGA
yOdxC7Y5aSvTTsu3cF2HBs7DDIO/ycZdXfW91d+HVCy+uevnI3Jt5we4TYOK5+C6
hUEqiR23qOUmLNMHOtAc7HAugXhKGduz0JMDXxEp18AXck9TOei/EvXi6qS+8F7o
9xLKoc7C42c9pcYFBuGZ0K4LByLaJ5YV7VB6sJKdY5vU71g/7TFZpzTOmOlLrgCX
UwfBrxthAxYgZzqiYXX06oYvp16qRRwlkQBklcECgcxrsMIo/QXYm/w4NSMDGURb
L903tnqOOt7nH1YLz8yG1wpWwbg+oznmO89rw43DBMPSfdH/01P46I9ECfesWZOp
/UqtncQfV+L3PqY0a4sG2RYpg6QNCc/8h3RXAHsQ8SeHI9YNHCPTUK/8Aeyf+RjC
uux61Z2NBjcYZgXf0vglrkcR4wdh1siRLjNAps1SXpGUIDd+ZSamgI3LFL38Fbb0
IzOzJyDHIFV+aDpXP+L+MS86ETmTZr+zTBbirYlvrbR9TANJS+U3xZ4tIUECgbRW
T2JGjav+r9/kYqs/CThqa6s05DA5x078QtfeuYB9wv1Cn8Uf6bN2/AKZIEnnNs3k
V4OFZlJBuWvJY2DWPn/GvZ0bOcXbzhOsdANIsGJtxa92Svy08+RQ4QPWaeEONdQC
3Z6LtCLmrvE0BWv4F1t9xZJah5jhN1mNjlDe/4PT7EitXsf5OP/pVxycQEFeTLs1
/X6eMZ0HxERCMFDKIdqWR5PJX/PKF0iKWtHr4kERh1rKIIECgcw60tM9MwJ6Z29G
cFkTObOIKIRwaibE+ZJEtSwtlj0OSc9KsMs2wwUC068a6SseE2amSmpYg0x1e5zn
/K+reLgOHGbu9/KWeFbX6Lqntsh9NN2XMz8vwhAs1zCIQcRtLshi5ZNK4utso99W
gLIj0ED9em9rnwBQ3fAkZSXwaQOCavCBPeMUKQB2MaLMxkV1ayTNe4xrTjiMjGRb
n1ww+oUxRqBcWPmC9VvUXxNh4sgqkcwlzCGUs+Hq8wqBut1Y7DQ7t7n7La6JlXG4
IMw=
-----END RSA PRIVATE KEY-----

"""
pbkey = rsa.PrivateKey.load_pkcs1(pvKey)


for fls in Fls:
    with open(fls, "rb") as thefls: 
        content = thefls.read() 
        charesDecrypted = rsa.decrypt(content, pbkey)

    with open(fls, "wb") as thefls:
        thefls.write(charesDecrypted)
        thefls.close()
        print("File Decrypted !!")

