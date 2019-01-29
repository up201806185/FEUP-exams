from FEUP_exams import FEUP_exams, COURSES_IDS
from pprint import pprint

pprint(FEUP_exams(COURSES_IDS["MIEIC"], ["MDIS", "AOCO"]))#If you only want certain units, you can specify them as a list in the second argument

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