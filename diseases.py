import streamlit as st
from PIL import Image


early = Image.open('early.png')
late = Image.open('late.png')
healthy = Image.open('healthy.png')

st.markdown("""
Just like any other sectors that are faced with different challenges, agriculture sector is not excempted from this problem.  

Farmers experience several problems that hinder their optimum production ranging  from financial to disease problems, whether growing crops or rearing animals.  

Potatoe farmers (iris potatoe) are faced with mainly three typesn of diseases as discussed below.

""")

st.markdown("---")
st.subheader('Early blight')
early_col1,early_col2 = st.columns(2)
with early_col1:
    st.image(early,caption='source: google')
with early_col2:
    st.markdown("""Early blight of potato is caused by the fungus, Alternaria solani, which can cause disease in potato, tomato, other members of the potato family, and some mustards.
                This disease, also known as target spot, rarely affects young, vigorously growing plants.
                It is found on older leaves first. Early blight is favored by warm temperatures and high humidity.
                """)
    st.markdown("""[learn more](https://www.seipasa.com/en/blog/early-blight-in-potato-identification-and-control/)""")

st.markdown("---")
st.subheader('Late blight')
late_col1,late_col2 = st.columns(2,gap='small')
with late_col1:
    st.image(late,caption='source: google')
with late_col2:
    st.markdown("""
Late blight is a potato disease caused by the fungus Phytophthora infestans that can also affect tomatoes. It's considered the most destructive potato disease.
The primary host is potato, but P. infestans also can infect other solanaceous plants, including tomatoes, petunias and hairy nightshade.
""")
    st.markdown("[learn more](https://byjus.com/biology/late-blight-of-potato/)")

st.markdown("---")
st.subheader('Healthy potato')
healthy_col1,healthy_col2 = st.columns(2,gap='small')
with healthy_col1:
    st.image(healthy,caption='source: google')
with healthy_col2:
    st.markdown("""
                A whole and unblemished potato is a potato tuber that is intact, without cuts, bruises, soft spots, or other damage to its skin or flesh.
                It is free from sprouts (unless intentionally sprouted for seed potatoes) and lacks any green discoloration, which indicates the presence of solanine, a potentially toxic compound.
                Essentially, it's a potato in its complete, undamaged, and natural state, ready for cooking or storage.
                """)