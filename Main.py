import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ASCIIGradient = [" ", ".", "'", "`", "^", "\"", ",", ":", ";", "!", "i", "l", "I", "?", "/", "|", "(", ")", "1", "t", "f", "L", "T", "F", "E", "X", "H", "#", "@", "8", "&", "%", "$"]
video_path = "res/one_last_breath.mp4"
output_video_path = "res/one_last_breath_ascii.mp4"
frame_rate = 6

#128 / 72

# load video from file
video_capture = cv2.VideoCapture(video_path)
fps = video_capture.get(cv2.CAP_PROP_FPS)
frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
extract_interval = int(fps / frame_rate)

frames = []

# extract each frame from the video and save in list
frame_number = 0
while True:
    success, frame = video_capture.read()
    if not success:
        break

    if frame_number % extract_interval == 0:
        frames.append(frame)
    frame_number += 1

video_capture.release()

#grayscale each frame
for frame in frames:
    for i in range(len(frame)):
        for j in range(len(frame[0])):
            value = int((int(frame[i][j][0]) + int(frame[i][j][1]) + int(frame[i][j][2])) * 0.33)
            frame[i][j][0] = value
            frame[i][j][1] = value
            frame[i][j][2] = value

ascii_frames = []
ppc = 8 # pixels per character

for frame in frames:
    frame_text = []
    for i in range(0, len(frame), ppc):
        for j in range(0, len(frame[0]), ppc):
            sum = 0
            for x in range(ppc):
                for y in range(ppc):
                    sum += int(frame[i+x][j+y][0])
            avg = float(sum) / ppc**2
            avg = avg / 25.5
            idx_con = 10/(len(ASCIIGradient)-1)
            character_idx = int(round(avg/idx_con))
            frame_text.append(ASCIIGradient[character_idx])
        frame_text.append("\n")
    ascii_frames.append(frame_text)

font = ImageFont.truetype("res/CascadiaMono.otf", 11)

generated_frames = []
for frame in ascii_frames:
    img = Image.new("RGB", (970, 680), "black")
    draw = ImageDraw.Draw(img)
    text = " ".join(frame)
    text_position = (0, 0)
    text_color = (255, 255, 255)
    draw.text(text_position, text, fill=text_color, font=font)
    cv_image = np.array(img)
    generated_frames.append(cv_image)

video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), frame_rate, (970, 680))

for frame in generated_frames:
    video.write(frame)

cv2.destroyAllWindows()
video.release()