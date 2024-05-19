import speech_recognition as sr

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something:")
        audio = r.listen(source)

        try:
            recognized_text = r.recognize_google(audio)
            print("You have said:\n", recognized_text)

            # Save the recognized text to a text file
            with open("recognized_text.txt", "w") as file:
                file.write(recognized_text)
                print("Recognized text saved to 'recognized_text.txt'.")

        except sr.UnknownValueError:
            print("The  Speech Recognition model could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()
