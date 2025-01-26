# VideoAndAudioAutoMerge

Description:
------------
Tools provide automatic video conversion under the expectation that the video file was created by kdenlive (or any other tools) and render was targetted to the output wav files containing language footages

Funtionality:
-------------
The script searches all mp4 files and corresponding audio footage files with different language footages.

The expectation is for example:
```
video-test-instructions.mp4
video-test-instructions_A1-original.wav
video-test-instructions_A2-cs.wav
video-test-instructions_A3-es.wav
video-test-instructions_A4-en.wav
```

what corresponds to the situation when kdenlive outputs video without audio tracks and (in this case) four audio tracks, original and 3 variants.

All videos in the current folder are processed.

Usecase:
--------
It is expected that original track contains all audio.
Each language variant contains only that audio which corresponds to the spoken word. E.g. if only czech language is used in cs track, all other tracks are empty.

Use case in this case is:
- to further automatically create subtitles from each track in related language (other scripts)
- to create automatic dubbing for each language (other scripts)

Target example:
---------------
For the example above, the following command will be produced:
```
ffmpeg -i video-test-instructions.mp4 \
-i video-test-instructions_A1-original.wav \
-i video-test-instructions_A2-cs.wav \
-i video-test-instructions_A3-es.wav \
-i video-test-instructions_A4-en.wav \
-y \
-map 0:v -map 1:a -map 2:a -map 3:a -map 4:a \
-metadata:s:a:0 title="Original audio" -metadata:s:a:0 language=und \
-metadata:s:a:1 title="Czech audio" -metadata:s:a:1 language=cs \
-metadata:s:a:2 title="Spanish audio" -metadata:s:a:2 language=es \
-metadata:s:a:3 title="English audio" -metadata:s:a:3 language=en \
-c:v copy -c:a aac -q:a 0 output-video-test-instructions.mp4
```

Dependencies:
-------------
```
ffmpeg
python
```

Usage:
------
```
python merge.py
```


