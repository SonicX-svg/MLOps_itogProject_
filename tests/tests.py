#________________________________________test____________________________________________
import pytest
import os
import sys
from pathlib import Path
parent_dir = Path(os.path.dirname(__file__)).parent
sys.path.append(parent_dir)
print(os.path.dirname(__file__))
from model_preprocessing import df
from test_model import model_accuracy

def test_data():
    assert not df.isnull().sum()
    
def test_accuracy():
    assert model_accuracy>55 
    

