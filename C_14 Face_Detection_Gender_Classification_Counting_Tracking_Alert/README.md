<H1 align="center">Face Detection and Gender Classification using YOLOv8</H1>


## ⚙️Steps to run Code

- Clone the repository
```
gdown "https://drive.google.com/uc?id=1AHy2I7uNCgggnHDgHgF9NNmkTI8DFTsc&confirm=t"
```
- Goto the cloned folder.
```
cd FaceDetectionYOLOv8
```
- Install the dependecies
```
pip install -e '.[dev]'

```

- Setting the Directory.
```
cd ultralytics/yolo/v8/detect
```


- Downloading a Weights from the Google Drive
```
gdown "https://drive.google.com/uc?id=1nzT3up9NZ4MZFUZaqQexC9gl5RJ-fiqv&confirm=t"
```
- Downloading a Sample Video from the Google Drive
```
gdown "https://drive.google.com/uc?id=1Rka-b-nUCEa6CaA44kxp752ZnAGVlb7W&confirm=t"
gdown "https://drive.google.com/uc?id=1wQNjDU0bb33YlZa14KPzri7fMyh_NBBg&confirm=t"

```
- Run the code with mentioned command below.
```
python predict.py model='best.pt' source='demovideo.mp4'
```

## 🎥Demo

Watch the full demo video on YouTube: https://youtu.be/Yabmx0fYNwA
