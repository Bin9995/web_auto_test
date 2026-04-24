import os
from faker import Faker

PATH = os.path.dirname(__file__)
BASE_URL = "http://121.43.169.97:8081"
BACK_URL = "http://121.43.169.97:8082"

fk = Faker(locale='zh_CN')
NAME = fk.name()
PHONE = fk.phone_number()
CARD = fk.ssn()
print(NAME, PHONE, CARD)
