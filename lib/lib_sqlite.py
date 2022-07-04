import sys,datetime,threading,sqlite3
class LIB_SQLITE:
    def __init__(self,path):
        if path != "":
            if __name__ != "":
                self.opendb = sqlite3.connect(path)
                print("[*]Opening Database...")
                self.cursor = self.opendb.cursor()
                print("[+}Database open success!\n[*]Creating cursor...")
    def runcmd(self,command):
        '''run db command'''
        print("[*]Running Command:"+command)
        try:
            self.cursor.execute(command)
            if self.cursor.fetchone():
                print("[+]Database sent back results:\n")
                for i in self.cursor.fetchone():
                    print(i)
                print("\n")
            else:
                print("[+]Executed command!")
            return self.cursor.fetchone()
        except Exception as e:
            print("[!]Error!\n"+str(e))
            print("[*]Rolling back...")
            self.opendb.rollback()
            print("[+]Command rolled back.")
            
    def closedb(self):
        print("[*]Commiting cursor...")
        self.opendb.commit()
        print("[+]Cursor commit success!\n[*]Closing cursor...")
        self.cursor.close()
        print("[*]Cursor Closed\n[*]Closing Database...")
        self.opendb.close()
        print("[+]Database Close Success!")
        
        
