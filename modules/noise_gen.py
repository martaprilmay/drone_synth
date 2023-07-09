import numpy as np


class NoiseGenerator:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def white_noise(self, duration):
        num_samples = int(duration * self.sample_rate)
        noise = np.random.randn(num_samples)
        return noise
