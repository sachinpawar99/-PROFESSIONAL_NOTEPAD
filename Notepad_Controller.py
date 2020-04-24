from Notepad_Model import Model
class Controller:

    def __init__(self):
        self.Model=Model()

    def save(self,msg,url):
        self.Model.save_file(msg,url)

    def save_as(self,msg,url):
        self.Model.save_as(msg,url)

    def read_file(self,url):
        self.msg,self.base=self.Model.read_file(url)
        return self.msg,self.base

    def takeQuery(self):
        self.takeAudio = self.Model.takeQuery()
        return self.takeAudio


