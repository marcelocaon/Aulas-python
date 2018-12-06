# Interactive Facial Recognition Overlays
# # This example requires the python library dlib, which can be install with pip.
# #
# # pip install dlib
# #
# # Note: building this library requires cmake to be installed and may take some time.
# #
# # Also needed are the two .dat files (mmod_human_face_detector.dat and mmod_dog_hipsterizer.dat) which can be downloaded here compressed as .gz files. Download and uncompress them in the same root directory as this example.
# #
# # In [5]:
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import dlib


#load dlib's pretrained face detector
cnn_human_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')

#choose a file in your current directory or download https://raw.githubusercontent.com/michaelbabyn/plot_data/master/beethoven.jpg
f = 'beethoven.jpg'
img = dlib.load_rgb_image(f)

human_dets = cnn_human_detector(img,1)

#load dlib's pretrained dog-face detector
cnn_dog_detector = dlib.cnn_face_detection_model_v1('mmod_dog_hipsterizer.dat')

dog_dets = cnn_dog_detector(img, 1)

layout= go.Layout(
    xaxis = go.layout.XAxis(
        showticklabels = False,
        showgrid=False,
        zeroline=False,
        range = [0, img.shape[1]]
    ),
    yaxis = go.layout.YAxis(
        showticklabels = False,
        showgrid=False,
        zeroline=False,
        range = [0, img.shape[0]],
        scaleanchor = 'x'
        ),
    autosize=False,
    height=img.shape[0],
    width=img.shape[1],
    margin = {'l': 0, 'r': 0, 't': 0, 'b': 0},
    images= [dict(
        source= "https://raw.githubusercontent.com/michaelbabyn/plot_data/master/beethoven.jpg",
        x=0,
        sizex=img.shape[1],
        y=img.shape[0],
        sizey=img.shape[0],
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch"
     )]
)

humans=[
    go.Scatter(
        x=[d.rect.left(), d.rect.right(), d.rect.right(), d.rect.left(), d.rect.left()],
        y=[img.shape[0] - d.rect.top(),img.shape[0] - d.rect.top(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.top()],
        hoveron = 'fills',
        name = 'Human #{0}'.format(i+1),
        text = 'confidence: {:.2f}'.format(d.confidence),
        mode='lines',
        line = dict(width=4,color='red'),
        showlegend = False
        )
    for i,d in enumerate(human_dets)]

dogs = [
    go.Scatter(
        x=[d.rect.left(),d.rect.right(),d.rect.right(),d.rect.left(),d.rect.left()],
        y=[img.shape[0] - d.rect.top(),img.shape[0] - d.rect.top(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.bottom(),img.shape[0] - d.rect.top()],
        hoveron = 'fills',
        name = 'Dog #{0}'.format(i+1),
        text = 'confidence: {:.2f}'.format(d.confidence),
        mode='lines',
        line = dict(width=4,color='blue'),
        showlegend = False
        )
    for i,d in enumerate(dog_dets)]

py.iplot(dict(data=humans+dogs,layout=layout),filename='EXAMPLES/facial_rec')