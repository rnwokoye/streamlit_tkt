import psycopg2
import os

# from psycopg2.extensions import register_adapter, AsIs
import streamlit as st
import pandas as pd


def create_connection(connection_url):
    connection = None
    try:
        connection = psycopg2.connect(connection_url)
        print("Connected to db")
    except psycopg2.Error as e:
        print(f"The error of '{e}' has occured")
    return connection
