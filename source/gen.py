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

index = 0
itr = 5000
end = 4400

start = time.time()

def cmd(num, sec=30):
	cmdstart = time.time()

	global walk_dir
	for genre in range(5):
		os.chdir('.../tensorflow-wavenet/')
		rawString = 'python3 generate.py --samples ' \
			+ str(16000 * sec) + ' --gc_channels=32 --gc_cardinality=5 --gc_id=' + str(genre) \
			+ ' --wav_out_path '+str(out_dir)+'gen_genre-' + str(genre) + '_num-' + str(num) + '.wav ' \
			+ str(walk_dir) + 'model.ckpt-' + str(num)
		
		print(rawString)

	print('Gen of num/sec ' + str(num) + '/' + str(sec) + ' took ' + str(time.time() - cmdstart))

index = 20
itr = 5000
end = 15000

while index <= end:

	cmd(index)
	index = index + itr
	if index == end:
		sys.exit(0)
	if index > end:
		index = end

	time.sleep(1)

print('Took ' + str(time.time() - start))
