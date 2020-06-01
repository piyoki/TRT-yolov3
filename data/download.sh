#!/bin/bash

echo "[BASH] Downloading test media files ..."
#mkdir data/videos
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/cars.mp4 -q --show-progress --no-clobber -O data/videos/cars.mp4
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/passby.mp4 -q --show-progress --no-clobber -O data/videos/passby.mp4
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/ped03.mp4 -q --show-progress --no-clobber -O data/videos/ped.mp4
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/shinjuku.mp4 -q --show-progress --no-clobber -O data/videos/shinjuku.mp4
echo "[BASH]  Download finished ..."
