until python3 train.py --data_dir=.../Data --gc_channels=32 --checkpoint_every=10 --batch_size=2 --logdir=.../Output >> results.txt 2>&1;do
	echo "Restarting the service at $(date)" >> results.txt
	sleep 10
done
