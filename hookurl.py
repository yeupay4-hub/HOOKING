import os
import site
import sys
hinhnen = """
⠤⣤⣤⣤⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⠤⠤⠴⠶⠶⠶⠶
⢠⣤⣤⡄⣤⣤⣤⠄⣀⠉⣉⣙⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠘⣉⢡⣤⡤⠐⣶⡆⢶⠀⣶⣶⡦
⣄⢻⣿⣧⠻⠇⠋⠀⠋⠀⢘⣿⢳⣦⣌⠳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⣡⣴⣧⠻⣄⢸⣿⣿⡟⢁⡻⣸⣿⡿⠁
⠈⠃⠙⢿⣧⣙⠶⣿⣿⡷⢘⣡⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣷⣝⡳⠶⠶⠾⣛⣵⡿⠋⠀⠀
⠀⠀⠀⠀⠉⠻⣿⣶⠂⠘⠛⠛⠛⢛⡛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠀⠉⠒⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⡁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀ ⠀⠀⠀⠿
"""
print(hinhnen)
print("\n-> Author: Anhnguyencoder")
print("[INFO] https://www.facebook.com/anhnguyencoder.izumkonata\n")
print(f"[INFO] Python version: {sys.version.split()[0]}")
if sys.version_info < (3, 7):
    print("[!] Python quá cũ, nên dùng 3.8+ trở lên.")
print()

HOOK_CODE = r'''
def request_logger():
    import os, datetime
    LOG_FILE = os.path.join(os.getcwd(), "bug.txt")
    def write_log(t):
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(t + "\n")
        except:
            pass
    write_log("\n===== BYPASS ANTI-HOOK =====\n" + str(datetime.datetime.now()))
    try:
        import requests.sessions
        _old_req = requests.sessions.Session.request
        def new_req(self, method, url, *args, **kwargs):
            msg = f"[Url] {method} {url}"
            print(msg)
            write_log(msg)
            return _old_req(self, method, url, *args, **kwargs)
        requests.sessions.Session.request = new_req
    except:
        pass
    try:
        import urllib3.connectionpool
        _old_urlopen = urllib3.connectionpool.HTTPConnectionPool.urlopen
        def new_urlopen(self, method, url, *args, **kwargs):
            scheme = "https" if self.scheme == "https" else "http"
            msg = f"[Urllib3] {method} {scheme}://{self.host}{url}"
            print(msg)
            write_log(msg)
            return _old_urlopen(self, method, url, *args, **kwargs)
        urllib3.connectionpool.HTTPConnectionPool.urlopen = new_urlopen
    except:
        pass
request_logger()
'''

def get_sitecustomize_path():
    user_site = site.getusersitepackages()
    os.makedirs(user_site, exist_ok=True)
    return os.path.join(user_site, "sitecustomize.py")

def tai_hook():
    path = get_sitecustomize_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(HOOK_CODE)
    print(f"[+] Hook installed at: {path}")

def xoa_hook():
    path = get_sitecustomize_path()
    if os.path.exists(path):
        os.remove(path)
        print("[+] Hook removed.")
    else:
        print("[!] No hook found.")

if __name__ == "__main__":
    print("1. Install hook")
    print("2. Remove hook")
    choice = input(">> ")

    if choice == "1":
        tai_hook()
    elif choice == "2":
        xoa_hook()
    else:
        print("Chọn sai rồi nhóc!")