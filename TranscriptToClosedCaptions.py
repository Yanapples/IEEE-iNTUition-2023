import cv2
import pysubs2

videoname = 'black5s'
subtitlefile = 'subtitles'

# Load the video and subtitles
cap = cv2.VideoCapture('black5s.mp4')
subs = pysubs2.load('black5s.srt')

# Synchronize the subtitles with the video
# shift = subs.shift_seconds(-2)  # shift subtitles by -2 seconds
# subs = subs.shift(shift)

def shift(subs, ms):
    for line in subs:
        line.start += ms
        line.end += ms

# Loop through the frames in the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Get the current time in seconds
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000

    # Find the subtitle that matches the current time
    subtitle = subs.shift(current_time).as_list()[0]

    # Add the subtitle text to the frame
    cv2.putText(frame, subtitle.text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the frame with the subtitles
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video and close the window
cap.release()
cv2.destroyAllWindows()
