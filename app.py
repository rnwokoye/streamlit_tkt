import streamlit as st
import pandas as pd
import numpy as np

from admin_page import get_tickets
from config.db_con import create_connection

db_connect = st.secrets.connections.cockroachdb.DATABASE_URL

st.title("Traffic Ticket Assignement")

if "session_data" not in st.session_state:
    st.session_state.session_data = {}


def my_function():
    st.write(f"Current session state data is: {st.session_state.session_data}")
    st.write("Hello World")
    return


with st.form(key="form"):
    user_name = st.text_input("Text")
    if user_name:
        st.session_state.session_data["user_name"] = user_name
    submit = st.form_submit_button()

if submit:
    st.write(f"Text: {user_name}")


st.write("Pandas Testing")
data = np.arange(0, 100, 2).reshape(5, 10)
df = pd.DataFrame(data)
st.write(df)

data2 = get_tickets(create_connection(db_connect))


st.write(data2)


if __name__ == "__main__":
    my_function()
