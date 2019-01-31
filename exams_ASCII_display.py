import texttable

int_to_week_day = {
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday"
}

def print_exams_list(exams_list, language = "EN"):
    assert type(exams_list) == list
    assert language == "EN" or language == "PT"

    exams_list.sort(key = lambda item: item["timestamp"])

    if language == "EN":
        table_list = [["day", "week day", "unit", "start - finish", "exam rooms"]]
    else:
        table_list = [["dia", "dia da semana", "unidade", "início - fim", "salas de exame"]]
    
    for exam in exams_list:

        day = exam["timestamp"].date().__str__()

        if language == "EN":
            weekday_str = int_to_week_day[ exam["timestamp"].weekday() ]
        else:
            weekday_str = exam["Week_day"]
        
        unit_initials = exam["unit_initials"]

        start_finish = " - ".join(exam["hours"])

        rooms = " ".join(exam["rooms"])

        table_list.append([day, weekday_str, unit_initials, start_finish, rooms])
    
    table = texttable.Texttable()
    table.set_deco(texttable.Texttable.HEADER)
    table.set_cols_dtype(["t", "t", "t", "t", "t"])
    table.set_cols_align(["l", "l", "l", "l", "l"])
    table.add_rows(table_list)

    print(table.draw())
    print()


def personal_use():
    from FEUP_exams import FEUP_exams, COURSES_IDS
    from datetime import datetime

    print_exams_list(
        FEUP_exams(
            COURSES_IDS["MIEIC"],
            ["MDIS", "AOCO", "FPRO", "ALGE", "AMAT"]
            ),
    "PT"
    )

    input()
    
if __name__ == "__main__":#My personal use
    personal_use()
