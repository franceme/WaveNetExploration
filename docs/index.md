---
layout: default
---

# Wave Net Exploration

## About

This is an open-source class project for the [Advanced Machine Learning course](http://courses.cs.vt.edu/cs5824/) under [Dr. Bert Huang](http://berthuang.com).
This project is intended for us (the developers) to reproduce a Machine Learning Paper's results in a new manner.

You can find the binder containing the results here [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/franceme/WaveNetExploration/master?filepath=jupyterSandbox%2FWaveNetExploration_DataHandling.ipynb).

---

For our project we reproduce the paper [WaveNet](https://arxiv.org/pdf/1609.03499.pdf), with more resources listed below. The paper can also be found at the following website [here](https://deepmind.com/blog/article/wavenet-generative-model-raw-audio).

Other papers read through this project are listed below.

> PixelCNN [Paper](https://arxiv.org/pdf/1606.05328.pdf) [Website](https://deepmind.com/research/publications/conditional-image-generation-pixelcnn-decoders)
>
> PixelRNN [Paper](https://arxiv.org/pdf/1601.06759.pdf) [Website](https://deepmind.com/research/publications/pixel-recurrent-neural-networks)

## Data Caveats

* All of the data was collected from the team members combined music.
	* **None of the music used for the training can be hosted due to various Terms and Conditions**.
* This was collected based on the top genre songs available.
	* The genres were retrieved via using the mutagen python library.
		* If the genre and the year were not available from the song, they were not used.
	* The sub genres were also moved up into their main genre.
		* ex. if the genre is metalcore, then the genre is metal.

* Also, if the song was not at least 2 minutes in length it would not be included.

```python
#Script to collect the songs
#./../../source/musicHandler.py

if ext == '.mp3' or ext == '.flac':
	print(filename)
	try:
		muta = mutagen.File(filepath)
.
.
.
		if genre in ('metal', 'hip', 'rock', 'classical', 'hardcore') and year is not None:
			print('working with file: ' + str(filename))
.
.
.
			minuteLength = int(len(output)/1000/60)
			if (minuteLength >= 2):
				wavName = str(len(yearLyst) * genreLyst.index(genre) + yearLyst.index(year)) + '_' + str(index) + '.wav'
				index += 1

				#Setting the length to two minutes
				output = output[:2*60*1000]
				output = output.set_frame_rate(16000)
				output.export(os.path.join(out_dir,wavName), format='wav')

```

## Environment Clarification
* Two computers were used only out of necessity; the checkpoints were restored from each part.
  1. The first computer (used for the steps 0 to 343 and 870 to 15000)
     * Python3: 7.6.1
     * Tensorflow: 1.14.0
     * Tensorflow-GPU: 1.14.0
     * Cores: 8
     * Ram: 16
  2. The second computer (used between the steps of 343 to 870)
     * Python3: 7.8.0
     * Tensorflow: 1.14.0
     * Tensorflow-GPU: 1.14.0
     * Cores: 6
     * Ram: 16

## Procedure

For this project, we used a similar pattern used for machine learning projects.
1. Understanding WaveNet
2. Understand or Implement the model
3. Prepare and format the data
4. Train the model
5. Run the model

---

### Understanding WaveNet

WaveNet is a deep generative architecture for modelling audio waves. The overall structure of the model is based on a previous approach to generative image modelling called pixelCNN. It is able to produce high quality audio by generating each sample sequentially, conditioning each new sample on previous generated samples, making it an autoregressive model. This is different to other recent generative modelling approaches such as generative adversarial networks (GANs) and variational auto-encoders (VAEs), which seek to approximate the latent variables of the underlying distribution giving rise to dataset.

pixelCNN is an image generating architecture based on the idea of generating an image pixel by pixel. Each new pixel is a probability distribution over possible pixel values conditioned on all previous pixels. The conditional distribution in this case in a CNN, which enables fast training as all the losses of the output values of the network given pixel values in real images can be computed in parallel. Additionally, as well as conditioning on all previous pixels, the pixels can be conditioned on a label or vector. This approach of generating an image pixel by pixel suggests a method of generating a soundwave sample by sample, however most soundwaves have sample rates of thousands of samples per second, making it computationally difficult to condition a long soundwave on all previous samples.

WaveNet overcomes this issue through the use of 'dilated causal convolution layers'. A dilated layer is essentially a convolution kernel with holes in the middle values, which means it covers a larger area than its true length. By having stacks of dilated layers, the receptive field can grow exponentially in the number of layers. WaveNet uses a small kernel size to keep computational cost down as well.

In posts on the DeepMind blog (the authors of the paper all work for DeepMind) samples generated by WaveNet are shown. Particularly impressive are the text to speech samples, which have a very human-like quality, and through conditioning on speaker identity are able to show great variety. Also shown are samples of piano music trained a classical music database.

Our project aims to recreate the successful generation of music by training a WaveNet model on a database of our own music, and see if we can achieve results comparable to the authors.

### Understanding the Model

Fortunately for us, this model had already been created several times.
To ensure we could spend most of the time for the project on training, we decided to use [ibab's](ttps://github.com/ibab/tensorflow-wavenet.git) implementation of the methodology.

> There were only two changes we implemented within the code, only to ensure project compatibility.
> > At line 274 in train.py, we modified the following to ensure we could save more checkpoints.
> > ```python3
> > -    saver = tf.train.Saver(... .max_checkpoints)
> > +    saver = tf.train.Saver(... .max_checkpoints, keep_checkpoint_every_n_hours=0.16)
> > ```
> 
> At line 68 of wavenet/audio_reader.py, we modified the following since the specific method was depricated.
> > ```python3
> > -    energy = librosa.feature.rmse(audio, frame_length=frame_length)
> > +    energy = librosa.feature.rms(audio, frame_length=frame_length)
> > ```


### Prepare and format the data

For the data preperation, the team used various music samples that were trimmed to fit a uniform format (2-minute wav files).
We choose the top 5 genres shared between us for the most amount of data.
Shown below is the distribution of collected of music samples.

<object width="100%" type="image/svg+xml" data="imgs/DataDistribution.svg"></object>

For the library used, we had to use strict wav files without any meta-data.
For this we ran a script to automatically go through the music files, and if they had a genre and a year in their meta-data, we converted their first 30 seconds into a wav file format.

### Train the model


To train the model, we ran the library for roughly 4 days using the following Scriptfile:
```bash
#./../source/AutoRun.sh

until python3 train.py --data_dir=.../Data --gc_channels=32 --checkpoint_every=10 --batch_size=2 --logdir=.../Checkpoints/2019-11-24T04-32-56 >> results.txt 2>&1; do
	echo "Restarting the service at $(date)" >> results.txt
	sleep 10
done
```
> As noted, there were several restart points where the training was migrated from machines to machine.
> The following script was used to ensure the system would automatically restart after waiting 10 seconds.

Using another script to parse through the results.txt file, we were able to obtain the following statistics throughout the training process.

```python
#captures step # - loss = #.###, (###.## sec/step)
pattern = re.compile('step [0-9]+ - loss = [0-9]+.[0-9]*, \([0-9]+.[0-9]* sec\/step\)')

#captures ##.#####
numbah = re.compile(r'[0-9]+\.?[0-9]*')
#...
with open(file, 'r') as foil:
	line, restartFlag = foil.readline(), False
	while line:
		isStep = pattern.match(line) != None and len(numbah.findall(line)) == 3
		if isStep:
			step, loss, speed = numbah.findall(line)
			results[step] = {'loss':loss, 'speed':speed}
			if restartFlag:
				restartFlag = False
				restart += [int(step)-1]
			elif line.startswith(restartPattern):
				restartFlag = True
		line = foil.readline()
```

---

> Loss vs. Step

<object width="100%" type="image/svg+xml" data="imgs/LossStep.svg"></object>

Shown above is the loss (blue) of the model at each checkpoint.
A trendline was also introduced to better visualize the overall training trend.

Also shown are the manual and automatic restart points, respectively being showing switching computers and program restart points.

---

> Speed per Step

<object width="100%" type="image/svg+xml" data="imgs/SpeedStep.svg"></object>

Shown above is the speed (blue) taken per checkpoint.
A trendline was also introduced to better visualize the speed taken.

Also shown are the manual and automatic restart points, respectively being showing switching computers and program restart points.


## Results

---

### Experiment Results

Instead of attempting an exahaustive amount of audio files, out of the 15000 steps we used four (roughly divided) checkpoints.
This would help to show the progression of the audio generation without given the timeframe for this assignment.

#### Model Training Statistics

To ensure each audio segement generation was isolated, the commands were first generated and then ran through a Makefile to ensure the order.

> The python script generating the commands iterated through the step division (the four main checkpoints)
> then used the following method to create the string

```python
#./../source/gen.py

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
		# This would print out a string command for hip (id=2) at step 20
		# python3 generate.py --samples 480000 --gc_channels=32 \
		# --gc_cardinality=5 --gc_id=2 --wav_out_path .../Generations/gen_genre-2_num-20.wav \
		# .../Checkpoints/2019-11-24T04-32-56/model.ckpt-20 >> .../results_gen.txt 2>&1
```
Combining these results with a date echo (used for checkpoints) resulted in the following Makefile section

```Makefile
# ./../source/Makefile
terribleScan:
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=0 --wav_out_path .../Generations/gen_genre-0_num-20.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-20 >> .../results_gen.txt 2>&1
	$(($(date +%s%N)/1000000)) >> .../results_gen.txt
.
.
.
	python3 generate.py --samples 480000 --gc_channels=32 --gc_cardinality=5 --gc_id=4 --wav_out_path .../Generations/gen_genre-4_num-15000.wav .../Checkpoints/2019-11-24T04-32-56/model.ckpt-15000 >> .../results_gen.txt 2>&1
	echo $$(($$(date +%s%N)/1000000)) >> .../results_gen.txt
```

---

The checkpoints gave the following insight about how long the generation took.


<object width="100%" type="image/svg+xml" data="imgs/GeneratingTime.svg"></object>

From this we know the average time for generating each audio file took approximately 1909 seconds, or 32 minutes.
The generation time for all audio samples took a total time of approximately 10 hours

#### Generated Samples

Listed below is the table linking each audio generation according to it's genre and it's checkpoint number.
Due to size limitations we chose to display the initial and final audio generation to showcase the progression of the audio generation.

| Genre/Step | 20 | 15000 |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hardcore | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/hardcore_20.mp3"     type  =  "audio/mpeg"   > | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/hardcore_15000.mp3"     type  =  "audio/mpeg"   > |
| Classical | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/classical_20.mp3"     type="audio/mpeg">    </audio> | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/classical_15000.mp3"     type="audio/mpeg">    </audio> |
| Hip | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/hip_20.mp3"     type="audio/mpeg">    </audio> | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/hip_15000.mp3"     type="audio/mpeg">    </audio> |
| Metal | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/metal_20.mp3"     type="audio/mpeg">    </audio> | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/metal_15000.mp3"     type="audio/mpeg">    </audio> |
| Rock | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/rock_20.mp3"     type="audio/mpeg">    </audio> | <audio controls> <source src="https://raw.githubusercontent.com/franceme/WaveNetExploration/master/audiogen/rock_15000.mp3"     type="audio/mpeg">    </audio> |

> Please note that for more browser support, the original output wav files were transformed into mp3 files.
> The initial wav files are still in the same [location](https://github.com/franceme/WaveNetExploration/tree/master/audiogen).

#### Generated Samples Progression

Given none of these samples are up to the quality as any of the individually trained songs, the steps show clear progression towards real music.

Relatively comparing the audio samples from steps 20 to 15000, there are more song-like elements being introduced.
There is still a lot of static, however there is more fluxuation and the base of song-like elements introduced.

Ordering the genres from top to bottem in order of the amount of songs available also help to show the difference in generated music quality (lower to higher data amount).
The rock generated music appears to have a relatively higher quality than the hardcore music, which may be due to the increase of data for the particular genre.
Speculations as to why the audio quality is still very low could include reasons such as lack of training time, training computation, or the complexity of the audio samples.
The audio samples that we used included various instruments (including but not limitied to: vocalists, drumset, guitars, base guitars and electronics) compared to the original sampling of only pianos samples from the Youtube data set.

The rest of the data files (including the checkpoints at 5020 and 100020) are located [here](https://github.com/franceme/WaveNetExploration/tree/master/audiogen).

### Models Used for the samples

We made sure to capture every 10th checkpoint during the training, however it was decided to load only the ones used for generating the [audio samples](https://github.com/franceme/WaveNetExploration/tree/master/audiogen).

You can find the models uploaded in the [modelsUsed folder](https://github.com/franceme/WaveNetExploration/tree/master/modelsUsed).

## Conclusion

Though we weren't able to generate music, through our process and relatively minimal training we were able to show progression towards actual music. This supports the original WaveNet paper, since the progression we created with our relatively limited training time and data shows the progression of the WaveNet model.

However, our particular experiment shows a large degree of underfitting. It is likely that the complexity of the model needed to be increased to accommodate the complexity of the music we chose. It is also possible that with more data, or with more detailed and specific data labels ('rock' is a genre that has so much variety it may as well be labeled 'music'), we could train a more realistic generative model. It seems that simply increasing training time would not decrease the loss, as for a long period there were simply noisy fluctuations in the loss centered on a stable trendline, although with deep learning models it is possible that it would find some new gradient direction to optimize towards and leave its local minima after more training.

## Libraries used

* [WaveNet](https://github.com/ibab/tensorflow-wavenet) - Used for the model, the training, and the generation
* [Mutagen](https://github.com/quodlibet/mutagen) - Used to retrieve music meta information from the file.
* [Pydub](https://github.com/jiaaro/pydub) - Used to edit and manipulate the music to transform it into wav files.
* [Matplotlib](https://matplotlib.org) - Used for all of the diagrams.

---

Basic Template sourced from: https://github.com/pages-themes/cayman
