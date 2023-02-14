#!/bin/bash

mkdir data/videos
wget https://objectstorage.us-sanjose-1.oraclecloud.com/n/axdjylkbplt1/b/artifacts/o/cars.mp4 -q --show-progress --no-clobber -O data/videos/cars.mp4
wget https://objectstorage.us-sanjose-1.oraclecloud.com/n/axdjylkbplt1/b/artifacts/o/passby.mp4 -q --show-progress --no-clobber -O data/videos/passby.mp4
wget https://objectstorage.us-sanjose-1.oraclecloud.com/n/axdjylkbplt1/b/artifacts/o/ped.mp4 -q --show-progress --no-clobber -O data/videos/ped.mp4
wget https://objectstorage.us-sanjose-1.oraclecloud.com/n/axdjylkbplt1/b/artifacts/o/shinjuku.mp4 -q --show-progress --no-clobber -O data/videos/shinjuku.mp4
cd ..
echo "[BASH]  Download finished ..."
