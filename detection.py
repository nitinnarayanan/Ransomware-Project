import os
import re
import time


def detection():
    gen_words = ["sha256","sha384","sha224","sha512","sha1","aes","des","crypt","encrypt","decrypt","hash","RSA","base64","hashlib","key","keys","pub","public","private","rsa","fernet","salt","attack","crack","cipher","cipher","PEKS","trapdoor","hexdigest","Fernet","secret","encode","decode","md5"]
    Fls=[] 
    for fls in os.listdir():
        if fls == "detection.py" or fls == "mitigation.py":
            continue
        if os.path.isfile(fls):
            Fls.append(fls)

    for d in Fls:
        virus=False
        f1 = open(d, "r", errors='ignore')
        lns=f1.readlines()
        time.sleep(1.20)
        
        for ln in lns:
            match = re.search('|'.join(gen_words), ln)      
            if (match):
                print("This file seems to be malicious: "+d+" \u2717 \u2717 \u2717")
                virus=True
                break

        if (virus==False):
            print("This file looks good: "+d+" \u2713 \u2713 \u2713")
        
        
prjct_grp_lg = """

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗     ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗             ███████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗            ██╔════╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝    █████   ███████╗
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝             ╚════██║
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║                 ███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝                 ╚══════╝
"""

print(prjct_grp_lg)
time.sleep(1)
logo = """

.----------------------------------------------------------.
| DETECTION: Scanning for possible malicious files........ |
'----------------------------------------------------------'

"""
print(logo)
time.sleep(1)
detection()

