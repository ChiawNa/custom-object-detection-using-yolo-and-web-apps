## 🖥️Object Detection, Instances Segmentation, Pose Estimation and Image Classification

This repository demonstrates how to run object detection, instances segmentation, pose estimation and image classification using YOLOv11.

## ⚙️Requirements

Ensure you have the following installed:

- 🐍Python 3.8 or later
- 📦ultralytics library (for YOLOv8)

## 📦Installation and Running the Prediction

```bash
pip install ultralytics
```
```bash
cd yolo11_window_rec
```

```bash
yolo predict model=yolo11n.pt source='images.jpg'
```

## 🎥Result

### i) Object Detection
<img src="https://github.com/user-attachments/assets/bb898df7-f83d-4aaa-bbd8-cebeaf717ddc" width="700">

### ii) Instances Segmentation
<img src="https://github.com/user-attachments/assets/b3e12304-1f72-4a08-b333-2e926d7be498" width="700">

### iii) Pose Estimation
<img src="https://github.com/user-attachments/assets/02812347-0521-4c26-9d15-cd9f00fce602" width="700">

### iv) Image Classification
<img src="https://github.com/user-attachments/assets/7180681d-b056-430d-8853-2861dad404a8" width="700">

## 📚 References

For additional information, visit: 
- https://github.com/ultralytics/ultralytics
- https://docs.ultralytics.com/models/yolo11/
