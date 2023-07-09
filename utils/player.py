import pyaudio
import wave


class Player:
    def __init__(self, sample_rate=44100):
        self._sample_rate = sample_rate
        self._p = pyaudio.PyAudio()
        self._stream = None

    def play_waveform(self, waveform, sample_rate=None):
        self._stream = self._p.open(format=pyaudio.paFloat32,
                                   channels=1,
                                   rate=sample_rate or self._sample_rate,
                                   output=True)

        self._stream.write(waveform.tobytes())

        self._stream.stop_stream()
        self._stream.close()

    def save_waveform(self, waveform, output_filename, sample_rate=None):
        with wave.open(output_filename, "wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(self._p.get_sample_size(pyaudio.paFloat32))
            wav_file.setframerate(sample_rate or self._sample_rate)
            wav_file.writeframes(waveform.tobytes())

    def terminate(self):
        if self._stream is not None:
            self._stream.stop_stream()
            self._stream.close()
        self._p.terminate()
