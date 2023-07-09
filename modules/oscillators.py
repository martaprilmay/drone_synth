import numpy as np


class Oscillator:
    def __init__(self, sample_rate=44100):
        self._sample_rate = sample_rate

    def sine_wave(self, frequency, duration):
        num_frames = int(duration * self._sample_rate)
        t = np.arange(num_frames) / float(self._sample_rate)
        waveform = np.sin(2 * np.pi * frequency * t)
        return waveform

    def sawtooth_wave(self, frequency, duration):
        num_frames = int(duration * self._sample_rate)
        t = np.arange(num_frames) / float(self._sample_rate)
        waveform = 2 * frequency * (t - np.floor(t + 0.5))
        return waveform

    def triangle_wave(self, frequency, duration):
        num_frames = int(duration * self._sample_rate)
        t = np.arange(num_frames) / float(self._sample_rate)
        waveform = np.abs(4 * frequency * (t - np.floor(t + 0.5))) - 1
        return waveform

    def square_wave(self, frequency, duration):
        num_frames = int(duration * self._sample_rate)
        t = np.arange(num_frames) / float(self._sample_rate)
        waveform = np.sign(np.sin(2 * np.pi * frequency * t))
        return waveform

    def pulse_wave(self, frequency, duration, pulse_width=0.3):
        num_frames = int(duration * self._sample_rate)
        t = np.arange(num_frames) / float(self._sample_rate)
        waveform = np.where(np.sin(2 * np.pi * frequency * t) >= pulse_width, 1.0, -1.0)
        return waveform
