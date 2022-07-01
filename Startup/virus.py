import requests
check_for_update = "https://raw.github.com/OomsOoms/cloud_stoage/main/check_update.txt"

response = requests.get(check_for_update)
print(response.content)
open("update_v2.zip", "wb").write(response.content) 
