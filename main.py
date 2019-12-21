import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):


def mergeAudios(audios):    
def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')
    start=88000
    finish=90200
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")
    audio=AudioSegment.from_mp3('railway.mp3')
    
    start=91000
    finish=92200
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")
    
    
    start=
    finish=
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    
    start=
    finish=
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")
    
    audio=AudioSegment.from_mp3('railway.mp3')
    start=
    finish=
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")
    
def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
            
if__name__=="__main__":
    print("Generating Skeleton")
    generateSkeleton()
    print("Now generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")    