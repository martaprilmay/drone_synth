import numpy as np


class FX:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def broken_reverb(self, waveform, reverb_decay: float):
        """
        reverb_decay: The decay amount for the reverb effect. Higher values result in longer decay. (0.1 to 2.0)
        """
        impulse_response = np.random.randn(int(self.sample_rate * reverb_decay))
        waveform_with_reverb = np.convolve(waveform, impulse_response, mode='same')

        return waveform_with_reverb

    def pumping_delay(self, waveform, delay_time: float, delay_gain: float):
        """
        delay_time: The time delay of the delayed signal in seconds. (0.01 to 0.5)
        delay_gain: The gain of the delayed signal. Higher values result in a louder delayed signal. (0.1 to 0.9)
        """
        delay_frames = int(delay_time * self.sample_rate)
        delay_line = np.zeros(delay_frames)
        waveform_with_delay = np.zeros(len(waveform))

        for i in range(len(waveform)):
            if i < delay_frames:
                delayed_sample = delay_line[i]
            else:
                delayed_sample = delay_line[i % delay_frames]

            delay_line[i % delay_frames] = waveform[i] + delay_gain * delayed_sample
            waveform_with_delay[i] = waveform[i] + delayed_sample

        return waveform_with_delay

    def ok_lfo(self, waveform, lfo_frequency: float, lfo_min_depth: float, lfo_max_depth: float):
        """
        lfo_frequency: The frequency of the LFO in Hz. Determines the speed of the modulation. (0.1 to 10.0)
        lfo_min_depth: The minimum depth (amount applied) of modulation in Hz. (1.0 to 20.0)
        lfo_max_depth: The maximum depth (amount applied) of modulation in Hz. (10.0 to 100.0)
        """
        lfo = np.sin(2 * np.pi * lfo_frequency * np.arange(len(waveform)) / float(self.sample_rate))
        modulation_depth = np.random.uniform(lfo_min_depth, lfo_max_depth)
        waveform_with_lfo = waveform * (1 + lfo * modulation_depth)

        return waveform_with_lfo
