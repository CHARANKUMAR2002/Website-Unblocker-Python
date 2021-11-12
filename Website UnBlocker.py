from tkinter import *

win = Tk()
win.update()
win.geometry('160x80')
win.resizable(0,0)
win.config(bg='light green')
win.title('UnBlock All Websites')
host_path = 'C:\Windows\System32\drivers\etc\hosts'


def unblock():
    with open(host_path, 'w') as host:
        host.write('# Copyright (c) 1993-2009 Microsoft Corp.\n'
"#\n"
"# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.\n"
"#\n"
'# This file contains the mappings of IP addresses to host names. Each\n'
'# entry should be kept on an individual line. The IP address should\n'
'# be placed in the first column followed by the corresponding host name.\n'
'# The IP address and the host name should be separated by at least one\n'
'# space.\n'
'#\n'
'# Additionally, comments (such as these) may be inserted on individual\n'
'# lines or following the machine name denoted by a # symbol.\n'
'#\n'
'# For example:\n'
'#\n'
'#      102.54.94.97     rhi9o.acme.com          # source server\n'
'#       38.25.63.10     x.acme.com              # x client host\n\n'

'# localhost name resolution is handled within DNS itself.\n'
'#	127.0.0.1       localhost\n'
'#	::1             localhost\n')
        Label(win, text='UnBlocked All Websites!', font='arial 10 bold', bg='light green').place(x=0, y=50)


un_blocker = Button(win, text='UnBlock', font='arial 12 bold', pady=1, command= unblock, width=7, bg='green', activebackground='blue')
un_blocker.place(x=38, y=10)
win.mainloop()

