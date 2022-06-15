#!/bin/bash

# Remove annoying spaces in file names.
for f in *\ *; do mv "$f" "${f// /_}"; done

##
# convert mp3 files to wave
##

for file in *.mp3; do
   ffmpeg -i "$file" -acodec pcm_s16le -ac 1 -ar 44100 "${file%.mp3}".wav
done
