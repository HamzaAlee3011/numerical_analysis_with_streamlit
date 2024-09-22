import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email sender details
your_email = "ameer.hamza.alee3011@gmail.com"
your_password = "hjzvupobibsrigsn"

# Function to send email
@st.dialog(title='Feedback Form')
def feedback_function():


    def send_feedback(name, user_email, feedback, rating):
        msg = MIMEMultipart()
        msg['From'] = user_email
        msg['To'] = your_email
        msg['Subject'] = f"Feedback from {name} - {rating} star(s)"

        # The body of the email
        body = f"Name: {name}\nEmail: {user_email}\nRating: {rating} star(s)\n\nFeedback:\n{feedback}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Secure the connection
            server.login(your_email, your_password)
            server.sendmail(user_email, your_email, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


    # Streamlit form for feedback

    # Sentiment mapping for stars
    sentiment_mapping = ["one", "two", "three", "four", "five"]

    with st.form(key='feedback_form'):
        name = st.text_input("Your Name")
        user_email = st.text_input("Your Email Address")
        feedback = st.text_area("Your Feedback")

        # Star feedback mechanism
        selected = st.feedback("stars")

        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        if name and user_email and selected is not None:
            # Map the star feedback to number of stars
            rating = sentiment_mapping[selected]

            success = send_feedback(name, user_email, feedback, rating)
            if success:
                st.toast("Feedback submitted successfully!")
            else:
                st.error("Failed to send feedback. Please try again.")
        else:
            st.warning("Please fill out atleast name and email address fields and provide a star rating before submitting.")
