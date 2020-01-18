import openpyxl
from os import listdir

def xlsx_to_csv(namefile):
    name = (namefile.split("/")[-1]).split(".xlsx")[0]

    xlsx = openpyxl.load_workbook(namefile)
    sheet = xlsx.active
    data = sheet.rows

    with open("./"+name+".csv", "w") as fw:
        for row in data:
            l = list(row)
            line = ''
            for i in range(len(l)):
                if i == len(l)-1:
                    line += str(l[i].value)
                else:
                    line += str(l[i].value) + ","
            if not ("None" in line):
                fw.write(line+"\n")
    print(name+".csv has been created")

for fl in listdir("./"):
    if "xlsx" in fl:
        xlsx_to_csv(fl)
