import streamlit as st
import arcpy
import os
import pathlib
import time

def gis():
    aprx = arcpy.mp.ArcGISProject(
        r'S:\Felles\SamferdselInfrastruktur\skredmal_streamlit\GIS\Mal_skredfarevurdering.aprx')
    project_name = pathlib.Path(aprx.filePath)
    directory = str(project_name.parent)
    output_directory = os.path.join(directory, r'eksporterte_kart')

    for i in range(len(aprx.listLayouts())):
        if aprx.listLayouts()[i].name == 'Skogtype':
            lyt = aprx.listLayouts()[i]
            lyt.exportToJPEG(os.path.join(output_directory, 'Skogtype'), 300)

def check_folder(path):
    return len(os.listdir(path))

def vent():
    with st.spinner('Vent du no litt Magne...'):
        while True:
            file_count = check_folder(f'S:\\Felles\\SamferdselInfrastruktur\\skredmal_streamlit\\GIS\\eksporterte_kart')
            if file_count >= 1:
                time.sleep(5)
                st.balloons()
                break
            else:
                time.sleep(2)



st.title('Streamlit + ArcGIS = SANT')


if st.button('Hent kart fra arcgis', on_click=vent()):
    gis()

if os.path.exists(f'S:\\Felles\\SamferdselInfrastruktur\\skredmal_streamlit\\GIS\\eksporterte_kart\\Skogtype.JPG'):
    with open(f'S:\\Felles\\SamferdselInfrastruktur\\skredmal_streamlit\\GIS\\eksporterte_kart\\Skogtype.JPG', 'rb') as file:
        st.download_button(
            label="Last ned kart",
            data=file,
            file_name=f'S:\\Felles\\SamferdselInfrastruktur\\skredmal_streamlit\\GIS\\eksporterte_kart\\Skogtype.JPG')
