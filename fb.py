#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import yaml
import ast
import fitbit
import pprint as p

if len(sys.argv) != 3:
    print('usage: fb.py [conf_file] [date]')
    sys.exit(1)

with open(sys.argv[1]) as file:
    conf = yaml.safe_load(file)

tokens = ast.literal_eval(open('.tk').read())
at = tokens['access_token']
rt = tokens['refresh_token']

#自動更新時のコールバックで再保存
def update(token):
    f = open('.tk', 'w')
    f.write(str(token))
    f.close()
    return

client = fitbit.Fitbit(conf['ci'],conf['cs'],
        access_token=at,refresh_token=rt,refresh_cb=update)

# Ex.歩数取得 '1sec','1min',or'15min'
#p.pprint(client.intraday_time_series('activities/steps','2019-11-02',detail_level='15min'))

p.pprint(client.activities(date=sys.argv[2]))
p.pprint(client.sleep(date=sys.argv[2]))

