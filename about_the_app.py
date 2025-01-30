import streamlit as st
from PIL import Image

agric1 = Image.open('agric1.png')
agric2 = Image.open('agric2.png')
agric3 = Image.open('agric3.png')

about_col1,about_col2 = st.columns([2,1],gap='small')

with about_col1:
    st.markdown("""
    Agriculture being not only the main source of food and also a source of employment, it should be our responsibility to jealously guard it against any destructions.  
    In the process of guarding it, we should put in place any measure that is geared towards detecting and identifying any looming potential
                problems that might destroy it.  

    **Potatoes** `(Starchy tuberous vegetable that is consumed as a staple food in many parts of the world are underground tubers of the plant Solanum tuberosum, a perennial in the nightshade family Solanaceae).` face 2 major diseases that is late blight and early blight that reduces their productivity and even destroys the crop.  

    The purpose of this project is therefore to build a deep learning model [CNN](https://www.ibm.com/think/topics/convolutional-neural-networks) that can help small farmers in identifying problem affecting their potato crops in the farms
                and give link to sources that may help handle the diseases
    """)

with about_col2:
    st.image(agric1)
    st.image(agric3)
    st.image(agric2, caption="source: google")