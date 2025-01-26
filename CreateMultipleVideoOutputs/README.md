# CreateMultipleVideoOutputs
Tools to create multiple video outputs

Description:
------------
Tools provide automatic following functionalities:
- create various lower resolution video files (4k -> 1080p, 720p, 360p)
- create various lower resolution HLS (http live streaming) videos (4k -> 1080p, 720p, 360p) with multiple language support (audio and subtitles) and master.m3u8 playlist

Funtionality:
-------------
The allows single mp4 file which expects to have multiple language audio tracks (to be implemented later) and the original footage in one language.

The expectation is to have single video, for example:
```
video-test-instructions.mp4
video-test-instructions_cs.srt
video-test-instructions_en.srt
video-test-instructions_es.srt
```

Usecase:
--------
Allow to prepare youtube videos.
Allow custom site video streaming.

Target example:
---------------


Dependencies:
-------------
See Dockerfile

Usage:
------

