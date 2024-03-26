import streamlit as st
import streamlit_authenticator as stauth
# from dependancies import fetch_users, sign_up
import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
import mysql.connector
import time
import bcrypt
from sqlalchemy.sql import text

st.set_page_config(page_title='Streamlit', page_icon='🐍', initial_sidebar_state='collapsed')
conn = st.connection('mysql', type='sql')

def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com

    if re.match(pattern, email):
        print(pattern)
        return True
    return False
def fetch_users():
    df = conn.query('SELECT * from users;', ttl=600)


def get_user_emails():
    df = conn.query('SELECT * from users;', ttl=600)
    st.write(df.to_dict(),"KKK")
    emails = []
    for row in df.itertuples():
        st.write(row,"JJJ")
        emails.append(row.email)
    return emails
def validate_username(username):
    pattern = "^[a-zA-Z0-9 ]*$"
    if re.match(pattern, username):
        return True
    return False

def get_usernames():
    df = conn.query('SELECT * from users;', ttl=600)
    st.write(df.to_dict())
    usernames = []
    for row in df.itertuples():
        usernames.append(row.userName)
    return usernames
def main():
    try:
        with st.form('signup'):
            st.subheader('Sign Up')
            email = st.text_input('Email', placeholder='Enter Your Email')
            username = st.text_input('Username', placeholder='Enter Your Username')
            password1 = st.text_input('Password', placeholder='Enter Your Password', type='password')
            password2 = st.text_input('Confirm Password', placeholder='Confirm Your Password', type='password')
            # btn1= st.columns(1)
            # showError = False
            # with btn1:
            if st.form_submit_button('Sign Up'):
                st.write("LL")
                if email:
                    if validate_email(email):
                        if email not in get_user_emails():
                            if username and validate_username(username):
                                if username not in get_usernames():
                                    if len(username) >= 2:
                                        if len(password1) >= 6:
                                            if password1 == password2:
                                                # Add User to DB
                                                hashed_password = stauth.Hasher([password2]).generate()
                                                # insert_user(email, username, hashed_password[0])
                                                # with conn.session as s:

                                                insert_stmt = (
                                                    "INSERT INTO users(username, email, password)" "VALUES (%s, %s, %s)")
                                                data = (username, email, hashed_password[0])
                                                print(data,"?????????????????/",insert_stmt)
                                                # conn.query(insert_stmt, data)
                                                    # cu.execute(insert_stmt, data)
                                                    # s.commit()
                                                conn = st.connection('mysql', type='sql')

                                                with conn.session as s:
                                                    a = 'INSERT INTO users (username, email, password) VALUES ("{username}","{email}","{password}");'.format(username=username, email=email, password=hashed_password[0])
                                                    st.write(a)
                                                    s.execute(
                                                        text(a)
                                                    )
                                                    s.commit()
                                                st.success('Account created successfully!!')
                                                st.balloons()
                                            else:
                                                st.warning('Passwords Do Not Match')
                                        else:
                                            st.warning('Password is too Short')
                                    else:
                                        st.warning('Username Too short')
                                else:
                                    st.warning('Username Already Exists')

                            else:
                                st.warning('Invalid Username')
                        else:
                            st.warning('Email Already exists!!')
                    else:
                        st.warning('Invalid Email')
                else:
                    # showError = True
                    st.warning("Please add all details")


    except Exception as e:
        st.write(e)

if __name__ == '__main__':
    main()
