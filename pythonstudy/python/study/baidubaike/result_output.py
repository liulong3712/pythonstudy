class result_output:
    def __init__(self):
        pass

    def outPutFile(self, outputData):
        #E:\PythonStudy\pythonstudy\python\study\baidubaike
        import chardet
        #print chardet.detect(outputData)
        fp = open('E:\\PythonStudy\\pythonstudy\\python\\study\\baidubaike\\text.txt','a')
        fp.write(outputData.encode('utf-8'))
        fp.write('\n')
        fp.close()