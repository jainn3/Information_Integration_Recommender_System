import csv
import random
user_prod = {}

csvwriter = csv.writer(open('user-prod.csv','wb'))
csvwriter.writerow(['user_id','product_id','rating'])

for i in range(1,999):
    n = random.randint(1,8)
    listofprod = random.sample(range(1,30575),n)
    for prod in listofprod:
        csvwriter.writerow([i,prod, random.randint(1,5)])