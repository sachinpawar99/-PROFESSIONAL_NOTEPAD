import os
import speech_recognition as s
import pyaudio
class Model:
    def __init__(self):
        self.key='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.offset=5

    def encrypt(self,plaintext):
        result=''
        for st in plaintext:
            try:
               ind=(self.key.index(st)+self.offset)%62
               result+=self.key[ind]
            except ValueError:
                result+=st
        return result

    def decrypt(self,cinphertext):
        result = ''
        for st in cinphertext:
            try:
                ind = (self.key.index(st) - self.offset) % 62
                result += self.key[ind]
            except ValueError:
                result += st
        return result

    def save_file(self,msg,url):
        if(type(url) is not  str):
            file=url.name
        else:
            file=url
        filename , extension=os.path.splitext(file)
        if(extension in '.ntxt'):
               encrypt=self.encrypt(msg)
               with open(url.name,"w",encoding='utf-8')as fin:
                      fin.write(encrypt)
        else:
            content=msg
            with open(url.name,"w",encoding='utf-8')as fin:
                 fin.write(content)

    def save_as(self,msg,url):
        if (type(url) is not str):
            file = url.name
        else:
            file=url

        encrypt = self.encrypt(msg)
        with open(url.name, "w", encoding='utf-8')as fin:
             fin.write(encrypt)

    def read_file(self,url):
            file=url
            filepath = os.path.basename(file)
            filename, extension = os.path.splitext(file)
            if (extension in '.ntxt'):
                    f=open(file, "r")
                    read=f.read()
                    decrypt=self.decrypt(read)
                    f.close()
                    return filepath,decrypt
            else:
                f = open(file, "r")
                read=f.read()
                return filepath,read

    def takeQuery(self):
        sr = s.Recognizer()
        sr.pause_threshold = 1
        with s.Microphone() as m:
            try:
                sr.adjust_for_ambient_noise(m)
                audio = sr.listen(m)
                query = sr.recognize_google(audio, language='eng-in')
                return query
            except Exception as e:
                print("Exception in this ",e)
                print("not recognized")
