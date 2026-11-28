import hashlib
import requests

#this script elps you check if your password has been breached at some point or somehere.
password = input("what's the password?").strip() 


password_bytes = password.encode("utf-8")
hash_object = hashlib.sha1(password_bytes)
hash_text = hash_object.hexdigest().upper()


prefix = hash_text[:5]
suffix = hash_text[5:]

url = "https://api.pwnedpasswords.com/range/" + prefix
response = requests.get(url)
for line in response.text.splitlines():
    hash_ending, count  = line.split(":")
    if hash_ending == suffix:
        print(f"This password appeared in {count} known breaches. Don't use it.")
        break
else:
    print("Password not found in known breaches.")