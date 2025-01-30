import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import time


st.header("NB: 👇") 
st.warning("ONLY LOAD POTATO IMAGES FOR CORRECT CLASSIFICATION!!!")
#Loading the model, defining extensions and defining class labels
model = tf.keras.models.load_model('version1.h5')
extension = ['png','jpg','jpeg','img']
class_labels = ["Early blight","Late blight","Healthy"]

loaded_image = st.file_uploader(label='Upload an image to predict',type=extension)

#Defining the preparation function that returns the expanded image
def load_and_prepare(loaded_image):
    image = Image.open(loaded_image)
    image_array = np.array(image)
    rgb_image = image_array[:,:,:3]
    expanded_image = np.expand_dims(rgb_image,axis=0)

    return expanded_image

if loaded_image is not None:
    progress_bar = st.progress(0)

    for percent_completed in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_completed+1)

    input_image = Image.open(loaded_image)
    st.image(input_image,caption='loaded image')
    st.success('Image loaded successfully!')
    
    #Making prediction
    prediction_image = load_and_prepare(loaded_image=loaded_image)
    predicted_array = model.predict(prediction_image)
    flattened_predicted_array = predicted_array.flatten()

    predicted_class_index = np.argmax(predicted_array)
    predicted_class_label = class_labels[predicted_class_index]
    confidence_level = flattened_predicted_array[predicted_class_index]*100

    if predicted_class_index==2:
        st.write(f"I am {confidence_level:.4f} % confident that your crop is healthy")
    else:
        st.write(f"I am {confidence_level:.4f} % confident that the crop is infected by {predicted_class_label}")

    #Referral for remedy
    if predicted_class_index == 0:
        st.markdown("""Sad news! 😢, your crops are infected with `Early blight`.  
                    But Hey! Don't you worry visit [Koppert](https://www.koppert.com/plant-diseases/early-blight/) for help and
                    rescue your crops.""")
    elif predicted_class_index == 1:
        st.markdown("""Sad news! 😢, your crops are infected with `Late blight`.  
                    But Hey! Don't you worry visit 
                    [AHDB](https://archive.ahdb.org.uk/knowledge-library/late-blight-disease-and-its-management-in-potatoes#:~:text=persist%20in%20soil.-,Symptoms,the%20lesions%20under%20moist%20conditions.)  
                    for help and rescue your crops""")
    else:
        st.success("Keep going! your crops are healthy 😄")
else:
    st.info("Please upload an image")