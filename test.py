import pandas as pd 
import streamlit as st 

def main():

    st.title("Test for GIT LFS")

    df = pd.read_csv(r"C:\Users\Elisha.Zissman\OneDrive - Social Investment Business\Desktop\GIT_LFS_TEST\LARGEDATA\pc_data.csv")
    st.write(df.head())

if __name__ == "__main__":
    main()

