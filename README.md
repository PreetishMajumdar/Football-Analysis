# Football Analysis Live  
**Real-Time Football Match Analysis with Computer Vision and Deep Learning**

## Table of Contents
- [Overview](#overview)  
- [Features](#features)  
- [Demo](#demo)  
- [Project Architecture](#project-architecture)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Sample Results](#sample-results)  
- [Future Work](#future-work)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

## Overview  
**Football Analysis Live** is an end-to-end platform for real-time football match analysis, leveraging state-of-the-art computer vision and deep learning techniques. The system processes live video feeds to detect and track players, referees, and the ball, automatically assigns teams, and generates advanced analytics and visualizations. This project aims to empower coaches, analysts, and fans with actionable insights and tactical data during live matches.

## Features
- **Real-Time Object Detection:** Detects players, referees, goalkeepers, and the ball using YOLOv8.  
- **Multi-Object Tracking:** Maintains consistent IDs for all entities using ByteTrack.  
- **Automatic Team Assignment:** Uses clustering algorithms to group players by jersey color.  
- **Advanced Analytics:** Calculates possession, pass networks, player speeds, distances covered, and expected goals (xG).  
- **Heatmaps & Tactical Visualizations:** Generates player heatmaps, pass maps, Voronoi diagrams, and territory control visuals.  
- **Perspective Transformation:** Maps player positions from video frames to real-world field coordinates.  
- **Intuitive Dashboards:** Presents live analytics and visualizations for easy interpretation.  
- **Modular & Extensible:** Designed for easy integration and future feature expansion.

## Demo
![Demo GIF](demo/demo.gif)  
*System processes a live football match and generates real-time analytics!*

## Project Architecture
```mermaid
graph TD
    A[Live Video Feed] --> B[YOLOv8 Object Detection]
    B --> C[ByteTrack Multi-Object Tracking]
    C --> D[Team Assignment (K-means Clustering)]
    D --> E[Perspective Transformation]
    E --> F[Analytics Engine]
    F --> G[Visualization Dashboard]
```

## Technologies Used
- Python 3.x  
- OpenCV – Image and video processing  
- YOLOv8 – Object and pose detection  
- ByteTrack – Multi-object tracking  
- scikit-learn – Clustering (K-means)  
- NumPy & Pandas – Data processing  
- Matplotlib / Plotly – Visualization  
- UMAP – Embedding & clustering  
- SigLIP – Visual embeddings (optional)  
- Streamlit / Dash – Interactive dashboards (optional)

## Installation

### Clone the Repository
```bash
git clone https://github.com/anonimity69/Football-Analysis-Live.git
cd Football-Analysis-Live
```

### Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Download YOLOv8 Weights  
Download pre-trained YOLOv8 weights for football detection and place them in the `weights/` directory.

## Usage

### Run the Main Script
```bash
python main.py --video path/to/your/video.mp4
```

Or, for live webcam:
```bash
python main.py --webcam 0
```

### View Results  
Analytics and visualizations will be displayed in the output window or dashboard.

### Configuration  
Adjust parameters in `config.yaml` for custom settings (model paths, detection thresholds, etc.).

## Project Structure
```
Football-Analysis-Live/
│
├── data/                # Sample videos and images  
├── weights/             # Pre-trained YOLOv8 models  
├── src/                 # Source code  
│   ├── detection.py     # Object detection pipeline  
│   ├── tracking.py      # Multi-object tracking  
│   ├── team_assign.py   # Team assignment logic  
│   ├── analytics.py     # Statistical analysis  
│   ├── visualization.py # Visualization utilities  
│   └── utils.py         # Helper functions  
├── demo/                # Demo files and outputs  
├── requirements.txt     # Python dependencies  
├── config.yaml          # Configuration file  
└── main.py              # Main entry point  
```

## Sample Results

| Feature              | Example Output                 |
|----------------------|--------------------------------|
| Player Detection     | ![](demo/player_detection.png) |
| Pass Network         | ![](demo/pass_network.png)     |
| Tactical Dashboard   | ![](demo/dashboard.png)        |

## Future Work
- Enhance ball tracking accuracy during occlusion  
- Add player re-identification across multiple camera angles  
- Integrate live data feeds from external providers  
- Expand analytics to include more advanced metrics (e.g., pressing intensity, tactical formations)  
- Deploy as a web-based or mobile application  

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for suggestions, bug fixes, or new features.

## License
This project is licensed under the MIT License.

## Contact
For questions, feedback, or collaboration, please reach out via GitHub Issues or connect with me on [LinkedIn]([https://www.linkedin.com/](https://www.linkedin.com/in/preetish-majumdar-75296b211/)).

---

Empowering football analysis with the power of AI and real-time data!
