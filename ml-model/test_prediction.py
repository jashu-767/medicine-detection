from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
model = load_model("C:/model/medicine_model.h5")
train_dir = "C:/model_split/train"
class_names = sorted(os.listdir(train_dir))  
img_path ="C:\model\\aggrex\\20210831_130748.jpg"
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0) / 255.0
pred = model.predict(x)
predicted_label = class_names[np.argmax(pred)]
confidence = float(np.max(pred))
print("Predicted:", predicted_label, "with confidence:", confidence)
