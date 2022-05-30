import os, json

default = [0, 85]

wks = json.loads(os.popen('i3-msg -t get_workspaces').read())
cur = [wk for wk in wks if wk['focused'] == True][0]

os.popen(f"i3-msg \"gaps left current set {default[cur['output'] == 'DP-1']}\"")