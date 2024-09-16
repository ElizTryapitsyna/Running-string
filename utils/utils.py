import cv2
import numpy as np
import transliterate
import movis as mv


def create_video_opencv(message: str):
    if len(message) > 50:
        title = message[:50]
    elif len(message) == 0:     #creating the title
        title = 'empty-video'
    else:
        title = message
    # ь is used to work with latin symbols
    title = transliterate.slugify('ь' + title)
    width, height = 100, 100
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    out = cv2.VideoWriter(f"media/videos/{title}.mp4", fourcc, 24, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Parameters of the font
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 10
    font_thickness = 10
    font_color = (255, 255, 255)

    message_size = cv2.getTextSize(message, font, font_scale, font_thickness)
    x, y = width, height // 2

    speed = 2 * message_size[0][0] // (3 * 24)
    video_dur = 3 * 24
    while video_dur > 0:
        frame.fill(0)
        x -= speed
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)
        video_dur -= 1

    out.release()

    return {'title': title, 'path': f"videos/{title}.mp4"}


def convert_to_h264(file):
    intro = mv.layer.Video(file)
    scene = mv.layer.Composition(size=(1920, 1080), duration=0.1)
    masdin = mv.concatenate([intro, scene])
    masdin.write_video(file)