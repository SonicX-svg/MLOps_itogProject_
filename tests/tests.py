#________________________________________test____________________________________________
import pytest
import os
import sys
from pathlib import Path

# Расчёт пути к родительской директории
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Проверка наличия родительской директории в sys.path
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from model_preprocessing import df
from test_model import model_accuracy

def test_data():
    assert not df.isnull().sum()
    
def test_accuracy():
    assert model_accuracy>55 
    

