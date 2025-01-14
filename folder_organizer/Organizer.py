import os
import time

here = os.getcwd()
print(here)

list = os.listdir('.')

print(list)

# Check if log file exists

if not os.path.exists('log'):
    os.makedirs('log')


date = time.ctime().split(' ')

date = date[2] + date[1] + date[4]

log_path = 'log/log' + date + '.txt'

if not os.path.exists(log_path):

    log = open(log_path, 'w')
    log.write('Log file created at ' + time.ctime() + '\n\n\n' )
    log.close()



log = open(log_path, 'a')

# Counting userful files
number = 0
for files in list:
    if '.' in files and files != 'Organizer.py':
        number += 1

log.write('Organizing ' + str(number) + ' files at ' + time.ctime() + '\n')

for file in list:

    if file == 'Organizer.py':
        continue
    if '.' not in file:
        continue

    tipo = file.split('.')[-1]
    if not os.path.exists(tipo):
        os.makedirs(tipo)
    
    os.rename(file, tipo + '/' + file)

    log.write(file + ' moved to ' + tipo + ' at ' + time.ctime() + '\n')

log.write('\n\n')

log.close()

