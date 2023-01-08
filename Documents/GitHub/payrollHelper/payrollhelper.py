from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("payrollhelper.html")

# this is the function that runs when the files are submitted
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        file = request.files["file"]
        
        if file:
            data = pd.read_excel(file, header=1)
            df = data.sort_values("Teacher")
            currName = None
            for index, row in df.iterrows():
                if row["Teacher"] != currName:
                    currName = row["Teacher"]
                    teacherInfo = df.loc[df["Teacher"] == currName]
                    # sortCoachActivity(teacherInfo)
            
            return df.to_html()
        
        return redirect("/")



# file = "testFile.xlsx"

# def createFile(spreadsheet, lessonType):
#     totalPay = 0
#     for index, row in spreadsheet.iterrows():
#         if row["Paid"] == "No":
#             totalPay += row["Commission"]
#     spreadsheet.loc[len(spreadsheet.index), "Package"] = "Total"
#     spreadsheet.loc[len(spreadsheet.index) - 1, "Total revenue"] = str(totalPay)
#     spreadsheet.to_excel(lessonType)

# def sortCoachActivity(spreadsheet):
#         spreadsheet = spreadsheet[spreadsheet.Status != "cancel_on_time"]
#         privateLessons = spreadsheet.loc[spreadsheet["Type"] == "Lesson"]
#         clinics = spreadsheet.loc[spreadsheet["Type"] != "Lesson"]
#         createFile(privateLessons, "private.xlsx")
#         createFile(clinics, "clinics.xlsx")
               
# def sortData(spreadsheet):
#     spreadsheet = pd.ExcelFile(spreadsheet)
#     sheets = list(spreadsheet.sheet_names)
#     coaches = []
#     for sheet in sheets:
#         df = spreadsheet.parse(sheet, header=1)
#         df = df.sort_values("Teacher") #look at later
#         currName = None
#         for index, row in df.iterrows():
#             if row["Teacher"] != currName:
#                 currName = row["Teacher"]
#                 teacherInfo = df.loc[df["Teacher"] == currName]
#                 sortCoachActivity(teacherInfo)
#                 break
#     return None


    
# sortData(file)  