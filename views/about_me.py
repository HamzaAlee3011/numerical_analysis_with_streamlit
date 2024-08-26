import streamlit as st
import time

# st.set_page_config(page_title='About Ameer Hamza Ali', layout="wide")

# Step 2: Load the PDF File
pdf_file_path = "./assets/Resume_Ameer_Hamza_Ali_darkmode.pdf"  # Replace with the actual path to your PDF file

with open(pdf_file_path, "rb") as file:
    pdf_bytes = file.read()

# Step 3: Create a Download Button
@st.fragment
def download_resume():
    if st.download_button(
        label="Download Resume (PDF)",
        data=pdf_bytes,
        file_name="Resume_Ameer_Hamza_Ali.pdf",  # The name with which the file will be downloaded
        mime="application/pdf"
    ):
        st.balloons()

# download_resume()

intro_para = """
**Hi there** 👋  
**Ameer Hamza Ali** here!
---
An undergraduate student pursuing a degree in **Civil Engineering** at **NED University of Engineering & Technology**. I am deeply interested in integrating modern technology into traditional civil engineering practices, and I love exploring how modern technology can revolutionize our field. I’m always on the lookout for the latest trends and enjoy applying them to real-world projects.
"""

# intro_para = """
# # Ameer Hamza Ali
# ---
# An undergraduate student pursuing a degree in **Civil Engineering** at **NED University of Engineering & Technology**. I am deeply interested in integrating modern technology into traditional civil engineering practices, and I love exploring how modern technology can revolutionize our field. I’m always on the lookout for the latest trends and enjoy applying them to real-world projects.
# """

def stream_data():
    for word in intro_para.split(" "):
        yield word + " "
        time.sleep(0.04)


# HERO SECTION
col1, col2 = st.columns([1.12, 2], gap='small', vertical_alignment='center')
with col1:

    st.image('./assets/person_30dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg', use_column_width='always')
with col2:
    # st.title('Ameer Hamza Ali', anchor=False)
    st.write_stream(stream_data)

st.write("\n")
cola , colb = st.columns([1.1, 2], gap='small')

with cola:
    # Container for Contact Information
    with st.container(border=True):
        st.write("\n")
        st.write("### :blue-background[**:material/contact_page: Social**]")
        st.write(":grey-background[**:material/mail: Email**]")
        st.write("ameer.hamza.alee3011@gmail.com")

        st.write(":grey-background[**LinkedIn**]")
        st.write('https://www.linkedin.com/in/hamza-ali-35449a2aa/')
        # Contact Info with Icons
        st.markdown("""""")



        # Language Section
        st.write("---")
        st.write("### :blue-background[**:material/language: Language**]")
        st.write('- English')
        st.write('- Urdu')


with colb:
    with st.container(border=True):
        # Title Section
        st.write("\n")
        st.write("### :blue-background[**Experience**]")
        st.write("Fresher")
        st.write("---")

        # Education Section
        st.write("\n")
        st.markdown("### :blue-background[**:material/school: Education**]")

        col1, col2 = st.columns([4, 1], vertical_alignment='bottom')
        with col1:
            st.write("#### NED University of Engineering and Technology")
            st.write("BE, Civil Engineering")
        with col2:
            st.write("Oct 2022 - Present")

        col1, col2 = st.columns([4, 1], vertical_alignment='bottom')
        with col1:
            st.write("#### Adamjee Govt. Science College")
            st.write("Inter Education")
        with col2:
            st.write("2020 - 2022")
        st.write("---")

        # Certifications Section
        st.write("\n")
        st.write("### :blue-background[**:material/approval: Certifications**]")

        st.write("- #### Introduction to Python - Sololearn")
        st.write("Issued Apr 2023")
        st.write("Credential ID: CC-KGKMA0F")



        st.write("- #### Revit Course for Beginners - Alison")
        st.write("Issued Feb 2024")
        st.write('Credential ID: AC-6352-37287052')
        st.write("---")

        st.write("\n")
        st.write("### :blue-background[**:material/article: Skills**]")

        st.write("- #### :grey-background[AutoCAD]")
        st.write("*Expert in drafting, with a strong command of both 2D and 3D design principles.*")

        st.write("- #### :grey-background[Revit]")
        st.write(
            "*Skilled in 3D architectural and structural modeling with a high interest in Building Information Modeling (BIM).*")

        st.write("- #### :grey-background[MS Office]")
        st.write(
            "*Proficient in the MS Office suite, with advanced skills in MS Word and MS Excel for documentation and data analysis.*")

        st.write("- #### :grey-background[Python]")
        st.write(
            "*Keen on leveraging Python for automating tasks specially in the Civil Engineering domain, with a strong focus on data analysis and visualization.*")