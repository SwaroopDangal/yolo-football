from utils import read_video, save_video
from trackers import Tracker
import cv2

def main():
    #read video
    video_frames = read_video("video/08fd33_4.mp4")

    #Initalize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path='stubs/track_stubs.pkl')

    # save cropped image of player
    for track_id, player in tracks['players'][0].items():
        bbox = player['bbox']
        frame = video_frames[0]

        #crop box from frame
        cropped_image = frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]

        #save cropped image
        cv2.imwrite(f'output/cropped_image.jpg', cropped_image)

        break


    

    ##draw o/p
    # draw object tracks

    output_video_frames=tracker.draw_annotations(video_frames,tracks)



    # Save video
    save_video(output_video_frames, "output/output_video.avi")


if __name__=='__main__':
    main()
