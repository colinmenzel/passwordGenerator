import secrets
import csv

secretsGenerator = secrets.SystemRandom()

num = []

for i in range(0, 30, 1):
    num.append(str(secretsGenerator.randrange(0,10,1)))
    print(num[i])

    with open('C:\\Users\\csmen\\Documents\\Pers-Project\\randTest.csv', 'w') as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(num)