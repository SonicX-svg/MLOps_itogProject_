#________________________________________test____________________________________________
import pytest
import os
import sys
from pathlib import Path
sys.path.append('..')
print('os.path.abspath(os.curdir)', os.path.abspath(os.curdir))


from model_preprocessing import df
from test_model import model_accuracy

def test_data():
    assert not df.isnull().sum()
    
def test_accuracy():
    assert model_accuracy>55 
    

