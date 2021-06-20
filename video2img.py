import cv2
import os

STANDARD_VIDEO_FORMATS = ['avi', 'mp4', 'mp3', 'mov']

def convert(videoFile, outputFolder=None, recurse=False):
    if not os.path.exists(videoFile):
        raise FileNotFoundError(videoFile)

    if outputFolder == None:
        outputFolder = videoFile.split('.')[0]
    
    if recurse:
        if os.path.isdir(videoFile):
            print("inside :", videoFile)
            for item in os.listdir(videoFile):
                convert(f"{videoFile}/{item}", f"{outputFolder}/{item.split('.')[0]}", recurse)
            return
        else:
            if videoFile.split('.')[1] not in STANDARD_VIDEO_FORMATS:
                print(f"Cannot convert {videoFile}, UNSUPPORTED FORMAT : {videoFile.split('.')[1]}")
                return
    
    if not os.path.isdir(outputFolder):
        os.makedirs(outputFolder)

    try:
        cap = cv2.VideoCapture(videoFile)
    except:
        pass

    i=0
    while(cap.isOpened()):
        try:
            ret, frame = cap.read()
            if ret == False:
                break
            cv2.imwrite(f'{outputFolder}/frame_{i}.jpg', frame)
            i+=1
        except:
            pass


if __name__ == '__main__':
    demoFile = "demo"
    outPut   = "output"

    convert(demoFile, outPut, True)

    print(f"successfully converted {demoFile} to images and stored in {outPut}")
