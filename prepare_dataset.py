# this scripts read a bunch of .csv files, chunks them into 1 second intervals and saves as .wav files
import pandas as pd
from scipy.io.wavfile import write
import os
import soundfile as sf

# COLD
cold_path = '/local2/abzaliev/road_sound/road test 02-13-24 Dixie Hwy and I-75'
mph50 = pd.read_csv(os.path.join(cold_path, 'road test1-50MPH_road-name-Dixie hwy_cold 35F.csv'), header=None)
mph60 = pd.read_csv(os.path.join(cold_path, 'road test1-60MPH_road-name-I75_cold 35F.csv'), header=None)
mph65 = pd.read_csv(os.path.join(cold_path, 'road test1-65MPH_road-name-Dixie hwy_cold 35F.csv'), header=None)
mph70 = pd.read_csv(os.path.join(cold_path, 'roadtest1_70MPH_road-name-I75_cold 35F.csv'), header=None)

sf.write('new_file.flac', data, 25600)
