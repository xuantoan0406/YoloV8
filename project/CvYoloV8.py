import gradio as gr
from project.YoloV8 import YoloV8
from core import config

classify = YoloV8(config.C_YOLOV8)
detection = YoloV8(config.D_YOLO_V8)
segment = YoloV8(config.SEGMENT)


def image_label(model, path_image):
    if model == "classify":
        output = classify.predict(path_image)
    elif model == "detection":
        output = detection.predict(path_image)
    else:
        output = segment.predict(path_image)

    return output


demo = gr.Interface(
    image_label,
    [gr.Dropdown(
        ["classify", "detection", "segment"], label="Models", info="Will add more animals later!",value="detection"
    ),
        gr.Image(type="pil"),
    ],
    outputs='image',
    examples=[
        [None,"assets/images/objectDetection/anh-cho-cuoi.jpg"],
        [None,"assets/images/objectDetection/Hinh-anh-cho-ngau.jpg"],
    ],

)

demo.launch()
