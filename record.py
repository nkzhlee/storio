from flask import Flask, render_template, request
import os,io
import speech_recognition as sr
import wave
import base64
from google.cloud import speech_v1p1beta1 as speech
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('process-audio.html')

@app.route('/process-audio', methods=['POST'])
def process_audio():
    # filename = 'output.wav'
    # data = request.files['audio']
    # audio_file = os.path.join(app.instance_path, filename)
    #
    # audio_data = memoryview(data.read())
    # #define the audio file parameters
    # nframes = len(audio_data)
    # # create a new wave file
    # wavefile = wave.open(audio_file, 'wb')
    # # set the parameters for the wave file
    # wavefile.setnchannels(1)
    # wavefile.setsampwidth(2)
    # wavefile.setframerate(44100)
    # wavefile.setnframes(nframes)
    # # write the audio data to the wave file
    # wavefile.writeframes(audio_data)
    # # # close the wave file
    # wavefile.close()
    # # initialize the recognizer
    # r = sr.Recognizer()
    # # use the recognizer to read the audio file
    # with sr.AudioFile(audio_file) as source:
    #     audio_text = r.record(source)  # read the entire audio file
    #
    # # use the recognizer to transcribe the audio to text
    # text = r.recognize_google(audio_text)
    print("11111")
    audio_file = request.files['audio']

    # convert audio file to bytes
    audio_bytes = audio_file.read()
    # create speech-to-text client
    client = speech_v1.SpeechClient()
    # set audio file properties
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        audio_channel_count=2,
        enable_separate_recognition_per_channel=True,
    )

    # create audio object
    audio = {
        'content': audio_bytes
    }

    # perform speech-to-text conversion
    response = client.recognize(config, audio)
    # extract transcription from response
    transcription = response.results[0].alternatives[0].transcript
    # print the transcribed text
    print(transcription)
    return "Audio processed successfully"

if __name__ == '__main__':
    app.run()
