# Summary - Michael
# Procedure - Myles w/Michael
## Link source code
## Link wavenet tensorflow code
## Push Trained model
## Push audio samples
clear && python3 train.py --data_dir=/media/maister/Seagate\ Backup\ Plus\ Drive/Stuff/Data/ --gc_channels=32 --checkpoint_every=1 --batch_size=2

clear && python3 train.py --data_dir=/media/maister/Seagate\ Backup\ Plus\ Drive/Stuff/Data/ --gc_channels=32 --checkpoint_every=1 --batch_size=2

clear && python3 generate.py --samples 16000 --gc_channels=32 --gc_cardinality=5 --gc_id=0 --wav_out_path raplh.wav logdir/train/2019-11-23T17-05-09/model.ckpt-30
## Pull the loss of the training model
Python scripting + bash script?
# Links - Myles && Michael
# Summarize the results
## Print the logs
## Diagram of the loss functionality with overlay of how "musical" they sound