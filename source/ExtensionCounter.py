#!/usr/bin/python3
import os
import sys
import json
import mutagen
from pydub import AudioSegment as seg
import time

extz={}
walk_dir = sys.argv[1]
out_dir = sys.argv[2]

yearLyst = sorted(['1725',
 '1955',
 '1956',
 '1957',
 '1958',
 '1960',
 '1961',
 '1963',
 '1964',
 '1965',
 '1966',
 '1967',
 '1968',
 '1969',
 '1970',
 '1971',
 '1972',
 '1973',
 '1974',
 '1975',
 '1976',
 '1977',
 '1978',
 '1979',
 '1980',
 '1981',
 '1982',
 '1983',
 '1984',
 '1985',
 '1986',
 '1987',
 '1988',
 '1989',
 '1990',
 '1991',
 '1992',
 '1993',
 '1994',
 '1995',
 '1996',
 '1997',
 '1998',
 '1999',
 '2000',
 '2001',
 '2002',
 '2003',
 '2004',
 '2005',
 '2006',
 '2007',
 '2008',
 '2009',
 '2010',
 '2011',
 '2012',
 '2013',
 '2014',
 '2015',
 '2016',
 '2017',
 '2019'])

genreLyst = sorted(["metal",
            "hip",
            "rock",
            "classical",
			'hardcore'])

index = 0

start = time.time()

extz['error'] = []
extz['skip'] = []

for root, directories, filenames in os.walk(walk_dir):
	for filename in filenames:
		filepath=os.path.join(root,filename)
		ext=os.path.splitext(filename)[-1].lower()

		if ext not in extz:
			extz[ext] = {}
			extz[ext]['kount'] = 0
			extz[ext]['GENRE'] = {}
			extz[ext]['YEAR'] = {}

		extz[ext]['kount'] += 1

		if ext == '.mp3' or ext == '.flac':
			print(filename)
			try:
				muta = mutagen.File(filepath)
				genre, year = None, None

				if 'TCON' in muta:
					genre = str(muta['TCON'][0]).lower()

					if 'metal' in genre:
						genre = 'metal'
					elif 'hip' in genre or 'rap' in genre:
						genre = 'hip'
					elif 'rock' in genre:
						genre = 'rock'
					elif 'hardcore' in genre:
						genre = 'hardcore'

					if genre in extz[ext]['GENRE']:
						extz[ext]['GENRE'][genre] += 1
					else:
						extz[ext]['GENRE'][genre] = 1

				if 'TDRC' in muta:

					year = str(muta['TDRC'][0])

					if (len(year) > 4):
						year = year[0:4]

					if year == '' or year == ' ' or year == '0000' or year == '0004':
						continue

					if year in extz[ext]['YEAR']:
						extz[ext]['YEAR'][year] += 1
					else:
						extz[ext]['YEAR'][year] = 1

				if genre in ('metal', 'hip', 'rock', 'classical', 'hardcore') and year is not None:
					print('working with file: ' + str(filename))

					output = seg.from_file(filepath, ext.replace('.',''))

					minuteLength = int(len(output)/1000/60)
					if (minuteLength >= 2):
						wavName = str(len(yearLyst) * genreLyst.index(genre) + yearLyst.index(year)) + '_' + str(index) + '.wav'
						index += 1

						output = output[:2*60*1000]
						output = output.set_frame_rate(16000)
						output.export(os.path.join(out_dir,wavName), format='wav')
						print('outputed: ' + str(wavName))
					else:
						extz['skip'] += [filepath]
						print('skipping: ' + str(wavName))

			except:
				extz['error'] += [filename]

print('Took ' + str(time.time() - start))
with open('data.json', 'w') as outfile:
	json.dump(extz, outfile)