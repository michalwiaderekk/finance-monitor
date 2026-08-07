import pdfplumber
import re
import pandas as pd
import csv

with pdfplumber.open('C:\\Users\\rwiad\\Desktop\\finance-monitor\\data\\wyciag.pdf') as pdf:
    data = []
    account_number = []
    for page in pdf.pages:
        text = page.extract_text()
        if re.findall(r"\d{2} \d{4} \d{4} \d{4} \d{4} \d{4} \d{4}", text) != []:
            account_number = re.findall(r"\d{2} \d{4} \d{4} \d{4} \d{4} \d{4} \d{4}", text)
        raw_data = re.findall(r"(^\d{4}-\d{2}-\d{2}) (.*) (-?\d+\.\d{2}) (\d+\.\d{2})",text, re.MULTILINE)
        for row in raw_data:
            acc = (account_number[0],)
            new_row = row + acc
            data.append(new_row)
    #print(data)
    sum = 0.0
    for row in data:
        if row[4] == '21 1160 2202 0000 0003 6355 9336':
            continue
        elif float(row[2]) < 0.0:
            sum += float(row[2])
            print(f'{sum} += {row[2]}')
    print(sum)