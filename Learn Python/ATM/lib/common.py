import os
import time

from conf.setting import LOG_PATH


def logger(msg):
    with open(LOG_PATH,
              mode='at', encoding='utf-8') as f:
        f.write('%s %s\n' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))
