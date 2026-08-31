from utils import read_video, save_video

def main():
    #read video
    video_frames = read_video("video/08fd33_4.mp4")

    # Save video
    save_video(video_frames, "output/output_video.avi")


if __name__=='__main__':
    main()