import re
email = "jjashdjajsadhb@gmail.com"
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("true")
else:
    print ("false")