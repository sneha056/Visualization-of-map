import streamlit as st
from state_city_map import *


#to remove left padding
st.set_page_config(layout="wide")
st.title("VISUALISATION OF MAP")

SIDEBAR_DICT = {  #KEYS ARE DISPLAYED AND VALUES ARE USED TO CALL FUNCTION
    "STATE-CITY SCATTER MAP OF INDIA": state_city_scatter_mapbox_india,
    "STATE-CITY CHOROPLETH MAP OF INDIA": state_city_choropleth_mapbox_india,
    "STATE-CITY SCATTER MAP OF US": state_city_scatter_mapbox_us
}




def main1():
  #for side bar of map. bullets are of radio type and function isdfg called on the basis of dict keys i.e which key is pressed
  chart_type = st.sidebar.radio("Select chart type  for region: ",
                                SIDEBAR_DICT.keys())
  SIDEBAR_DICT[chart_type]()




if __name__ == "__main__":
  main1()

