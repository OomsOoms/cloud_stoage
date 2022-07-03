from googleapiclient.discovery import build
from google.oauth2 import service_account

#comp_num = input("Input spreadhseet comp numebr")
comp_num = "15.0"
#spreadsheet_id = input("Spreadsheet id")
spreadsheet_id = "1OBeQCqsvpxCIpjHmSVW29HNulKyt2beSHtLXlgg_3LE"

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
credentials = service_account.Credentials.from_service_account_file(
        "keys.json", scopes=SCOPES)

# The ID of the spreadsheet
service = build('sheets', 'v4', credentials=credentials)


# Call the Sheets API
sheet = service.spreadsheets()
# all the data
result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="Form responses 1!c2:o").execute()
# usable data
values = result.get('values', [])


# works out averages EVENT 1

entry_number = 0
new_accounts = []
number_of_solves = []
account = []

for x in range (len(values)):
    user = values[entry_number][1]
    account = []
    times = [] 
    total = []
    
    entry = values[entry_number]
    entry_number += 1
    
    
    name = entry[0]
    total.append(name)
    entry = entry[2:]
    
    for x in range(0, 10, 2):
        penalties = entry[x+1]

        mins, temp = entry[x].split(":")
        sec, ms = temp.split(".")
        if mins == "00":
            mins_display = ""

        else:
            if int(mins) < 10:
                mins_display = f"{mins[1]}:"
            else:
                mins_display = f"{mins}:"
            
        if penalties == "No Penalties":
            total.append(f"{mins_display}{sec}.{ms}")
            times.append(str(int(mins)*60+int(sec)+int(ms)/100))
            
            
        elif penalties == "+2":
            total.append(f"{mins_display}{int(sec)+2}.{ms}+")
            
            times.append(str(int(mins)*60+int(sec)+2+int(ms)/100))
            
        else:
            times.append("-1")
            total.append("DNF")
    new_best_single = max(times) 
    times.remove(max(times))
    times.remove(min(times))
    average = 0
    if min(times) == "-1":
        average = "DNF"
        total.append("DNF")
    else:
        for x in range(3):
            average += float(times[x])
        average /= 3

        mins = int(average/60)
        sec = float(average%60)

        if mins == 0:
            if float(sec) < 10:
                average = f"{sec:.2f}"

            else:
                average = f"{sec:.2f}"

        else:
            if float(sec) < 10:
                average = f"{mins}:0{sec:.2f}"
            else:
                average = f"{mins}:{sec:.2f}"
 
        account.append(name)
        account.append(user)
        account.append(comp_num)
        account.append(new_best_single)
        account.append(comp_num)
        account.append(average)
        new_accounts.append(account)

spreadsheet_id = "1s06YPtUzSK9ql3HS4p5OW42zHhuWf7kVNRFs5QTMSLQ"

result = sheet.values().get(spreadsheetId=spreadsheet_id,
                            range="accounts!a2:i").execute()
# usable data
old_accounts = result.get('values', [])

account_num = 0
compare_num = 0
for x in range(len(old_accounts)* len(new_accounts)):
    try:
        #print(new_accounts[account_num][1], old_accounts[compare_num][1])

        if new_accounts[account_num][1] == old_accounts[compare_num][1]:
            print(f"Match: {new_accounts[account_num][1], old_accounts[compare_num]}")

            # comparing singles
            #print("singhle", new_accounts[account_num][3], old_accounts[compare_num][3])
            if new_accounts[account_num][3] < old_accounts[compare_num][3]:
                new_accounts[account_num][3] = old_accounts[compare_num][3]
                new_accounts[account_num][2] = old_accounts[compare_num][2]

            #print(new_accounts[account_num][4], old_accounts[compare_num][4])
            if new_accounts[account_num][5] > old_accounts[compare_num][5]:
                new_accounts[account_num][5] = old_accounts[compare_num][5]
                new_accounts[account_num][4] = old_accounts[compare_num][4]
                #print(new_accounts[account_num][4], old_accounts[compare_num][4])

            
        compare_num += 1

        if compare_num == (min([len(old_accounts), len(new_accounts)])):
            account_num += 1
            compare_num = 0

        if compare_num == len(old_accounts)* len(new_accounts)-1:
            break

    except IndexError:
        break

spreadsheet_id = "1s06YPtUzSK9ql3HS4p5OW42zHhuWf7kVNRFs5QTMSLQ"

request = sheet.values().update(spreadsheetId=spreadsheet_id,range=f"accounts!a2", valueInputOption="USER_ENTERED", body={"values":new_accounts}).execute()