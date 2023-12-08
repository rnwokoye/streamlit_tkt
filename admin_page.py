import streamlit as st
import pandas as pd
import datetime
import numpy as np

# from psycopg2.extensions import register_adapter, AsIs


# from config.db_con import create_connection


st.write("Admin Page")

# db_connect = st.secrets.connections.cockroachdb.DATABASE_URL


def calc_fine(row):
    initial_fine = row["fine_amount"]
    days_lapsed = row.days_lapsed

    if days_lapsed > 30:
        periods_overdue = -(-days_lapsed // 30)  # Ceiling
        return initial_fine * periods_overdue
    else:
        return initial_fine


def get_tickets(connection_object) -> pd.DataFrame:
    query = f"""SELECT * FROM traffic_tickets;"""
    today = datetime.datetime.now().date()
    st.write(f"Today's date is {today}")

    with connection_object.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
        cols = [i[0] for i in cursor.description]
        res_df = pd.DataFrame(data, columns=cols)
        res_df["days_lapsed"] = pd.to_timedelta(today - res_df["due_date"]).dt.days
        res_df["status"] = np.where(res_df["days_lapsed"] > 30, "Overdue", "Current")
        res_df["penalty_amount"] = res_df.apply(lambda x: calc_fine(x), axis=1)

        return res_df
