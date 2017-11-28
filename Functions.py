import wave
import math
import struct
import random
import string
import pygame

class Audio:
    temp_name = "".join([random.choice(string.digits + string.letters) for i in xrange(15)]) + ".wav"
    sound = []
    CHANNELS = 2
    SAMPLE_WIDTH = 2
    SAMPLE_RATE = 44100.0
    BIT_DEPTH = 2.0
    sample_length = 0
    volume = 0

    def __init__(self,frequency, sampleRate, sampleLength, volume):
        """Generates Sinal Wave"""
        values = []
        self.sample_rate = sampleRate
        self.sample_length = sampleLength
        self.volume = volume
        for i in range(0, sampleLength):
            value = math.sin(2 * math.pi * frequency * (i / sampleRate)) * (volume * self.BIT_DEPTH)
            packed_value = struct.pack('h', value)

            for j in xrange(0, self.CHANNELS):
                self.sound.append(packed_value)

    def save_wave_file(self,filename):
        """Saves File as WAV"""
        noise_out = wave.open(filename, 'w')
        noise_out.setparams((self.CHANNELS, self.SAMPLE_WIDTH, self.SAMPLE_RATE, 0, 'NONE', 'not compressed'))
        value_str = ''.join((str(n) for n in self.sound))
        noise_out.writeframes(value_str)
        noise_out.close()

    def vol_change(self,multiplier):
        """Multiplies """
        for s in self.sound:
            s*=multiplier

    def flatten(self,value):
        for s in self.sound:
            if s+value < 0:
                s=0
            else:
                s+=value

    def change_lambda(self,function):
        """Lambda function with perams sound value at location (or value at time)"""
        for i in range(0,len(self.sound)):
            self.sound[i]=function(self.sound[i],i)

    def play(self):
        self.save_wave_file(self.temp_name)
        sound = pygame.mixer.Sound(self.temp_name)
        sound.play()

