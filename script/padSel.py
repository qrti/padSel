# pad selection V0.5 qrt@qland.de 220711
# Column Helper for vsCode
#
# Because vsCodes lack of a real column edit function some typework is needed to pretty up comments
#
# - install multi-command and command-runner extensions in vsCode
# - add extension settings to settings.json and optionally to keybindings.json  
#   adapt paths for your system
# - Python has to be installed on your system
# 
# - select some code lines, be careful to select complete lines
# - the line in the selction with the right most comment is used as position template  
#   if no existing comments are found a default position is used  
#   already commented or longer lines are ignored
# - press your binded key or run multiCommand.padSel (with command palette)
# - the selection will be processed and replaced
#
# needed extensions
# https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command
# https://marketplace.visualstudio.com/items?itemName=edonet.vscode-command-runner

import sys
import pyperclip as clip
from operator import itemgetter

# extension: comment string dictonary
extD = { '.c': '//', '.cpp': '//', '.h': '//', '.py': '#', '.asm': ';' }

copDef = 64                                                     # comment position default

ext = sys.argv[1]                                               # file extension
cms = extD.get(ext, None)                                       # comment string for extension

if not cms:                                                     # extension not found
    print('error: extension not found')                         #
    exit(0)                                                     #

spl = clip.paste().splitlines()                                 # paste from clipboard and split lines
lines = [ [line.rstrip(), line.rfind(cms)] for line in spl ]    # [ [line, comment position] ]

cop = max(lines, key=itemgetter(1))[1]                          # comment position
                                                                #
if cop == -1:                                                   # 
    cop = copDef                                                #

for line in lines:                                              # pad lines
    if line[1]==-1 and len(line[0])<cop:                        #
        line[0] = ('{:<' + str(cop) + '}{}').format(line[0], cms)

nLines = '\n'.join([ line[0] for line in lines ]) + '\n'        # join lines
clip.copy(nLines)                                               # copy to clipboard
