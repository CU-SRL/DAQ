import csv
import io
import queue
import datetime
import time
import threading 

class loggingTelem():
    def __init__(self, telemQ):
        self.telemQ = telemQ
        self.run_flag = threading.Event()
        self.path = 'telemetry/testData%s.csv' % (str(datetime.datetime.today()))
        self.csvFile = open(self.path, 'w', newline= '\n')
        self.dataWriter = csv.writer(self.csvFile, delimiter = ',')
        self.header = ['time','loadcell','tc1','tc2'] 
        self.dataWriter.writerow(self.header)
        print("peepeepoopoo")

    def __del__(self):
        self.csvFile.close()

    def logTelem(self):
        while not self.run_flag.is_set():
            if (not (self.telemQ.empty())):
                self.dataWriter.writerow(self.telemQ.get())
                #print(self.telemQ.get())
            time.sleep(.5)
    
    def close_csv(self):
        self.csvFile.close()




 #Test for logging. Won't get called by main file
if __name__ == "__main__":
     telemQTest = queue.Queue(maxsize = 100)
     loggingObj = loggingTelem(telemQTest)
     #loggingObj.path = '../telemetry/testData%s.csv' % (str(datetime.datetime.today()))

     telemQTest.put(['beans1','beans1','beans1','beans1'])
     telemQTest.put(['beans2','beans1','beans1','beans1'])
     telemQTest.put(['beans3','beans1','beans1','beans1'])
     telemQTest.put(['beans4','beans1','beans1','beans1'])

     loggingObj.logTelem()
