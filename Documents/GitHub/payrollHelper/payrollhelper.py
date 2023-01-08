import pandas as pd

file = "testFile.xlsx"

def createFile(spreadsheet, lessonType):
    totalPay = 0
    for index, row in spreadsheet.iterrows():
        if row["Paid"] == "No":
            totalPay += row["Commission"]
    spreadsheet.loc[len(spreadsheet.index), "Package"] = "Total"
    spreadsheet.loc[len(spreadsheet.index) - 1, "Total revenue"] = str(totalPay)
    spreadsheet.to_excel(lessonType)

def sortCoachActivity(spreadsheet):
        spreadsheet = spreadsheet[spreadsheet.Status != "cancel_on_time"]
        privateLessons = spreadsheet.loc[spreadsheet["Type"] == "Lesson"]
        clinics = spreadsheet.loc[spreadsheet["Type"] != "Lesson"]
        createFile(privateLessons, "private.xlsx")
        createFile(clinics, "clinics.xlsx")
        
        

def sortData(spreadsheet):
    spreadsheet = pd.ExcelFile(spreadsheet)
    
    sheets = list(spreadsheet.sheet_names)
    coaches = []
    for sheet in sheets:
        df = spreadsheet.parse(sheet, header=1)
        df = df.sort_values("Teacher") #look at later
        currName = None
        for index, row in df.iterrows():
            if row["Teacher"] != currName:
                currName = row["Teacher"]
                teacherInfo = df.loc[df["Teacher"] == currName]
                sortCoachActivity(teacherInfo)
                break
                # make new spreadsheet for this new teacher

       
    # group by teacher name, in a new excel sheet

    return None


    
            

sortData(file)  







# NextSteps
# 1. Calculate the pay of each person.
# 2. Do the same thing for office workers/stringer
# 3. Revert the dataframe back into the excel sheet

