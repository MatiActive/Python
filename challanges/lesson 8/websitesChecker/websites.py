class Websites:
    def __init__(self,filename):
        self.filename = filename
        self.fileList = [] # lista slownikow
        self.reportList = []
        self.index = 0
        self.loadFile(filename)

    def loadFile(self, filename):
        fh= open(filename, "r")
        dataList = fh.readlines()
        for i in dataList:
            i = "https://" + i.strip()
            data = {"website" : i, "statusCode" : -1}
            self.fileList.append(data)
            data["index"]= len(self.fileList) - 1

            #print(data)
    def getNextWebsiteToCheck(self):
        if self.index >= len(self.fileList):
            return None
        
        data = self.fileList[self.index]
        self.index += 1
        return data
    
    def putWebsiteData(self,data):
        if "index" in data and "website" in data and "statusCode" in data:
            self.reportList.append(data)
        else:
            print("bad keys in report: " + str(data))

    
    def saveReport(self):
        fh = open("report.txt", "w")
        for el in self.reportList:
            fh.write(str(el["website"])+ "-" + str(el)+ "\n")
        fh.close()
        print("report saved")