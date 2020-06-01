#!/bin/bash

echo "[BASH] Downloading test media files ..."
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/cars.mp4 -q --show-progress --no-clobber
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/passby.mp4 -q --show-progress --no-clobber
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/ped03.mp4 -q --show-progress --no-clobber
wget https://objectstorage.ca-toronto-1.oraclecloud.com/n/yzpqsgba6ssd/b/bucket-20200425-1646-media/o/shinjuku.mp4 -q --show-progress --no-clobber
echo "[BASH] Download finished ..."
