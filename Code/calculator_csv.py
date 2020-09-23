import csv
import json
import sys
def calculator(income):
    start_point = 5000
    social_insurance_point = 0.08+0.02+0.005+0.06
    tax_part = income*(1-social_insurance_point)-start_point
    if tax_part <=0:
        tax = 0
    elif tax_part <= 3000:
        tax = tax_part*0.03
    elif tax_part <= 12000:
        tax = tax_part*0.1-210
    elif tax_part <=25000:
        tax = tax_part*0.2-1410
    elif tax_part <=35000:
        tax = tax_part*0.25-2660
    elif tax_part <=55000:
        tax = tax_part *0.3 -4410
    elif tax_part <=800000:
        tax = tax_part*0.35-7160
    else:
        tax = tax_part*0.45-15160
    salary = income*(1-social_insurance_point)-tax
    return '{:.2f}'.format(salary)

def output(data):
    '''
    将字典存入文件
    '''
    json_str=json.dumps(data)
    link = sys.argv[2]
    with open((link),'w') as f2:
     f2.write(json_str)

def main():
    '''
     main()函数
    '''
    data_file = sys.argv[1]
    data= {}
        
    usr_csv = csv.reader(open(data_file))
    data_list = list(usr_csv)
    print(data_list)
    for item in data_list:
        id, income = item[0],float(item[1])
        income = calculator(income)
        data[id] = income
    output(data)

if __name__ =='__main__': 
    main()  
    
