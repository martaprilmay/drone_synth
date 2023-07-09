import pyaudio
import wave


class Player:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.p = pyaudio.PyAudio()
        self.stream = None

    def play_waveform(self, waveform, sample_rate=None):
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=sample_rate or self.sample_rate,
                                  output=True)

        self.stream.write(waveform.tobytes())

        self.stream.stop_stream()
        self.stream.close()

    def save_waveform(self, waveform, output_filename, sample_rate=None):
        with wave.open(output_filename, "wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(self.p.get_sample_size(pyaudio.paFloat32))
            wav_file.setframerate(sample_rate or self.sample_rate)
            wav_file.writeframes(waveform.tobytes())

    def terminate(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
