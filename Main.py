from pathlib import Path
import os
import PySimpleGUI as pysimpleGUI
from configparser import ConfigParser
from bookScannerSingle import SingleScan
from bookScannerMultiple import ScanMultiple

config = ConfigParser()
config.read(f'{os.path.join(Path(__file__).resolve().parent,"configration")}/bookScanner.cfg')
pysimpleGUI.theme(config.get('GENERAL_WINDOW','WINDOW_MAIN_THEME'))

layout = [
    [pysimpleGUI.T("Select Scanning Style")],
    [pysimpleGUI.B("Single"),pysimpleGUI.B("Multiple")]
]


window = pysimpleGUI.Window(config.get('GENERAL_WINDOW','WINDOW_TITLE'),layout,finalize=True,resizable=True) 
event, values = window.read()    
window.close()
if event == 'Single':
     startSingle = SingleScan()
     startSingle.startMain()
if event == 'Multiple':
     scannmultiple = ScanMultiple()
     scannmultiple.startMain()