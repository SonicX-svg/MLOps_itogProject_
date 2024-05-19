#________________________________________test____________________________________________
import pytest
import os
import sys
from pathlib import Path
print(os.path.dirname(__file__))
parent_dir = Path(os.path.dirname(__file__)).parent
print(parent_dir)
sys.path.append(parent_dir)
print(os.path.dirname(__file__))
from tests.model_preprocessing import df
from tests.test_model import model_accuracy

def test_data():
    assert not df.isnull().sum()
    
def test_accuracy():
    assert model_accuracy>55 
    

