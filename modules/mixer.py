import numpy as np


class Mixer:
    @staticmethod
    def mix_waveforms(*waveforms, amplitudes=None):
        """
        Takes multiple waveforms, finds the maximum length among the waveforms and pads each waveform with zeros
        to match that length. It then adds all the padded waveforms together to create a mixed waveform.
        """
        if amplitudes is None:
            amplitudes = [1.0] * len(waveforms)

        max_length = max(len(waveform) for waveform in waveforms)
        mixed_waveform = np.zeros(max_length)

        for waveform, amplitude in zip(waveforms, amplitudes):
            scaled_waveform = amplitude * waveform
            waveform_padded = np.pad(scaled_waveform, (0, max_length - len(waveform)), mode='constant')
            mixed_waveform += waveform_padded

        return mixed_waveform
