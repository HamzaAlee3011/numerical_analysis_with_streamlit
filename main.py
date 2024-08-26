import streamlit as st

# PAGE SETUP
st.set_page_config(layout='wide')

bisection_method_page = st.Page(

    page="views/Bisection_method.py",
    title="Bisection Method",
    # icon=":material/bid_landscape:",
)

about_me = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
)

# about_app = st.Page(
#     page="views/about_app.py",
#     title="About Application",
#     icon=":material/info:",
# )

# NAVIGATION SETUP (WITHOUT SECTIONS)
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# NAVIGATION SETUP (WITH SECTIONS)
pg = st.navigation({
    'Applications': [bisection_method_page],
    # 'Usage': [instructions],
    'Info': [about_me]
})


# SHARED ON ALL PAGES

# st.logo('assets/example_logo.png')
# st.sidebar.link_button(label='About me', url='https://about-hamza-ali.streamlit.app/')
# with 💥''')

#RUN NAVIGATION
pg.run()
