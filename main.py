import cv2, random, time


video = cv2.VideoCapture('My Neighbor Totoro 720p.mp4')

# get the FPS of the movie being played
fps = video.get(cv2.CAP_PROP_FPS)
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
video_length = num_frames / fps


#frame_id = int(fps * (minutes * 60 + seconds) + ms)
def call_pic():
    frame_id = random.randint(0, num_frames)
    print('frame id =', frame_id)

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()
    cv2.namedWindow("Movie", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("Movie", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


#imwrite saves the image to the computer, right now we don't need that
#cv2.imwrite('my_video_frame.png', frame)
active = True

def call_me():
    while active:
        call_pic()
        time.sleep(10)


call_me()