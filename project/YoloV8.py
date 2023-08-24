from ultralytics import YOLO
import torch
from PIL import Image


class YoloV8:

    def __init__(self, modelName):
        self.model = YOLO(modelName)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def predict(self, path_image):
        results = self.model(path_image, device=self.device)
        im_array = results[0].plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image

        return im
