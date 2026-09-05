from utils import read_video, save_video
from trackers import Tracker
from team_assigner import TeamAssigner
import cv2

def main():
    #read video
    video_frames = read_video("video/08fd33_4.mp4")
    print(f"Video read complete.")

    #Initalize Tracker
    tracker = Tracker('models/best.pt')
    print("Tracking objects in video...")

    tracks = tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path='stubs/track_stubs.pkl')
    print(f"Tracking completed.")
    

     # Interpolate Ball Positions
    print("Interpolating ball positions...")
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])
    print(f"Interpolation completed.")

    # Assign Teams
    print("Assigning teams to players...")
    team_assigner = TeamAssigner() 
    team_assigner.assign_team_color(video_frames[0],tracks['players'][0])

    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    print(f"Team assignment completed.")

    print(f"Drawing annotations on video frames...")

    ##draw o/p
    # draw object tracks

    output_video_frames=tracker.draw_annotations(video_frames,tracks)

    print(f"Drawing completed.")
    print(f"Saving output video...")


    # Save video
    save_video(output_video_frames, "output/output_video.avi")


if __name__=='__main__':
    main()
