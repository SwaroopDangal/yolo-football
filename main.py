from utils import read_video, save_video
from trackers import Tracker

def main():
    #read video
    video_frames = read_video("video/08fd33_4.mp4")

    #Initalize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path='stubs/track_stubs.pkl')

    ##draw o/p
    # draw object tracks

    output_video_frames=tracker.draw_annotations(video_frames,tracks)


    # Save video
    save_video(output_video_frames, "output/output_video.avi")


if __name__=='__main__':
    main()
