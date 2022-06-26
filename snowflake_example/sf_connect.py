import snowflake.connector
import os

conn = snowflake.connector.connect(
    user='ryanpearson',
    password='Rya07051634',
    account='CKA02716',
    session_parameters={
        'ROLE': 'accountadmin',
    }
)
