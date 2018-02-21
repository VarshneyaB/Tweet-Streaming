class export:
    def __init__(self):
        self.__cols = None

    def setColumns(self,*args):
        self.__cols = args
        print(args)
    
    def export(self,filename,tweets,mode,sep = " "):
        writer = open(filename,mode,encoding="utf-8")
        for i in tweets:
            row = ""
            for j in self.__cols:
                if j in i:
                    data = str(i[j])
                else:
                    data = "NULL"
                row += str(data) + sep
            row.strip()
            print(row)
            writer.write(row + "\n")
        writer.close()
                


