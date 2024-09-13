import streamlit as st

col0a, col0b, col0c = st.columns([0.6, 1, 0.6])
with col0b:
    st.title("About Application")
    st.write('\n')

st.write("### :blue-background[**:material/code_blocks: Developer**]")
st.write("""

***Ameer Hamza Ali***  
***Batch 2022***  
***Department of Civil Engineering***  
***NED University of Engineering & Technology, Karachi, Pakistan***  

Check out my profile:  
https://about-hamza-ali.streamlit.app/  
  
Let's connect!:  
https://www.linkedin.com/in/hamza-ali-35449a2aa/
""")

# st.write('\n')
# st.write("### :blue-background[**:material/update: Version**]")
# st.write(":grey-background[**Version 1.0**] - Initial Release (01/09/2024)")


st.write('\n')
st.write("### :blue-background[**:material/communities: Purpose**]")
st.write(
    """
    This application is designed to provide an interactive platform for performing various Numerical Analysis methods. 
    It aims to help students, engineers, and professionals solve complex mathematical problems with ease by leveraging 
    algorithms such as root-finding, solving systems of equations, interpolation, and more. The goal is to enhance the 
    understanding of numerical techniques through a user-friendly interface that facilitates practical learning and 
    application of theoretical concepts in real-time.
    """
)

st.write('\n')
st.write("### :blue-background[**:material/view_module: Modules Used**]")
st.write("""
- **:grey-background[Streamlit]:** For creating the interactive web application interface. [Streamlit Documentation](https://docs.streamlit.io/)
- **:grey-background[SymPy]:** For symbolic mathematics, solving equations, and implementing numerical methods. [SymPy Documentation](https://docs.sympy.org/)
- **:grey-background[Pandas]:** For data manipulation and handling tabular data efficiently. [Pandas Documentation](https://pandas.pydata.org/)
""")



st.write('\n')
st.write("###  :blue-background[**:material/call: Contact**]")
st.write("""
For further assistance, feedback, or to report any bugs, please contact me at ameer.hamza.alee3011@gmail.com.
""")

