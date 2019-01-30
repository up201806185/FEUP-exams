# FEUP-exams
A scraper written in python, that returns all (or some of) the exams from a given course ID.
This script saves the html of the page as a '.txt' and will use it as a cache. You can disable this feature by changing line 9 of FEUP_exams.py to 'CACHE_ENABLED = False'.
Feel free to use this script:)


### Usage

```py
from FEUP_exams import FEUP_exams, COURSES_IDS
from pprint import pprint

pprint(FEUP_exams(COURSES_IDS["MIEIC"])) #If the second argument is not specified, 
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

```py
from FEUP_exams import FEUP_exams, COURSES_IDS
from pprint import pprint

pprint(FEUP_exams(COURSES_IDS["MIEIC"], ["MDIS", "AOCO"]))#If you only want certain units,
# you can specify them as a list as the second argument

#Output
[{'Week_day': 'Quarta',
  'hours': ('13:30', '16:30'),
  'rooms': ('B104', 'B201'),
  'timestamp': datetime.datetime(2019, 1, 30, 13, 30),
  'unit_initials': 'AOCO',
  'unit_name': 'Arquitectura e Organização de Computadores',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=40968'},
 {'Week_day': 'Sexta',
  'hours': ('13:30', '16:30'),
  'rooms': ('B104', 'B207', 'B208', 'B213'),
  'timestamp': datetime.datetime(2019, 2, 1, 13, 30),
  'unit_initials': 'MDIS',
  'unit_name': 'Matemática Discreta',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=40979'}]
```

```py
from FEUP_exams import FEUP_exams, COURSES_IDS
from pprint import pprint
from datetime import datetime

pprint(FEUP_exams(COURSES_IDS["MIEIC"], ["MDIS", "AOCO"], datetime(2019, 2, 1)))
#You can also specify a cutoff date, after which no more tests are added to the output
#In this example, I'm excluding all the exams that are taken after 2019-Feb-1

#Output
[{'Week_day': 'Quarta',
  'hours': ('13:30', '16:30'),
  'rooms': ('B104', 'B201'),
  'timestamp': datetime.datetime(2019, 1, 30, 13, 30),
  'unit_initials': 'AOCO',
  'unit_name': 'Arquitectura e Organização de Computadores',
  'url': 'https://sigarra.up.pt/feup/pt/exa_geral.exame_view?p_exa_id=40968'}]
```

```py
from FEUP_exams import FEUP_exams, COURSES_IDS
from exams_ASCII_display import print_exams_list

exams_list = FEUP_exams(COURSES_IDS["MIEIC"])

print_exams_list(exams_list) #This function prints the exams as a nice-looking table

print_exams_list(exams_list, "PT") #You can have the table in portuguese if you wish (english is the default language)

# output
#    day       week day    unit    start - finish       exam rooms
# =====================================================================
# 2019-01-30   Wednesday   AOCO    13:30 - 16:30    B104 B201
# 2019-01-31   Thursday    CMOV    09:00 - 12:00    B216
# 2019-01-31   Thursday    ESOF    13:30 - 16:30    B338
# 2019-01-31   Thursday    SINF    17:00 - 20:00    B104
# 2019-02-01   Friday      LCOM    09:00 - 12:00    B213 B208
# 2019-02-01   Friday      MDIS    13:30 - 16:30    B104 B207 B208 B213
# 2019-02-01   Friday      APIN    17:00 - 20:00    B335
# 2019-02-04   Monday      LTW     13:30 - 16:30    B104
# 2019-02-04   Monday      ADAD    17:00 - 20:00    B335
# 2019-02-04   Monday      VCOM    17:00 - 20:00    B104
# 2019-02-05   Tuesday     SRSI    09:30 - 12:30    B115
# 2019-02-05   Tuesday     MNUM    13:30 - 16:30    B104 B207
# 2019-02-05   Tuesday     AIAD    17:00 - 20:00    B104
# 2019-02-05   Tuesday     RVAU    17:00 - 20:00    B111
# 2019-02-06   Wednesday   ECAC    09:00 - 12:00    B201
# 2019-02-06   Wednesday   GEMP    13:30 - 16:30    B229
# 2019-02-07   Thursday    TCOM    09:00 - 12:00    B221 B222
# 2019-02-07   Thursday    RCOM    13:30 - 16:30    B221 B223
# 2019-02-07   Thursday    IPCO    17:00 - 20:00    B104
# 2019-02-08   Friday      FISI2   13:30 - 16:30    B215 B217

#    dia       dia da semana   unidade   início - fim      salas de exame
# ==========================================================================
# 2019-01-30   Quarta          AOCO      13:30 - 16:30   B104 B201
# 2019-01-31   Quinta          CMOV      09:00 - 12:00   B216
# 2019-01-31   Quinta          ESOF      13:30 - 16:30   B338
# 2019-01-31   Quinta          SINF      17:00 - 20:00   B104
# 2019-02-01   Sexta           LCOM      09:00 - 12:00   B213 B208
# 2019-02-01   Sexta           MDIS      13:30 - 16:30   B104 B207 B208 B213
# 2019-02-01   Sexta           APIN      17:00 - 20:00   B335
# 2019-02-04   Segunda         LTW       13:30 - 16:30   B104
# 2019-02-04   Segunda         ADAD      17:00 - 20:00   B335
# 2019-02-04   Segunda         VCOM      17:00 - 20:00   B104
# 2019-02-05   Terça           SRSI      09:30 - 12:30   B115
# 2019-02-05   Terça           MNUM      13:30 - 16:30   B104 B207
# 2019-02-05   Terça           AIAD      17:00 - 20:00   B104
# 2019-02-05   Terça           RVAU      17:00 - 20:00   B111
# 2019-02-06   Quarta          ECAC      09:00 - 12:00   B201
# 2019-02-06   Quarta          GEMP      13:30 - 16:30   B229
# 2019-02-07   Quinta          TCOM      09:00 - 12:00   B221 B222
# 2019-02-07   Quinta          RCOM      13:30 - 16:30   B221 B223
# 2019-02-07   Quinta          IPCO      17:00 - 20:00   B104
# 2019-02-08   Sexta           FISI2     13:30 - 16:30   B215 B217

```