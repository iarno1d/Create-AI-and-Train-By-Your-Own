import sounddevice as sd
import queue
from vosk import Model, KaldiRecognizer
import json

class VoiceRecognizer:
    def __init__(self, model_path):
        # Load the Vosk model
        self.model = Model(model_path)
        self.q = queue.Queue()

    def recognize_voice(self):
        """Captures voice input and converts it to text."""
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=lambda indata, frames, time, status: self.q.put(indata[:])):
            recognizer = KaldiRecognizer(self.model, 16000)
            print("Listening... Speak now!")
            while True:
                # Read from the queue
                data = self.q.get()
                if recognizer.AcceptWaveform(data):
                    # Process the result and return the recognized text
                    result = json.loads(recognizer.Result())
                    return result.get('text', '')
