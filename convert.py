from moviepy.editor import *


def convert_video(video_input_path, video_output_path, black_image_path = "black_background.jpg"):
    # Variables that determine the quality of the video.
    vcodec =   "libx264"
    videoquality = "24"
    # ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
    compression = "veryslow"

    # A black image is used as a canvas and gets resized to 1080x1920
    black_canvas = (ImageClip(black_image_path)
                    .resize((1080,1920)))
 
    # The videoclip gets placed on top the canvas
    clip = (VideoFileClip(video_input_path).
            resize(height=1920).
            # Crop the video on the x-axix, this is what will be shown on the video.
            # You most likely need to experiment with the variables (x1, x2) to get the best result.
            crop(x1=600, x2=2000).
            set_position(("center")))


    # Create the video
    final_clip = CompositeVideoClip([black_canvas, clip])
    final_clip.write_videofile(video_output_path, 
        threads=4, 
        fps=60,
        codec=vcodec,
        preset=compression,
        ffmpeg_params=["-crf", videoquality])

convert_video("input_path.mp4", "output_path.mp4")
