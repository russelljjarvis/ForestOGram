from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import time
from scipy import signal, misc
import colorsys
import soundfile as sf
from scipy.linalg import svd
import scipy
from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage import gaussian_filter1d
import h5py
import array
from pydub import AudioSegment
from pydub.utils import get_array_type
import wave
from scipy.io.wavfile import write
from scipy import signal
path1 ="XC155388-Pink Pigeon (song, Mauritius, Black River Gorge, nov2012, 2).MP3"
sound = AudioSegment.from_file(file=path1)

fs = sound.frame_rate
left = sound.split_to_mono()[1]

bit_depth = left.sample_width * 8
array_type = get_array_type(bit_depth)

numeric_array = array.array(array_type, left._data)

label = loadtxt("XC155388 - Pink Pigeon - Nesoenas mayeri.txt")

num_label = len(label[:,0])

for raw in range (num_label):

        onset = int(label[raw, 0]*fs)

        offset = int(label[raw, 1]*fs)

        segment = numeric_array[onset:offset]

        write("segment_%s.wav" %raw, fs, int16(segment))

        print ("finish generating segment %s is from %s s (%s) to %s (%s)s" %(raw,label[raw, 0], onset,label[raw, 1], offset) )
