import csv
import io
import queue
import datetime
import time

class loggingTelem():
    def __init__(self, telemQ):
        self.telemQ = telemQ
        self.csvFile = open('../telemetry/testData%s.csv' % (str(datetime.datetime.today())), 'w', newline= '')
        self.dataWriter = csv.writer(self.csvFile, delimiter = ',')
        self.header = ['time','loadcell','tc1','tc2'] 
        self.dataWriter.writerow(self.header)

    def __del__(self):
        self.csvFile.close()

    def logTelem(self):
        while(True):
            if (not (self.telemQ.empty())):
                self.dataWriter.writerow(self.telemQ.get())
            time.sleep(.5)



#Test for logging. Won't get called by main file
if __name__ == "__main__":
    telemQTest = queue.Queue(maxsize = 100)
    loggingObj = loggingTelem(telemQTest)

    telemQTest.put(['beans1','beans1','beans1','beans1'])
    telemQTest.put(['beans2','beans1','beans1','eans1'])
    telemQTest.put(['beans3','beans1','beans1','beans1'])
    telemQTest.put(['beans4','beans1','beans1','beans1'])

    loggingObj.logTelem()
