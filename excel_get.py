from openpyxl import load_workbook

def get_xlsx():
    find = True
    lessons = ""
    lessons_dict = []
    wb = load_workbook("/driveone/excel/file.xlsx")
    sheet = wb["Лист1"]
    i = 0
    b = 0
    cord_a_value = ""
    while cord_a_value != "2-2 ис":
        i = i + 1
        cord_a_value = sheet["A" + str(i)].value
        if i > 150:
            find = False
            break
    if find:
        b = i
        while True:
            b = b + 1
            cord_a_value = sheet["A" + str(b)].value
            if str(cord_a_value) != "None":
                break
        for b in range(i, b):
            lesson = sheet["B" + str(b)].value
            lesson_name = sheet["C" + str(b)].value
            cab = sheet["D" + str(b)].value
            if cab == None:
                cab = ""
            message = lesson + " " + lesson_name + " " + cab + "\n"
            lessons = lessons + message
        return lessons
    else:
        return find