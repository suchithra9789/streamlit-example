import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# Set page config
st.set_page_config(page_title="Vengateswaran Arunachalam's Resume", layout="wide")

# Custom styles
st.markdown("""
<style>
body {
    font-family: 'Helvetica', sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}
