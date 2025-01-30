import tensorflow as tf
import streamlit as st
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("version1.h5")
classes = ["Early blight","Late blight","Healthy"]

image = st.file_uploader(label="Upload an image to predict",
                         type=["jpg",'jprg','png'])

if image is not None:
    image = Image.open(image)
    st.image(image,caption='Loaded image')

    image = np.array(image)
    image = np.expand_dims(image,axis=0)

    prediction = np.argmax(model.predict(image))
    confidence = model.predict(image).flatten()[prediction]*100
    st.write(f"The predicted label is : {prediction}-{classes[prediction]}")
    st.write("I am",round(confidence,4),"confidence that it is",classes[prediction])