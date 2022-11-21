import subprocess , os
os.system('cls' if os.name=='nt' else 'clear')
print('\n'*1)

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
print('--------------------+-------------------------+')
print("\033[33m{:<20}\033[0m|| \033[33m{:<}\033[0m{:>16}".format("Wi-Fi Name", "Password","|"))
print('====================+=========================+')
for i in profiles:
   try:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("\033[94m{:<20}\033[0m|  \033[92m{:<}\033[0m {:>13}".format(i, results[0],"|"))
        print('--------------------+-------------------------+')
    except IndexError:
        print ("\033[94m{:<20}\033[0m|  \033[92m{:<}\033[0m".format(i, ""))
   except subprocess.CalledProcessError:
        print ("\033[94m{:<30}\033[0m|  \033[92m{:<}\033[0m".format(i, "ENCODING ERROR"))

print('\n'*1)
input("Enter to close program >")