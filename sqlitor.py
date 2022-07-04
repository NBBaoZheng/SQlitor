from lib import lib_sqlite
import sys,os
os.system("title Sqlitor Runtime&&cls")
print("Sqlitor beta0.1")
sysrecv = sys.argv[1]
if sysrecv == '-o':

    init = lib_sqlite.LIB_SQLITE(path=sys.argv[2])
 
    while 1:
        command = input(">>>")
        if command == "exit":
            init.closedb()
            sys.exit()
        else:
            init.runcmd(command)

