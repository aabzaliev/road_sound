# this scripts read a bunch of .csv files, chunks them into 1 second intervals and saves as .wav files
import pandas as pd
import numpy as np
from scipy.io.wavfile import write
import os
import soundfile as sf
from pydub import AudioSegment
from math import log, ceil
from pydub.utils import make_chunks

SAMPLERATE = 25600
destination_path = "/local2/abzaliev/road_sound/road_data"
COLUMN = 3 # we use the microphone from the front  wheel / inside the wheel well TODO experiment with different columns
chunk_length_ms = 1000  # pydub calculates in millisec
# 1 - vibration sensor (in the engine compartment)
# 2 - inside the car / in front of passenger’s seat
# 3 - side of the car / next to rear wheel
# 4 - front  wheel / inside the wheel well.

# only running for COLD road but with different speeds
cold_path = '/local2/abzaliev/road_sound/road_data/road test 02-13-24 Dixie Hwy and I-75'
mph50 = pd.read_csv(os.path.join(cold_path, 'road test1-50MPH_road-name-Dixie hwy_cold 35F.csv'), header=None)
mph60 = pd.read_csv(os.path.join(cold_path, 'road test1-60MPH_road-name-I75_cold 35F.csv'), header=None)
mph65 = pd.read_csv(os.path.join(cold_path, 'road test1-65MPH_road-name-Dixie hwy_cold 35F.csv'), header=None)
mph70 = pd.read_csv(os.path.join(cold_path, 'roadtest1_70MPH_road-name-I75_cold 35F.csv'), header=None)

# save everything as .wav file, reload it and chunk it into 2 second audios
csv_files = {'50': mph50, '60':  mph60, '65': mph65, '70': mph70}

for name, csv in csv_files.items():
    # TODO check dtypes
    fpath = f'{destination_path}/{name}mph.wav'
    csv_shape = csv[COLUMN].values.shape
    sf.write(fpath, csv[COLUMN].values, SAMPLERATE, subtype='FLOAT')

    # now read it and chunk into smaller 1 second files
    wav, sr = sf.read(fpath)
    # wav = AudioSegment.from_file(fpath, "wav", frame_rate=SAMPLERATE)
    # wav_np = wav.get_array_of_samples()
    assert wav.shape == csv_shape # making sure after we save it as .csv the dimensions still match

    number_of_chunks = ceil(len(wav) / float(SAMPLERATE * 1)) # 1 sec = SAMPLERATE
    chunks = [wav[i * int(SAMPLERATE * 1):(i + 1) * int(SAMPLERATE * 1)] for i in range(int(number_of_chunks))]
    # chunks = make_chunks(wav, chunk_length_ms) # Make chunks of two sec
    for i, chunk in enumerate(chunks):
        destination_dir_for_chunks = f'{destination_path}/data_processed/{name}mph/'
        os.makedirs(destination_dir_for_chunks, exist_ok=True)
        chunk_name = f"chunk{i}.wav"
        sf.write(destination_dir_for_chunks + chunk_name, chunk, SAMPLERATE, subtype='FLOAT')
        # chunk.export(destination_dir_for_chunks + chunk_name, format="wav")