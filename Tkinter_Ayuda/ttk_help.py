import funciones as ff

from tkinter import ttk

dd1 =['Button', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'LabeledScale', 'Labelframe', 'Menubutton']
dd2 = ['Notebook', 'OptionMenu', 'PanedWindow', 'Panedwindow', 'Progressbar', 'Radiobutton', 'Scale', 'Scrollbar', 'Separator']
dd3 = ['Sizegrip', 'Spinbox', 'Style', 'Treeview', 'Widget', 'setup_master', 'tclobjs_to_py', 'tkinter']

for ss in dd3:
 com = 'ttk.'+ss
 print(help(eval(com)))


