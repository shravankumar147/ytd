import pafy
from pydub import AudioSegment
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=True, help="download link")
args = vars(ap.parse_args())


url = args["url"]
v = pafy.new(url)

# download the audio
ba = v.getbestaudio(preftype='m4a')
print('download started...')
filename = ba.download()
print('download completed!')
fname = filename.split('.')

# Convert m4a to mp3
# !avconv -i 'chain_smokers.m4a' 'out_chainsmokers.mp3'

sound = AudioSegment.from_file(filename)
print('converting m4a to mp3....')
sound.export(''.join([fname[0], '.mp3']), format="mp3", bitrate="192")
print('DONE!')
