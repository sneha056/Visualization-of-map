import pandas as pd
import plotly.express as px
import streamlit as st #use to make interactibe web application
import json as js


INDIA_PATH_TO_DATA = "state_city_data_in.json"  #PATH TO THE DATA FILE OF INDIA
PATH_TO_GEOJSON = "indian_map_cordinate.geojson"  #PATH TO THE GEOJSON FILE OF INDIA"
US_PATH_TO_DATA = "state_city_data_us.json"  # us data


def state_city_scatter_mapbox_india():
    #ADDING SUBHEADING UNDER THE SCATTER MAP HEADING
    st.subheader("visiualizing state and capital of india")
    #loading STATE AND CITY  from json file into pandas
    state_city_data = pd.read_json(INDIA_PATH_TO_DATA)
    #to display table and hiding the index which is by default generated as it is already in our data set
    st.dataframe(state_city_data, hide_index=True)
    # scatter mapbox is the type of map which we are using i.e how to plot data
    fig = px.scatter_mapbox(
        data_frame=state_city_data,
        lon="long",
        lat="lat",
        hover_name="state",
        hover_data="capital",
        color="capital",
        size="id",
        center={  #map cordinate that  how it should look at first
            "lat": 20.56,
            "lon": 79.96
        },
        zoom=3,
        height=600,
    )
    # to display map                #open street map is the type of map
    fig.update_layout(mapbox_style="open-street-map")
    return st.plotly_chart(fig)


def state_city_choropleth_mapbox_india():
    st.subheader("visiualizing state and capital of INDIA")
    state_city_data = pd.read_json(INDIA_PATH_TO_DATA)
    st.dataframe(state_city_data, hide_index=True)
    #choropleth mapbox is the type of map which we are using i.e that how to show data
    fig = px.choropleth_mapbox(
        data_frame=state_city_data,
        geojson=js.load(open(PATH_TO_GEOJSON, "r")),
        locations="state",
        featureidkey="properties.ST_NM",
        hover_name="state",
        hover_data="capital",
        color="capital",
        center={  #map cordinate that  how it should look at first
            "lat": 20.56,
            "lon": 79.96
        },
        zoom=3,
        opacity=0.5,
        height=600,
    )
    #background of map i.e style
    fig.update_layout(mapbox_style="carto-positron")
    return st.plotly_chart(fig)


def state_city_scatter_mapbox_us():
    st.subheader("visiualizing state and capital of UNITED STATES")
    state_city_data_us = pd.read_json(US_PATH_TO_DATA)
    state_city_data_us.insert(0,'row_id',range(1,1+len(state_city_data_us)))
    st.dataframe(state_city_data_us,hide_index=True)
    fig2 = px.scatter_mapbox(data_frame=state_city_data_us,
                             lon="long",
                             lat="lat",
                             size='row_id',
                             hover_name="state",
                             hover_data="capital",
                             zoom=3,
                             color="capital",
                            height=600)
    fig2.update_layout(mapbox_style="open-street-map")
    return st.plotly_chart(fig2)
