#!/bin/bash

mkdir data/videos
wget https://hidden-boat-623a.keviny-cloud.workers.dev/DeepLearning/sample_videos/cars.mp4 -q --show-progress --no-clobber -O data/videos/cars.mp4
wget https://hidden-boat-623a.keviny-cloud.workers.dev/DeepLearning/sample_videos/passby.mp4 -q --show-progress --no-clobber -O data/videos/passby.mp4
wget https://hidden-boat-623a.keviny-cloud.workers.dev/DeepLearning/sample_videos/ped.mp4 -q --show-progress --no-clobber -O data/videos/ped.mp4
wget https://hidden-boat-623a.keviny-cloud.workers.dev/DeepLearning/sample_videos/shinjuku.mp4 -q --show-progress --no-clobber -O data/videos/shinjuku.mp4
cd ..
echo "[BASH]  Download finished ..."
