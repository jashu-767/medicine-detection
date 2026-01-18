import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

train_dir = "C:/model_split/train"
val_dir = "C:/model_split/val"
datagen = ImageDataGenerator(rescale=1./255,
                             rotation_range=30,
                             zoom_range=0.2,
                             horizontal_flip=True)

train_gen = datagen.flow_from_directory(train_dir, target_size=(224, 224), batch_size=32)
val_gen = datagen.flow_from_directory(val_dir, target_size=(224, 224), batch_size=32)
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
preds = Dense(train_gen.num_classes, activation="softmax")(x)
model = Model(inputs=base_model.input, outputs=preds)
for layer in base_model.layers:
    layer.trainable = False
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(train_gen, validation_data=val_gen, epochs=10)
model.save("C:/model/medicine_model.h5")
print("✅ Model training complete and saved.")
