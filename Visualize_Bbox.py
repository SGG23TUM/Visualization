from PIL import Image, ImageDraw, ImageFont
import json

def draw_bounding_boxes_and_labels(image_path, json_data):
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 30)  

        for image_info in json_data:
            for obj in image_info['objects']:
                
                left, top, right, bottom = obj['x'], obj['y'], obj['x'] + obj['w'], obj['y'] + obj['h']

                
                draw.rectangle([left, top, right, bottom], outline='red', width=3)

                
                label = obj['names'][0] if obj['names'] else 'Unknown'
                draw.text((left, top), label, fill='blue', font=font)

        img.show()


json_file_path = 'predictions_img8908.json'
with open(json_file_path, 'r') as file:
    json_data = json.load(file)


image_path = 'test_image/IMG_8908.JPG'


draw_bounding_boxes_and_labels(image_path, json_data)
