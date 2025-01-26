import os
import re
import subprocess

mp4Files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.mp4') and not f.endswith("-output.mp4")]

#print(mp4Files)

def evaluateTrackName(trackName, wavFile):
    name = []
    if trackName == "original":
        name = ["Original audio", "und"]
    elif trackName == "en":
        name = ["English audio", "en"]
    elif trackName == "cs":
        name = ["Czech audio", "cs"]
    elif trackName == "sk":
        name = ["Slovak audio", "sk"]
    elif trackName == "es":
        name = ["Spanish audio", "es"]
    elif trackName == "de":
        name = ["German audio", "de"]
    elif trackName == "fr":
        name = ["French audio", "fr"]
    else:
        name = ["Unknown audio", "und"]
    name += [wavFile]
    return name

for mp4File in mp4Files:
    videoFile = os.path.splitext(mp4File)[0]
    print(f"Processing {videoFile}")
    audioPattern = rf"^{videoFile}_A\d+-(.+)\.wav$"
    wavFiles = [f for f in os.listdir() if os.path.isfile(f) and re.match(audioPattern, f)]
    #print(wavFiles)
    audioTracks=[]
    for wavFile in wavFiles:
        match = re.match(audioPattern, wavFile)
        if match:
            trackName = match.group(1)
            audioTracks.append(evaluateTrackName(trackName, wavFile))
    audioTracks.sort(key=lambda x: (x[0] != 'Original audio', x[1]))
    print(audioTracks)
    command = [
        "ffmpeg",
        "-y",
        "-i", f"{mp4File}"
        ]
    for audioTrack in audioTracks:
        command += ["-i", audioTrack[2]]
    audioCounter = 1
    for audioTrack in audioTracks:
        command += ["-map", f"{audioCounter}:a"]
        audioCounter += 1
    
    command += [
        "-map", "0:v"
        ]
    
    audioCounter = 0
    for audioTrack in audioTracks:
        command += [f"-metadata:s:a:{audioCounter}", f"title=\"{audioTrack[0]}\""]
        command += [f"-metadata:s:a:{audioCounter}", f"language=\"{audioTrack[1]}\""]
        audioCounter += 1
    command += [
        "-c:v", "copy",
        "-c:a", "aac",
        "-q:a", "0",
        f"{videoFile}-output.mp4"
        ]
    #print(command)
    try:
        subprocess.run(command, check=True)
        pass
    except subprocess.CalledProcessError as e:
        print(f"Error processing final ffmpeg: {e}")








