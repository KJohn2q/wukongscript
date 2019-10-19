import configparser
from src.question import get_question

cp = configparser.RawConfigParser()
cp.read("program.ini")

sec_list = cp.sections()

driver_path = cp.get('program_cfg', "driver_path")
usercookie = cp.get('program_cfg', "usercookie")

ques_list = get_question(usercookie)

print(ques_list)