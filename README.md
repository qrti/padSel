# **padSel**
### **Column Helper for vsCode**

<br>

**Because vsCodes lack of a real column edit function some typework is needed to pretty up comments**  
This easy to adapt Python script may save some time

- install multi-command and command-runner extensions in vsCode
- add extension settings to [settings.json](#settingsjson) and adapt paths for your system  
  optionally bind a key to invoke the script in [keybindings.json](#keybindingsjson)
- Python has to be installed on your system

<br>

- select some code lines, be careful to select complete lines
- the line in the selection with the right most comment is used as position template  
  if no existing comments are found a default position is used  
  already commented or longer lines are ignored
- press your binded key or run multiCommand.padSel (with command palette)
- the selection will be processed and replaced

<br>

- see script for adding programming languages
- for debugging and error messages change in settings.json  
  `"command-runner.terminal.autoFocus": true`
- if terminal.autoFocus is true or on slow machines try  
  `"interval": 500`
- adapt paths to python interpreter and script for your system  
  `"padSel": "..\\python.exe ..\\padSel.py ${fileExtname}"`

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

### **keybindings.json**
optional
```
[
    {
        "key": "ctrl+alt+p",
        "command": "multiCommand.padSel",
        "when": "editorTextFocus"
    }
]
```

### **prerequisites**
https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command  
https://marketplace.visualstudio.com/items?itemName=edonet.vscode-command-runner  
https://www.python.org/

<br>

#### V0.5 220711
---

#### contact
[qrt@qland.de](mailto:qrt@qland.de)
