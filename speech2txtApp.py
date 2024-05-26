from flask import Flask
import speech_recognition as sr
app = Flask(__name__)

def recognize_speech():
    r = sr.Recognizer()
    response = ""

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        response += "Please say something...\n"

        try:
            audio = r.listen(source)
            recognized_text = r.recognize_google(audio)
            response += "You have said: \n" + recognized_text
        except sr.UnknownValueError:
            response += "The Speech Recognition model didn't understand the audio"
        except Exception as e:
            response += "Error: " + str(e)

    return response

@app.route('/recognize_speech', methods=['GET'])
def recognize_speech_route():
    result = recognize_speech()
    return result

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
