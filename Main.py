from configparser import ConfigParser
from pathlib import Path
import os
import PySimpleGUI as pysimpleGUI
from bookScannerVideo import VideoStreamFrame

config = ConfigParser()
config.read(f'{os.path.join(Path(__file__).resolve().parent,"configration")}/bookScanner.cfg')
pysimpleGUI.theme(config.get('GENERAL_WINDOW','WINDOW_MAIN_THEME'))

layoutLeft = [ [pysimpleGUI.B('First Capture',key=config.get('WINDOW_MAIN','MAIN_BUTTON_LEFT_KEY'))],
               [pysimpleGUI.Image(size=(300,300),key=config.get('WINDOW_MAIN','MAIN_IMAGE_LEFT_KEY'))],
               [pysimpleGUI.T('Left Alignment',key=config.get('WINDOW_MAIN','MAIN_TEXT_LEFT_KEY'))],
              ]
layoutRight = [ [pysimpleGUI.B('Second Capture',key=config.get('WINDOW_MAIN','MAIN_BUTTON_RIGHT_KEY'))],
                [pysimpleGUI.Image(size=(300,300),key=config.get('WINDOW_MAIN','MAIN_IMAGE_RIGHT_KEY'))],
                [pysimpleGUI.T('Second Alignment',key=config.get('WINDOW_MAIN','MAIN_TEXT_RIGHT_KEY'))],
              ]
layoutMain = [
     [pysimpleGUI.Column(layoutLeft),pysimpleGUI.VSeperator(),pysimpleGUI.Column(layoutRight)]
]


window = pysimpleGUI.Window(config.get('GENERAL_WINDOW','WINDOW_TITLE'),layoutMain,finalize=True,resizable=True)
streamVideoOne =  VideoStreamFrame(videosource=int(config.get('GENERAL_WINDOW','WINDOW_READ_CAMERA_FRIST')))
try:
    if streamVideoOne.initializeImutilsRead():
        while True:
            event, values = window.read(timeout=15)
            _, frameOne = streamVideoOne.readCaptureImage()
        
            if event in (pysimpleGUI.WIN_CLOSED,'Exit'):
                break
            capture_image_byte = streamVideoOne.imageCapture(frameOne)
            window[config.get('WINDOW_MAIN','MAIN_IMAGE_LEFT_KEY')].update(data=capture_image_byte)
            window[config.get('WINDOW_MAIN','MAIN_IMAGE_RIGHT_KEY')].update(data=capture_image_byte)
            
    streamVideoOne.__del__()
    window.close()
        
except Exception as e:
    streamVideoOne.__del__()
    window.close()
    print(e)