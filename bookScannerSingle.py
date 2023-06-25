from configparser import ConfigParser
from pathlib import Path
import os
import PySimpleGUI as pysimpleGUI
from bookScannerVideo import VideoStreamFrame

class SingleScan:
    def __init__(self) -> None:
         self.config = ConfigParser()
         self.config.read(f'{os.path.join(Path(__file__).resolve().parent,"configration")}/bookScanner.cfg')

    def startMain(self):
        pysimpleGUI.theme(self.config.get('GENERAL_WINDOW','WINDOW_MAIN_THEME'))
        layoutLeft = [ 
                 [pysimpleGUI.B('Capture',key=self.config.get('WINDOW_MAIN','MAIN_BUTTON_LEFT_KEY'))],
                 [pysimpleGUI.Image(size=(300,300),key=self.config.get('WINDOW_MAIN','MAIN_IMAGE_LEFT_KEY'))],
                 [pysimpleGUI.T('Left Alignment',key=self.config.get('WINDOW_MAIN','MAIN_TEXT_LEFT_KEY'))],
              ]
        
        window = pysimpleGUI.Window(self.config.get('GENERAL_WINDOW','WINDOW_TITLE'),layoutLeft,finalize=True,resizable=True)
        streamVideoOne =  VideoStreamFrame(videosource=int(self.config.get('GENERAL_WINDOW','WINDOW_READ_CAMERA_FRIST')))

        try:
            if streamVideoOne.initializeImutilsRead():
                while True:
                    event, values = window.read(timeout=15)
                    _, frameOne = streamVideoOne.readCaptureImage()
                    if event in (pysimpleGUI.WIN_CLOSED,'Exit'):
                        break
                    
                    byteFrameOne = streamVideoOne.imageCapture(frameOne)
                    window[self.config.get('WINDOW_MAIN','MAIN_IMAGE_LEFT_KEY')].update(data=byteFrameOne)
                    
            streamVideoOne.__del__()
            window.close()
                
        except Exception as e:
            streamVideoOne.__del__()
            window.close()
            print(e)
