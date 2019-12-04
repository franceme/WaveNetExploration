default:: train

train: sync
	clear
	nohup ./AutoRun.sh >/dev/null 2>&1 &
	tail -f results.txt

syncSettings:
	cp Makefile .../Checkpoints/Makefile
	cp results.txt .../Checkpoints/results.txt

sync:
	nohup watch -n 20 "rsync -rvhpt .../2019-11-24T04-32-56 .../Checkpoints/" >/dev/null 2>&1 &
	nohup watch -n 20 "cp results.txt .../Checkpoints/results.txt" >/dev/null 2>&1 &


reset:
	cp .../results_StepsTo*.txt results.txt

terribleScan:
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=0 --wav_out_path .../Generations/gen_genre-0_num-20.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-20 >> .../results_gen.txt 2>&1
	$(($(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=1 --wav_out_path .../Generations/gen_genre-1_num-20.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-20 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=2 --wav_out_path .../Generations/gen_genre-2_num-20.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-20 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=3 --wav_out_path .../Generations/gen_genre-3_num-20.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-20 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=4 --wav_out_path .../Generations/gen_genre-4_num-20.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-20 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=0 --wav_out_path .../Generations/gen_genre-0_num-5020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-5020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=1 --wav_out_path .../Generations/gen_genre-1_num-5020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-5020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=2 --wav_out_path .../Generations/gen_genre-2_num-5020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-5020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=3 --wav_out_path .../Generations/gen_genre-3_num-5020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-5020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=4 --wav_out_path .../Generations/gen_genre-4_num-5020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-5020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=0 --wav_out_path .../Generations/gen_genre-0_num-10020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-10020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=1 --wav_out_path .../Generations/gen_genre-1_num-10020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-10020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=2 --wav_out_path .../Generations/gen_genre-2_num-10020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-10020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=3 --wav_out_path .../Generations/gen_genre-3_num-10020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-10020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=4 --wav_out_path .../Generations/gen_genre-4_num-10020.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-10020 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=0 --wav_out_path .../Generations/gen_genre-0_num-15000.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-15000 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=1 --wav_out_path .../Generations/gen_genre-1_num-15000.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-15000 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=2 --wav_out_path .../Generations/gen_genre-2_num-15000.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-15000 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=3 --wav_out_path .../Generations/gen_genre-3_num-15000.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-15000 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=4 --wav_out_path .../Generations/gen_genre-4_num-15000.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-15000 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt