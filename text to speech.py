from gtts import gTTS
import os
text=open("newone.txt",'r',encoding='utf-8').read()
output=gTTS(text=text,lang="en",slow=False)
output.save("fileread1.mp3")
os.system("start fileread1.mp3")







































