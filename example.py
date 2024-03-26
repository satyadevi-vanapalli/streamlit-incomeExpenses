import sqlite3
import streamlit as st
from pymongo import MongoClient
import ssl
import mysql.connector
from sqlalchemy.sql import text

conn = st.connection('mysql', type='sql')
with conn.session as s:
    # s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    # s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        a = 'INSERT INTO details (name) VALUES ("{fname}");'.format(fname=k)

        s.execute(
            text(a)
        )
        s.commit()
        st.write("success", a)
