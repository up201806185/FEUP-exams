# FEUP-exams
A scraper written in python, that returns all (or some of) the exams from a given course ID.
This script saves the html of the page as a '.txt' and will use it as a cache. You can disable this feature by changing line 9 of FEUP_exams.py to 'CACHE_ENABLED = False'
Feel free to use this script:)


#Usage

```py
from FEUP_exams import FEUP_exams, COURSES_IDS
from pprint import pprint

pprint(FEUP_exams(COURSES_IDS["MIEIC"], [])) #If the second argument is an empty list, 
#the function will output all the exams it finds.

#Output
[{'Week_day': 'Terça',
  'hours': ('17:00', '20:00'),
  'rooms': ('B213',),
  'timestamp': datetime.datetime(2019, 1, 29, 17, 0),
  'unit_initials': 'PLOG',
  'unit_name': 'Programação em Lógica',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=42235'},
 {'Week_day': 'Quarta',
  'hours': ('13:30', '16:30'),
  'rooms': ('B104', 'B201'),
  'timestamp': datetime.datetime(2019, 1, 30, 13, 30),
  'unit_initials': 'AOCO',
  'unit_name': 'Arquitectura e Organização de Computadores',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=40968'},
 {'Week_day': 'Sexta',
  'hours': ('09:00', '12:00'),
  'rooms': ('B213', 'B208'),
  'timestamp': datetime.datetime(2019, 2, 1, 9, 0),
  'unit_initials': 'LCOM',
  'unit_name': 'Laboratório de Computadores',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=42423'},
 {'Week_day': 'Sexta',
  'hours': ('13:30', '16:30'),
  'rooms': ('B104', 'B207', 'B208', 'B213'),
  'timestamp': datetime.datetime(2019, 2, 1, 13, 30),
  'unit_initials': 'MDIS',
  'unit_name': 'Matemática Discreta',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=40979'},
 {'Week_day': 'Terça',
  'hours': ('09:00', '12:00'),
  'rooms': ('B219',),
  'timestamp': datetime.datetime(2019, 1, 29, 9, 0),
  'unit_initials': 'TVVS',
  'unit_name': 'Teste, Verificação e Validação de Software',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=41915'},
  etc,etc,etc...]
```