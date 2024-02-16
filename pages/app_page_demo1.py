# AISBACH Data Solutions DEMO App (Streamlit) - Implemented by Stefan Rummer, 2024

import numpy as np
import os
import librosa
import librosa.display
import soundfile as sf
import streamlit as st
import plotly.graph_objects as go
# has classes for tick-locating and -formatting

from st_app_design import add_spacer
from st_app_components import launch_page


streamlit_dark = 'rgb(15,17,22)'  # #0F1116' default dark theme


def melspectrogram_plotly3d(y, sr, sec_offset, mark_peaks, camera_mode_3d, zvalue_treshold):

    mels_count = 300
    max_freq = 32768  # Hz
    # zvalue_treshold = -15  # dB
    # mark_peaks = False
    # camera_mode_3d = False

    # calc playtime duration in seconds
    duration = librosa.get_duration(y=y, sr=sr)

    # Passing through arguments to the Mel filters
    spectrum = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=mels_count, fmax=max_freq)
    # decibel is measured using the np.max(S) value as a reference point
    mel_data = librosa.power_to_db(spectrum, ref=np.max)  # convert spectrum to dB


    # caculate sample points for adequate tick labels in plot
    xvalues_count, yvalues_count = len(mel_data[0]), len(mel_data)  # 764, 200

    # flat surface on level of zvalue treshold
    flat_data = np.full((len(mel_data), len(mel_data[0])), zvalue_treshold)

    # PLOT CONFIG
    config = {'displayModeBar': True, 'displaylogo': False,
              'modeBarButtonsToRemove': ['orbitRotation',
                                         'resetCameraDefault3d']}

    layout = go.Layout(  # layout of spikes that visualize cursor
        scene=go.layout.Scene(  # position on 3D plot side walls
            xaxis=go.layout.scene.XAxis(showspikes=True, color='white'),
            yaxis=go.layout.scene.YAxis(showspikes=True, color='white'),
            zaxis=go.layout.scene.ZAxis(showspikes=False)))

    if not camera_mode_3d:
        # 3D camera positioning: TOP VIEW
        camera = dict(up=dict(x=1, y=0, z=0),
                      center=dict(x=0, y=0, z=0),
                      eye=dict(x=0, y=0, z=1))
    elif camera_mode_3d:
        # 3D camera positioning: PERSPECTIVE VIEW
        camera = dict(up=dict(x=0, y=0, z=0),
                      center=dict(x=0, y=0, z=0),
                      eye=dict(x=1, y=1, z=0.8))

    # create custom colorscale for surfaceplot
    colorscale_melspectrum = [[0, 'rgb(0,0,0)'],
                              [0.005, 'rgb(100,100,100)'],
                              [0.01, 'rgb(0,0,0)'],
                              [0.3, 'rgb(30,30,30)'],
                              [0.4, 'rgb(50,50,50)'],
                              [0.5, 'rgb(80,80,80)'],
                              [0.75, '#16C89D'],  # Replace yellow with AISBACH green
                              [0.9, '#16C89D'],  # Replace yellow with AISBACH green
                              [0.975, 'rgb(255,255,255)'],
                              [1, 'rgb(255,255,255)']]

    # create custom colorscale for surfaceplot
    colorscale_flat = [[0, 'white'], [1, 'white']]

    # contour height level rings for values > treshold
    contours = {"z": {"show": mark_peaks, "start": zvalue_treshold,
                      "end": 0, "size": 1, "color": "black"}}

    # CALC correct 3D MEl Spectrogram X-AXIS Tick label texts & positions
    x_tickvals, x_ticktext = [], []
    timestep = duration / 10  # 10x timeslots
    xvaluestep = xvalues_count / 10  # 10x timeslots
    xvalue, timevalue = 0, sec_offset  # factor in offset
    while xvalue < xvalues_count:
        x_tickvals.append(round(xvalue, 2))
        x_ticktext.append(round(timevalue, 2))
        xvalue += xvaluestep
        timevalue += timestep

    # CALC correct 3D MEl Spectrogram Y-AXIS Tick label texts & positions
    y_tickvals, yvalue = [], 0
    y_ticktext = ["0", "512", "1024", "2048", "4096", "8192", "16384", "32768"]
    while yvalue <= yvalues_count + 1:
        y_tickvals.append(round(yvalue, 1))
        yvalue += (yvalues_count / 7)

    # PLOTLY GRPAH OBJECT GENERATE PLOT
    if mark_peaks:  # plot surface using selected colorscheme, layout and contours
        fig = go.Figure(data=[go.Surface(z=mel_data,
                                         showscale=True, colorscale=colorscale_melspectrum,
                                         # hovertemplate='<br>%{x} sec<br>%{y} Hz<br>%{z} dB<extra></extra>',
                                         hovertemplate='<br>%{z} dB<extra></extra>',
                                         opacity=1, contours=contours),  # colormapped opaque surface
                              go.Surface(z=flat_data, name=f'<br>amplitude<br>treshold',
                                         # name=f'<br>amplitude<br>treshold<br>{zvalue_treshold} dB',
                                         showscale=False, colorscale=colorscale_flat,
                                         # hovertemplate='<br>%{x} sec<br>%{y} Hz<br>%{z} dB',
                                         hovertemplate='<br>%{z} dB',
                                         opacity=0.4)], layout=layout)  # translucent flat surface

    if not mark_peaks:  # plot surface using selected colorscheme, layout and contours
        fig = go.Figure(data=[go.Surface(z=mel_data,
                                         showscale=True, colorscale=colorscale_melspectrum,
                                         # hovertemplate='<br>%{x} sec<br>%{y} Hz<br>%{z} dB<extra></extra>',
                                         hovertemplate='<br>%{z} dB<extra></extra>',
                                         opacity=1, contours=contours)], layout=layout)

    # background and axis label colors and dimensions
    fig.update_layout(autosize=True, width=950, height=600,
                      margin=dict(t=0, r=0, l=20, b=0),  # margins
                      paper_bgcolor=streamlit_dark,  # rgb(15,17,22)
                      font_family='Arial',  # "Courier New",
                      font_color="white",
                      legend_title_font_color="white")

    # replace perspective camera with orthogonal view
    fig.layout.scene.camera.projection.type = "orthographic"
    # turntable view of defined camera position
    fig.update_layout(scene_aspectmode='manual',
                      scene_camera=camera,
                      dragmode="turntable",
                      scene_aspectratio=dict(x=1.5, y=1, z=0.75),

                      scene_zaxis=dict(
                          gridcolor="rgb(055, 055, 055)",
                          showbackground=True,
                          backgroundcolor=streamlit_dark,
                          title='Volume [dB]'),

                      scene_xaxis=dict(
                          gridcolor="rgb(055, 055, 055)",
                          showbackground=True,
                          backgroundcolor=streamlit_dark,
                          title='Time [secs]',
                          tickvals=x_tickvals,
                          ticktext=x_ticktext,
                          tickangle=45),

                      scene_yaxis=dict(
                          gridcolor="rgb(055, 055, 055)",
                          showbackground=True,
                          backgroundcolor=streamlit_dark,
                          title='Frequency [Hz]',
                          tickvals=y_tickvals,
                          ticktext=y_ticktext)
                      )

    # enable x-axis traces without permanent projection
    fig.update_traces(contours_x=dict(show=False, usecolormap=False,
                                      highlightcolor="#16C89D",  # "#ff008d",
                                      highlightwidth=15, project_x=True))

    # define colorbar attributes
    fig.data[0].colorbar.title = "Amp [dB]"  # title text
    fig.data[0].colorbar.orientation = "v"  # orientation
    fig.data[0].colorbar.thickness = 25  # colorbar width
    fig.data[0].colorbar.len = 0.6  # colorbar length

    st.plotly_chart(fig, use_container_width=True, config=config)


