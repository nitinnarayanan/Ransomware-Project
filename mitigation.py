import os
import re
import time


def detection():
    delete_list=[]
    gen_words = ["sha256","sha384","sha224","sha512","sha1","aes","des","crypt","encrypt","decrypt","hash","RSA","base64","hashlib","key","keys","pub","public","private","rsa","fernet","salt","attack","crack","cipher","cipher","PEKS","trapdoor","hexdigest","Fernet","secret","encode","decode","md5"]
    Fls=[]
    delete_list=[]
    for fls in os.listdir():
        if fls == "detection.py" or fls == "mitigation.py":
            continue
        if os.path.isfile(fls):
            Fls.append(fls)
    
    for d in Fls:
        f1 = open(d, "r", errors='ignore')
        lns=f1.readlines()
        
        for ln in lns:
            match = re.search('|'.join(gen_words), ln)      
            if (match):
                #print(d)
                delete_list.append(d)
                break
            
    if len(delete_list) >=1:
    	print(" \u2717 \u2717 \u2717 THE BELOW FILES MIGHT BE DANGEROUS \u2717 \u2717 \u2717 \n")
    	print('\n'.join(map(str, delete_list)))
    else:
    	print('\033[1m'+"No Malicious files detected  \u2713 \u2713 \u2713 \n\n"+'\033[0m')
    	exit()   
    	
    return delete_list         
    
def action_1(delete_list):
    time.sleep(1.25)
    print("\nNote: These file type might harm your computer. Suggested to take an action here:\n")
    print("[1] Detele all the above files immediately and restart the system\n[2] I understand the risks and choose to keep the files.\n")
    print("Choose your action: [1] or [2]")
    p=int(input())
    if p == 1:
        for d in delete_list:
            print(d+" is deleted Successfully")
            os.remove(d)
            time.sleep(1)
        print("All the possible malicious files listed above are deleted..!")
        time.sleep(2)
        print("Proceeding to restart")
        time.sleep(2)
        os.system("sudo reboot now")
        
    elif p==2:
        action_2()
    else: 
        print("Choose correct option")
        action_1(delete_list)

def action_2():
    print("\nImmediate shutdown is suggested. Would you like to proceed?\n")
    print("[1]Restart the computer immediately\n[2]Not Required\n")
    print("Choose your action: [1] or [2]")
    q=int(input())
    if q==1:
        print("Proceeding to restart...")
        test.sleep(1.5)
        os.system("sudo reboot now")
    elif q==2:
        print("Closing the Scan")
        exit()
    else:
        print("Choose correct option")
        action_2()
        

	
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

.-----------------------------------------------------------------------------.
| MITIGATION: Scanning for possible malicious files and taking action........ |
'-----------------------------------------------------------------------------'

"""
print(logo)
time.sleep(1)
var = detection()
action_1(var)
action_2()

