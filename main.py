import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()


while True:
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language='es-MX')
            print("Has dicho: " + texto)
            if "ecobus" in texto:
                engine.say("Palabra detectada: Ecobus")
                engine.runAndWait()
        except sr.UnknownValueError:
            print("No se puedo reconocer la palbra")
        except sr.RequestError as e:
            print(f"Error al solicitar los resultados del servicio de reconocimiento de voz; {e}")