def build_page():

    audiofile_path = os.path.join(os.getcwd(), 'pages/app_demo_1/looperman_piano.wav')

    st.audio(audiofile_path, format='audio/wav', start_time=0)

    # extract technical specifications about wav file
    # no need for session_state saving bc instant calc
    wav_specs = sf.SoundFile(audiofile_path)
    wav_data, _ = sf.read(audiofile_path)
    sampling_freq = wav_specs.samplerate
    y, sr = librosa.load(audiofile_path, sr=sampling_freq)
    duration = librosa.get_duration(y=y, sr=sr)
    y_slice, sr_slice = librosa.load(audiofile_path, sr=sampling_freq, offset=0, duration=duration)


    plot_cols = st.columns([1, 1])
    with plot_cols[0]:
        with st.spinner('generating 3D Mel Spectrogram - DEFAULT MODE'):
            # plot 3D interactive mel spectrogram
            melspectrogram_plotly3d(y_slice, sr_slice, 0, False, False, -10)
    with plot_cols[1]:
        with st.spinner('generating 3D Mel Spectrogram - DEFAULT MODE'):
            # plot 3D interactive mel spectrogram
            melspectrogram_plotly3d(y_slice, sr_slice, 0, True, True, -10)


launch_page(build_page,
            access='email_funnel',
            title='Audio Data Spectral Analysis',
            description='Audio Analytics Dashboard that provides insights and eliminates'
                        ' tedious tasks in the music production workflow [Plotly, Librosa, Essentia]')
