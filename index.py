import subprocess
import re

def get_wifi_ssid():
    ssid_command = subprocess.check_output("netsh wlan show profiles")

    ssids = []
    profiles = re.findall(r"All User Profile(.*)",ssid_command.decode("852"))
    for profile in profiles:
        prof = profile.strip().strip(":").strip()
        ssids.append(prof)
    return ssids

def get_password():

    ssids = get_wifi_ssid()

    wifi_s = []

    for ssid in ssids:
        try:
            network = subprocess.check_output("""netsh wlan show profile "{}" key=clear""".format(ssid))
        except: print("\nError to find '{}' network\n".format(ssid)); continue
        wifi = dict()
        wifi["ssid"] = ssid
        password = re.findall(r"Key Content(.*)", network.decode("852"))
        try:
            wifi["password"] = password[0].strip().strip(":").strip()
        except IndexError:
            wifi["password"] = "None"
        auth = re.findall(r"Authentication(.*)", network.decode("852"))
        authentication = "/".join([c.strip().strip(":").strip() for c in auth])
        wifi["authentication"] = authentication

        wifi_s.append(wifi)
    
    display_wifis(wifi_s)

def display_wifis(wifis):

    for wifi in wifis:
        print("_"*50)
        print()
        print(f"SSID : {wifi['ssid']}")
        print(f"Password : {wifi['password']}")
        print(f"Authentication : {wifi['authentication']}")
    print("_"*50)
    print("\n Kucyx Pozdrawia")
    
# print(command.decode("437"))
if __name__ == "__main__":
    from os import system
    system("cls")
    print("Windows Password Getter by. Kucyx Hewooo")
    from time import sleep
    sleep(2)
    wifis = get_password()