# Yolo Football ⚽

## Demo

        <video src="https://github.com/SwaroopDangal/yolo-football/raw/main/output/output_video.avi" controls width="600"></video>
>

A computer vision project for analyzing football (soccer) match footage using **YOLO** object detection. The pipeline detects and tracks players, referees, and the ball, then layers on higher-level match analytics like team assignment, ball possession, player speed/distance, and camera movement compensation.

## Features

- **Object Detection & Tracking** — Detects players, referees, and the ball in each video frame and tracks them across frames (`trackers/`).
- **Team Assignment** — Groups players into teams based on jersey color clustering (`team_assigner/`).
- **Ball Possession** — Assigns the ball to the nearest player each frame to estimate possession (`player_ball_assigner/`).
- **Speed & Distance Estimation** — Calculates each player's speed and total distance covered (`speed_and_distance_estimator/`).
- **Camera Movement Compensation** — Estimates and corrects for camera pans/movements so player positions stay accurate (`camera_movement_estimator/`).
- **Perspective / View Transformation** — Maps pixel coordinates onto real-world pitch coordinates (`view_transformer/`).
- **Custom Model Training** — Includes resources for training/fine-tuning a YOLO model on football footage (`training/`).
- **Annotated Output** — Produces an output video with overlays (player IDs, team colors, ball possession, speed, etc.) saved to `output/`.

## Project Structure

```
yolo-football/
├── camera_movement_estimator/     # Estimates camera motion between frames
├── development-and-analysis/      # Notebooks / scripts for exploration and analysis
├── output/                        # Generated annotated output videos
├── player_ball_assigner/          # Assigns ball possession to nearest player
├── speed_and_distance_estimator/  # Computes player speed & distance
├── team_assigner/                 # Clusters players into teams by jersey color
├── trackers/                      # YOLO-based detection + tracking logic
├── training/                      # Model training resources/notebooks
├── utils/                         # Shared helper functions (video I/O, bbox math, etc.)
├── view_transformer/              # Perspective transform to real-world pitch coords
├── main.py                        # End-to-end pipeline entry point
├── yolo_inference.py              # Standalone script for quick YOLO inference checks
└── readme.md
```

## Requirements

- Python 3.8+
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- OpenCV
- NumPy
- scikit-learn (for team color clustering)
- pandas (optional, for analysis)

Install dependencies:

```bash
pip install ultralytics opencv-python numpy scikit-learn pandas
```

> If a `requirements.txt` is added to the repo, prefer `pip install -r requirements.txt` instead.

## Usage

1. Place your input football match video in an `input/` (or similar) directory.
2. Make sure a trained YOLO model (e.g. `best.pt`) is available and referenced correctly in `main.py`.
3. Run the full analysis pipeline:

   ```bash
   python main.py
   ```

4. To quickly test raw YOLO detections without the full pipeline:

   ```bash
   python yolo_inference.py
   ```

5. The annotated output video will be written to the `output/` directory.

## Training a Custom Model

The `training/` folder contains resources for training a YOLO model on a custom football dataset (e.g., via Roboflow or a similarly labeled dataset) so detection is tuned specifically for players, referees, and the ball.

## Notes

- This README was written based on the repository's folder/file layout, since the repo currently doesn't include a detailed one. Update the **Usage** section with the exact input/output paths and model file names used in `main.py` once confirmed.
- Consider adding a `requirements.txt`, sample input/output video or GIF, and license file to make the repo easier for others to run.

## License

No license specified yet — consider adding one (e.g., MIT) if you intend for others to use or contribute to this project.
