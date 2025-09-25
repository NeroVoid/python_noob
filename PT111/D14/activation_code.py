username = input("Please enter your username: ").strip()

from datetime import date
today = date.today().strftime("%Y-%m-%d")

import base64
activation_string = f"{username}:{today}"
activation_bytes = activation_string.encode("utf-8")
activation_code = base64.b64encode(activation_bytes).decode("utf-8")
print("Activation code:", activation_code)

decoded_bytes = base64.b64decode(activation_code)
decoded_string = decoded_bytes.decode("utf-8")
print("Decoded string:", decoded_string)    
