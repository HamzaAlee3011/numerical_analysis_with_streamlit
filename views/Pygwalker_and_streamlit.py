import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

# st.set_page_config(layout='wide')
uploaded_file = st.file_uploader('Upload File', type='csv')

st.write('\n')

if uploaded_file is not None:
    # Read Data
    df = pd.read_csv(uploaded_file)

    change_data = st.toggle('Edit Data')

    if change_data:
        # Update data (Choice)
        updated_data = st.data_editor(df, use_container_width=True, num_rows='dynamic')
    else:
        uploaded_data = st.dataframe(df, use_container_width=True)
        updated_data = df

    # Pass the data to Pygwalker
    pyg_app = StreamlitRenderer(updated_data)
    # Render the data in Pygwalker
    pyg_app.explorer()