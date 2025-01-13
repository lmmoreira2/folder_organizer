import os
import time

here = os.getcwd()
print(here)

list = os.listdir('.')

print(list)

# Check if log file exists

if not os.path.exists('log/log.txt'):

    # Create log file
    os.makedirs('log')

    log = open('log/log.txt', 'w')
    log.write('Log file created at ' + time.ctime() + '\n\n\n' )
    log.close()



log = open('log/log.txt', 'a')
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