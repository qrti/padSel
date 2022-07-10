# **padSel**
### **Column Helper for vsCode**

<br>

**Because vsCodes lack of a real column edit function some typework is necessary to pretty up comments**  
This easy to adapt Python script may save some typework

- select some code lines, be careful to select complete lines
- the line in the selction with the right most comment is used as position template  
  if no existing comments are found a default position is used  
  already commented or longer lines are ignored
- press your binded key or run multiCommand.padSel (with command palette)
- the selection will be processed and replaced

See script for adding programming languages

<br>

<img src="image/padSel.gif" width=480>

<br>

### **settings.json**
``` 
{
    "multiCommand.commands": [
        {
            "command": "multiCommand.padSel",
            "interval": 250,                                    // higher for slow machines
            "sequence": [
                "editor.action.clipboardCopyAction",
                {
                    "command": "command-runner.run",
                    "args": {
                        "command": "padSel"
                    }
                },
                "workbench.action.focusActiveEditorGroup",
                "editor.action.clipboardPasteAction"
            ]
        }
    ],

    "command-runner.terminal.name": "runCommand",
    "command-runner.terminal.autoClear": true,
    "command-runner.terminal.autoFocus": false,                 // if true, interval in multiCommand may be higher
    "command-runner.commands": {
        "padSel": "..\\python.exe ..\\padSel.py ${fileExtname}" // adapt your paths to python.exe and padSel.py
    }
}
```

### **optional keybindings.json**
```
[
    {
        "key": "ctrl+alt+p",
        "command": "multiCommand.padSel",
        "when": "editorTextFocus"
    }
]
```

### **prequisites**
https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command  
https://marketplace.visualstudio.com/items?itemName=edonet.vscode-command-runner  
https://www.python.org/


<br>

#### V0.5 220710
---

#### contact
[qrt@qland.de](mailto:qrt@qland.de)
