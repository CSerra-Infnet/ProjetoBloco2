import glob
import pandas as pd
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dataframe_collection = {} 

def load_data() -> None:
    """
    Load data from file path and return DataFrame
    """    
    for f in glob.glob('data/01_raw/*.csv'):
        dataframe_collection[f] = pd.read_csv(f, sep=";")

def Dashboard() -> None:
    """
    Main function to create the Dashboard
    """
    
    load_data()
  
    st.title("RespirAR")
    st.write("Plataforma para análise de dados de qualidade do ar e sugestão de medidas de mitigação das emissões de poluentes atmosféricos.")
    
    st.sidebar.title("Menu")
    st.sidebar.write("Selecione a opção desejada no menu abaixo:")
    menu = st.sidebar.radio("Menu", dataframe_collection.keys())
    
    if menu:
        st.write(f"### {menu}")
        st.write(dataframe_collection[menu].head())
    
    
    
    
    
if __name__ == "__main__":
    Dashboard()


 