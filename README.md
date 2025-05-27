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
- **Real-Time Object Detection**: Detects players, referees, goalkeepers, and the ball using YOLOv8.  
- **Multi-Object Tracking**: Maintains consistent IDs for all entities using ByteTrack.  
- **Automatic Team Assignment**: Uses clustering algorithms to group players by jersey color.  
- **Advanced Analytics**: Calculates possession, pass networks, player speeds, distances covered, and expected goals (xG).  
- **Heatmaps & Tactical Visualizations**: Generates player heatmaps, pass maps, Voronoi diagrams, and territory control visuals.  
- **Perspective Transformation**: Maps player positions from video frames to real-world field coordinates.  
- **Intuitive Dashboards**: Presents live analytics and visualizations for easy interpretation.  
- **Modular & Extensible**: Designed for easy integration and future feature expansion.

## Demo  
![Demo](demo/demo.gif)  
*The system processes a live football match and generates real-time analytics!*

## Project Architecture  
```mermaid
graph TD  
    A[Live Video Feed] --> B[YOLOv8 Object Detection]  
    B --> C[ByteTrack Multi-Object Tracking]  
    C --> D[Team Assignment (K-means Clustering)]  
    D --> E[Perspective Transformation]  
    E --> F[Analytics Engine]  
    F --> G[Visualization Dashboard]
