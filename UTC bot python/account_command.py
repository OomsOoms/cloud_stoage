def account_command(user):
    user = str(user)
    print(user, type(user))
    from googleapiclient.discovery import build
    from google.oauth2 import service_account

    spreadsheet_id = "1s06YPtUzSK9ql3HS4p5OW42zHhuWf7kVNRFs5QTMSLQ"

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
                                range="accounts!a2:o").execute()
    # usable data
    values = result.get('values', [])



    compare_num = 0
    for x in range(len(values)):
        print(user, str(values[compare_num][1]))
        if user == str(values[compare_num][1]):
            print(f"Match: {user, values[compare_num][1]}")
            print(values[compare_num])
            message = f"{user} past results\n\nCompetition: **UTC {values[compare_num-1][2]}**\nBest single: **{values[compare_num][3]}**\n\nCompetition: **UTC {values[compare_num-1][4]}**\nBest average: **{values[compare_num][5]}**\n\nIf there is a mistake please DM Ooms"
            return message


            
        compare_num += 1

        if compare_num == (len(values)):
            compare_num = 0

       

