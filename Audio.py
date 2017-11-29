import wave
import math
import struct
import random
import string
import pygame
import os
import Buttons

current_audio = None
prev_audio = None
error_bar = ""


def new_audio():  # generates new audio
    global current_audio, prev_audio
    prev_audio = current_audio
    current_audio = Audio(4000.0, 44100.0, 132000, 1000.0)

class Audio:
    """ Class Variables """
    FILE_LOCATION = "Sounds/"
    save = False
    name = FILE_LOCATION + "".join([random.choice(string.digits + string.letters) for i in xrange(15)]) + ".wav"
    sound = []
    audio = []
    CHANNELS = 2
    SAMPLE_WIDTH = 2
    SAMPLE_RATE = 44100.0
    BIT_DEPTH = 2.0
    sample_length = 0
    volume = 0

    """ File Functions """

    def __init__(self,frequency, sampleRate, sampleLength, volume):
        """Generates Sinal Wave --EDIT OF GITHUB CODE BY BRIAN--"""
        self.sample_rate = sampleRate
        self.sample_length = sampleLength
        self.volume = volume
        for i in range(0, sampleLength):
            self.sound.append(math.sin(2 * math.pi * frequency * (i / sampleRate)) * (volume * self.BIT_DEPTH))

    def play(self):
        self.save_wave_file()
        audio = pygame.mixer.Sound(self.name)
        audio.play()
        Buttons.display_error_text("Playing Sound",5)
        if not self.save:
            try:
                os.remove(self.name)
            except:
                pass

    def btn_save(self):
        self.save = True
        if Buttons.all_buttons[0].text != "":
            self.name = Buttons.all_buttons[0].text
        if self.name[-4:] != ".wav":
            self.name = self.name + ".wav"
        Buttons.all_buttons[1].text = "Saved File: " + self.name
        self.save_wave_file()

    def save_wave_file(self):
        self.audio = []
        for i in self.sound:
            packed_value = struct.pack('h', i)
            for j in xrange(0, self.CHANNELS):
                self.audio.append(packed_value)
        noise_out = wave.open(self.name, 'w')
        noise_out.setparams((self.CHANNELS, self.SAMPLE_WIDTH, self.SAMPLE_RATE, 0, 'NONE', 'not compressed'))
        value_str = ''.join((str(n) for n in self.audio))
        noise_out.writeframes(value_str)
        noise_out.close()

    def del_file(self):
        self.save = False
        try:
            os.remove(self.name)
        except:
            global error_bar
            error_bar = "No Such File Name" # todo: Is it possible to del self object or leave to GC

    """ Audio Functions """

    def increase_volume(self,loc=[0,0]):
        if loc == [0,0]:
            loc = [0,len(self.sound)]
        val = self.get_int_textbox()
        Buttons.display_error_text("Increase vol: " + str(val))
        for s in self.sound[loc[0]:loc[1]]:
            s *= val

    def flatten(self,loc=[0,0]):
        if loc == [0,0]:
            loc = [0,len(self.sound)]
        val = self.get_int_textbox()
        Buttons.display_error_text("Flatten vol: " + str(val))
        for s in self.sound[loc[0]:loc[1]]:
            s = s - (s / val)

    def cut(self,loc=[0,0]):
        if loc == [0,0]:
            loc = [0,len(self.sound)]
        loc[0] = self.get_int_textbox()
        Buttons.display_error_text("Cut at: " + str(loc))
        for s in self.sound[loc[0]:loc[1]]:
            s = 0

    def linear_vol(self,val=0.0,loc=[0,0]):
        inc = self.get_int_textbox()
        Buttons.display_error_text("Linear vol increase: " + str(inc))
        for i in range(loc[0], loc[1]):
            self.sound[i] += val + (i * inc)

    def ex_vol(self,loc=[0,0]):
        inc = self.get_int_textbox()
        if loc == [0,0]:
            loc = [0,len(self.sound)]
        Buttons.display_error_text("Exponential vol increase: " + str(inc))
        for i in range(loc[0], loc[1]):
            self.sound[i] = pow(self.sound, i + inc)

    def echo(self,sound2=[0],loc=5000):
        loc = self.get_int_textbox()
        Buttons.display_error_text("Echoing at: " + str(loc))
        if sound2 == [0]:
            sound2 = self.sound
        i = 0
        while self.sound[i] is not None and sound2[i+loc] is not None:
            self.sound[i] += sound2[i+loc]


def get_int_textbox(self):
    try:
        return float(Buttons.all_buttons[0].text)
    except:
        Buttons.display_error_text("Please input a number")
        return 1