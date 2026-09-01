from utils import read_video, save_video
from trackers import Tracker

def main():
    #read video
    video_frames = read_video("video/08fd33_4.mp4")

    #Initalize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path='stubs/track_stubs.pkl')


    # Save video
    save_video(video_frames, "output/output_video.avi")


if __name__=='__main__':
    main()