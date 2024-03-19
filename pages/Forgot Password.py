import smtplib
import streamlit as st

from dependancies import updatePassword

import string
import random
import re

import html

def convert_to_html_safe(text):
    return html.escape(text)

print(convert_to_html_safe('<p>Good luck! Hope it works.</p>'))
fields={'Form name':'Forgot password','Email':'Email','Submit':'Submit'}
def generate_random_pw(length: int=16) -> str:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length)).replace(' ','')

def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

    if re.match(pattern, email):
        return True
    return False
forgot_password_form = st.form('Forgot password')
forgot_password_form.subheader('Forget password' if 'Form name' not in fields else fields['Form name'])
email = forgot_password_form.text_input('Email' if 'Email' not in fields else fields['Email']).lower()
if forgot_password_form.form_submit_button('Submit' if 'Submit' not in fields else fields['Submit']):
    if len(email) > 0 and validate_email(email):
        password = generate_random_pw()
        print(password)
        # password = 'Satya@3112'
        updated = updatePassword(email,password)
        if password and updated:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("streamlitsatya@gmail.com", 'nevb ahzo ehby gcrt')
            msg = 'New Password: ' + password
            server.sendmail('streamlitsatya@gmail.com',email,password)
    else:
        st.error("Please enter valid email")



# Hi [name],

# There was a request to change your password!

# If you did not make this request then please ignore this email.

# Otherwise, please click this link to change your password: [link]

# st.write(generate_random_pw())

# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login("streamlitsatya@gmail.com", 'nevb ahzo ehby gcrt')
# server.sendmail('streamlitsatya@gmail.com','streamlitsatya@gmail.com',"HHHHHHHHHHHHHHHHHH")
# print("ssssssssssss")
