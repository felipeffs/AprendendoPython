from time import sleep
from emoji import emojize

for c in range(10, 0, -1):
    print('{}!!'.format(c))
    sleep(0.5)
print(emojize(':fireworks::sparkles::fireworks::sparkles::fireworks:' * 10, language='en'))
