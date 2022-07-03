def update_results(event_name):
    from googleapiclient.discovery import build
    from google.oauth2 import service_account
    from infomation import events_info

    results_sheet = events_info["results"][1].strip()

    for x in range(1,5):
        if event_name == events_info[f"event_{x}"][0]:
            break

    spreadsheet_id = events_info[f"event_{x}"][2].strip()

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
    write = []
    number_of_solves = []

    for x in range (len(values)):
        times = [] 
        total = []
        if len(values[entry_number]) == 12:
            video_proof = "No"
        else:
            video_proof = "Yes"
        
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
                total.append(f"'{mins_display}{sec}.{ms}")
                times.append(str(int(mins)*60+int(sec)+int(ms)/100))
                
                
            elif penalties == "+2":
                total.append(f"'{mins_display}{int(sec)+2}.{ms}+")
                
                times.append(str(int(mins)*60+int(sec)+2+int(ms)/100))
                
            else:
                times.append("-1")
                total.append("DNF")
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
                    average = f"' {sec:.2f}"

                else:
                    average = f"'{sec:.2f}"

            else:
                if float(sec) < 10:
                    average = f"{mins}:0{sec:.2f}"
                else:
                    average = f"'{mins}:{sec:.2f}"
            
            total.append(average)
            total.append(video_proof)
            
        write.append(total)
        write = (sorted(write, key=lambda x:x[6]))
        number = [entry_number]
        
        
        number_of_solves.append(number)
        
    request = sheet.values().update(spreadsheetId=results_sheet,range=f"{event_name}!b3", valueInputOption="USER_ENTERED", body={"values":write}).execute()
    request = sheet.values().update(spreadsheetId=results_sheet,range=f"{event_name}!a3:a", valueInputOption="USER_ENTERED", body={"values":number_of_solves}).execute()

    return write