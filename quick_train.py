import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

dataset_path = "dataset"

datagen = ImageDataGenerator(rescale=1./255)

train = datagen.flow_from_directory(
    dataset_path,
    target_size=(128, 128),
    batch_size=4,
    class_mode='categorical'
)

model = tf.keras.models.Sequential([
    tf.keras.Input(shape=(128,128,3)),

    tf.keras.layers.Conv2D(16, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(train.num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(train, epochs=5)

model.save("model/image_model.h5")

print("✅ Model trained and saved!")
