import requests

COMMON_PASSCODES_URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt"

def fetch_common_passwords(url):
    response = requests.get(url)
    if response.status_code == 200:
        return set(response.text.splitlines())
    else:
        raise Exception("Failed to fetch common passwords list")
    

def passcode_strength(passcode):
    try:
        common_passwords = fetch_common_passwords(COMMON_PASSCODES_URL)
    except Exception as e:
        return f"Error fetching common passwords list: {e}"

    if passcode in common_passwords:
        return "Unacceptable"

    length = len(passcode)

    if length < 8:
        return "Weak"
    elif length < 12:
        return "Strong"
    else:
        return "Very Strong"

if __name__ == "__main__":
    passcodes = ["cows", "toofew", "TheHippo", "TheCuriousHippo"]
    for p in passcodes:
        print(f"'{p}' is {passcode_strength(p)}")
