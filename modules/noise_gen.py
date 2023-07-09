import numpy as np


class NoiseGenerator:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def white_noise(self, duration):
        num_samples = int(duration * self.sample_rate)
        noise = np.random.randn(num_samples)
        return noise

    def pink_noise(self, duration):
        """
        Voss-McCartney algorithm to generate pink noise works by summing multiple sources of white noise
        with different periods, each contributing to different frequency bands.
        The downsampling operation helps to create a more balanced distribution of energy across the frequency spectrum.
        """
        num_samples = int(duration * self.sample_rate)
        num_sources = int(np.ceil(np.log2(num_samples)))
        num_noise_samples = 2 ** num_sources - 1

        white_noise = np.random.randn(num_noise_samples)
        pink_noise = np.zeros(num_samples)

        for _ in range(num_sources):
            pink_noise += np.pad(white_noise, (0, num_samples - num_noise_samples), mode='constant')
            white_noise = 0.5 * (white_noise[::2] + white_noise[1::2])  # Downsampling

        return pink_noise

    def brown_noise(self, duration):
        """
        Generates a waveform that resembles Brownian noise by cumulatively summing white noise samples
        and then normalizing the amplitude. Brown noise exhibits a relatively flat frequency response,
        with power decreasing by 6 dB per octave. It is often described as having a "darker" or "lower"
        sound compared to white noise.
        """
        num_samples = int(duration * self.sample_rate)
        brown_noise = np.cumsum(np.random.randn(num_samples))
        return brown_noise / np.max(np.abs(brown_noise))
