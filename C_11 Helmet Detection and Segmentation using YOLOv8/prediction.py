from ultralytics import YOLO

#Initialize YOLO with the Model Name
model = YOLO("best.pt")

##Predict Method Takes all the parameters of the Command Line Interface

model.predict(source='bike2.mp4', save=True, conf=0.5, save_txt=True)
# model.export(format="onnx")

