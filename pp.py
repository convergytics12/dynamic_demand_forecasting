import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)

filelist = []
dict={}
for i in uploaded_files:
    #dict[i]=i.name
    st.write(i)
    
st.write(dict)
    

for file in uploaded_files:
    st.write(file)
    filelist.append(file.name)
    df1 = pd.read_excel(file)
    st.write(df1)
selected_file = st.selectbox("Select a file:", filelist)

        
        
        

