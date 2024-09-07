import subprocess, sys, time, kintone, iotutils
from iotutils import getCurrentTimeStamp

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

# Duration: Length of a video to be taken in seconds
#
def takeVid(duration: float):
    timeStamp = getCurrentTimeStamp()
    vidFile = "videos/" + timeStamp + ".h264"
    
    command = "libcamera-vid -n -t " + str(int(float(duration) * 1000)) + " -o " + vidFile
    status = subprocess.run(command, capture_output=True, shell=True)
    if status.returncode == 0:
        print(timeStamp + " Video captured (" + str(duration) + " seconds).")
    else:
        print("Failed to capture a video")
        sys.exit()
    
    mp4File = "videos/" + timeStamp + ".mp4"
    command2 = "ffmpeg -y -i " + vidFile + " " + mp4File
    status = subprocess.run(command2, capture_output=True, shell=True)
    if status.returncode == 0:
        print(timeStamp + " MP4 file conversion completed.")
    else:
        print("Failed in MP4 file conversion.")
        sys.exit()

    fileKey = kintone.uploadFile(subDomain=sdomain,
                                 apiToken=token,
                                 filePath=mp4File)
    if fileKey is None:
        sys.exit()

    memo = "Video taken by the Underwater Eye system"
    payload = {"app": appId,
               "record": {"photo": {"value": [{"fileKey": fileKey}] },
                          "memo": {"value": memo} }}
    recordId = kintone.uploadRecord(subDomain=sdomain,
                                    apiToken=token,
                                    record=payload)
    if recordId is None:
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        takeVid(5)
    else:
        takeVid(float(sys.argv[1]))

