import pyttsx3
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    speak("I am EDITH. Tony Stark's augmented reality security and defense system.")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....") 
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
        print("recognition..")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("sorry, say again..")
        return "none"
    return query
    
if __name__=="__main__":
    wish()
    while True:
        query=command().lower()
        if "made you?" in query:
            query=query.replace("you have access to all of Tony's protocols.")
            speak(query)
        if 'wikipedia' in query:
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)