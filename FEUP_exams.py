from requests import get
from bs4 import BeautifulSoup
import re
import datetime
from time import time


LINK = "https://sigarra.up.pt/feup/pt/exa_geral.mapa_de_exames?p_curso_id="
CACHE_ENABLED = True
CACHE_TIMEOUT = 3600 #1 hour

COURSES_IDS = {
    "MIEIC"  : "742",
    "LCEEMG" : "738",
    "MIEC"   : "740",
    "MIEIG"  : "725",
    "MIEEC"  : "741",
    "MIEM"   : "743",
    "MIEMM"  : "744",
    "MIEQ"   : "745"
}

def FEUP_exams(course_id, filter_list = [], date_cutoff = None):
    assert type(course_id) == str, "The argument 'course_id' has to be a string"
    assert course_id in COURSES_IDS.values(), "The ID {0} is not valid.".format(course_id)

    assert type(filter_list) == list or\
           type(filter_list) == tuple or\
           type(filter_list) == set,\
           "The argument 'filter_list' has to be either a list, a tuple or a set"
    
    assert date_cutoff == None or type(date_cutoff) == datetime.datetime
    
    html = get_html(course_id, LINK)

    soup = BeautifulSoup(html, 'html.parser')
    weeks = soup.find_all('table', {'class': "dados "}) + soup.find_all('table', {'class': "dadossz"})

    exams_list = []
    
    for week in weeks:
        for day, exam_day in zip(days_of_the_week(week), exams_of_the_week(week)):
            for exam in exam_day:
                exam["Week_day"] = day[0]

                timestamp = datetime.datetime(*list(map(int, day[1].split("-") + exam["hours"][0].split(":"))))
                exam["timestamp"] = timestamp

                exams_list.append(exam)
    
    def filter_key(item):
        if date_cutoff != None:
            if item["timestamp"] > date_cutoff:
                return False
        
        if filter_list == []:
            return True

        if item["unit_initials"] not in filter_list:
            return False
        
        return True

    return list(filter(filter_key, exams_list))
    
def days_of_the_week(week):
    """Returns [('Segunda', '2019-01-28'), ('Terça', '2019-01-29'), ...]"""
    result = []
    days = week.find_all('th', {'width': "15%"})
    for day_html in days:
        temp = []

        temp.append(day_html.contents[0])

        temp.append(day_html.find("span", {"class":"exame-data"}).contents[0])
        
        temp = tuple(temp)
        result.append(temp)
    
    return result

def exams_of_the_week(week):
    """Returns [[{'hours': ('17:00', '20:00'),
   'rooms': ('B213',),
   'unit_initials': 'PLOG',
   'unit_name': 'Programação em Lógica',
   'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=42235' }],...]"""
    result = []
    days = week.find_all('td', {'class': "l k"})
    
    for day in days:
        exams = []

        exams_list = day.find_all('td', {'class': "l exame"})
        
        
        for exam_html in exams_list:
            exam_dict = {}
            links = exam_html.find_all('a')

            exam_link = links.pop(0)

            href = exam_link.get("href")
            exam_url = "https://sigarra.up.pt/feup/pt/" + href
            exam_dict["url"] = exam_url

            unit_name = exam_link.get("title")
            exam_dict["unit_name"] = unit_name

            unit_initials_html = exam_link.find("b")
            unit_initials = unit_initials_html.contents[0]
            exam_dict["unit_initials"] = unit_initials

            rooms_list = []
            for exam_room_html in links:
                rooms_list.append(exam_room_html.string)
            rooms_list.sort()
            exam_dict["rooms"] = tuple(rooms_list)

            match_object = re.search(r"[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9]", exam_html.text)
            time = match_object[0].split("-")
            exam_dict["hours"] = tuple(time)

            exams.append(exam_dict)
        

        result.append(exams)
    
    return result

def get_html(course_id, url, force_refresh_cache = False):
    if not CACHE_ENABLED:
        return get(url + course_id).text
    
    try:
        txt = open(course_id + ".txt")
        cache_time = float(txt.readline())
        if time() - cache_time > CACHE_TIMEOUT or force_refresh_cache:
            txt.close() #The cache has to be refreshed (the cache is too old OR I want the cache to be refreshed)
        else:
            html = txt.read()
            txt.close()
            return html
    except FileNotFoundError:
        pass
    
    html = get(url + course_id).text

    with open(course_id + ".txt","w") as txt:
        txt.write(str(time()) + "\n")
        txt.write(html)
    
    return html

if __name__ == "__main__":
    print("Exams for MIEIC")
    from pprint import pprint
    pprint(FEUP_exams(COURSES_IDS["MIEIC"], []))