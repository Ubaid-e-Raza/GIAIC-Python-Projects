import re
import streamlit as st

st.title("Password Strength Checker")
st.info("Password must be atleast 8 characters long, containing atleast one uppercase and lowercase letter, one number and one special character.")
password = st.text_input("Enter Password: ")
score = 0
problem = None
if password:
    if (len(password))>=8:
        score +=1
    else:
        st.error("Password must be alteast 8 characters long!")
        problem = 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else: 
        st.error("The password should contain both uppercase and lowercase letters!")
        problem = 2
    if re.search(r"\d", password):
        score += 1
    else:
        st.error("The password should contain atleast one number (0-9).")
        problem = 3
    if re.search(r"[!£$%^&*()_\-=+]", password):
        score +=1
    else:
        st.error("The password should contain atleast one special character (!£$%^&*()_-=+).")
        problem = 4

    if score == 4:
        st.success("You have created a strong password.")
    elif score ==3:
        if problem == 2:
            st.success("The passwords strength is intermediate, you can improve the password strength by adding uppercase or lowercase letters.")
        elif problem == 3:
            st.success("The passwords strength is intermediate, you can improve the password strength by adding numbers.")
        elif problem == 4:
            st.success("The passwords strength is intermediate, you can improve the password strength by adding atleast one special case characters [!£$%^&*()_-=+].")
    elif score == 2:
        st.error("Weak password, create a strong password by reading the instructions mentioned above.")