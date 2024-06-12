import pyautogui as p
import os
import argparse
import time

# parser = argparse.ArgumentParser(description='CTF Automation Tool')
# # parser.add_argument('-a',type=str,help='-a : Attacker\'s IP')
# parser.add_argument('-m',type=str,help='-m : machine\'s IP')
# parser.add_argument('-d',type=str,help='-d : domain name -- Example ~ machine.htb)')
# parser.add_argument('-p',type=str,help='-p : Platform Name Example : htb,thm,pg')
# parser.add_argument('-u',type=str,help='-u : username on platform')

# args=parser.parse_args()

# # attacker = args.a
# machine = args.m
# domain = args.d
# platform = args.p
# username = args.u
# attacker = input("Enter Machine's IP: ")

# function creation 
name = input("Enter CTF Machine Name: ")
machine = input("Enter Machine's IP: ")
domain = input("Enter domain Name (/etc/hosts): ")
platform = input("Enter Platform (htb,thb,pg): ")
username = input("Enter player's username: ")
hdir = os.getenv('HOME')
user = os.getenv('USER')    

# creation of directory
os.chdir(hdir)
if os.path.exists(f'{hdir}/CTF'):
    if os.path.exists(f'{hdir}/CTF/HTB'):
       print("[*]HTB Already exist")
    else:
        os.mkdir(f'{hdir}/CTF/HTB')
        print("[*]HTB Created Successfully.")
    if os.path.exists(f'{hdir}/CTF/THM'):
       print("[*]THM Already exist")
    else:
        os.mkdir(f'{hdir}/CTF/THM')
        print("[*]THM Created Successfully.")
    if os.path.exists(f'{hdir}/CTF/PG'):
       print("[*]PG Already exist")
    else:
        os.mkdir(f'{hdir}/CTF/PG')
        print("[*]PG Created Successfully.")
else:
    os.mkdir(f'{hdir}/CTF/')
    print("[*]~/CTF Created Successfully.")
    os.mkdir(f'{hdir}/CTF/HTB')
    print("[*]HTB Created Successfully.")
    os.mkdir(f'{hdir}/CTF/THM')
    print("[*]THM Created Successfully.")
    os.mkdir(f'{hdir}/CTF/PG')
    print("[*]PG Created Successfully.")

# machine based dir creation
if platform == 'htb' or platform == 'HTB':
    if os.path.exists(f'{hdir}/CTF/HTB/{name}'):
        pass
    else:
        os.mkdir(f'{hdir}/CTF/HTB/{name}')
elif platform == 'thm' or platform == 'THM':
    if os.path.exists(f'{hdir}/CTF/THM/{name}'):
        pass
    else:
        os.mkdir(f'{hdir}/CTF/THM/{name}')
elif platform == 'pg' or platform == 'PG':
    if os.path.exists(f'{hdir}/CTF/PG/{name}'):
        pass
    else:
        os.mkdir(f'{hdir}/CTF/PG/{name}')
else:
    print("Please check you platform name , it must be {htb,thm or pg} ")
    
# configuration of IP's
os.system(f'echo \'{machine}  {domain}\' | sudo tee -a /etc/hosts')
os.system(f'echo \'{machine}\' | sudo tee -a /etc/target')
# os.system(f'echo \"export aip=$\'{attacker}\'\" | tee -a /home/{user}/.zshrc')
os.system(f'echo \"export mip=$\'{machine}\'\" | tee -a /home/{user}/.zshrc')

#vpn connection
if platform == 'htb':
    p.hotkey('ctrl','s')
    p.write('vpn')
    p.press('enter')
    os.system(f'sudo gnome-terminal --title="VPN Connection" -- sudo openvpn /home/{user}/Downloads/lab_{username}.ovpn')
    p.hotkey('alt','tab')
    p.hotkey('ctrl','v')
    # p.hotkey('alt','space')
    # p.hotkey('n')
    # time.sleep(3)
    # os.system(f'ping {machine} -c 1')
    # result = os.system(f'ping {machine} -c 1 | grep icmp')
    # if result == 0:
    #     print("Connection built successfully")
    #     os.system("echo 'Connection built successfully'")
    #     os.system(f"figlet 'Happy Hacking {user}'")
    # else:
    #     print("Connection failed")
        

# terminal split

