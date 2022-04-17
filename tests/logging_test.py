"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import pytest
from app import create_app
from app.cli import create_log_folder
import datetime
import os 
from app import * 
from flask import current_app

def test_info_log_file_created(client):
    """This makes the task runner"""
    root = os.getcwd() #os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs') 
    assert os.path.exists(logdir) == True
    assert os.path.exists(os.path.join(logdir, 'info.log')) == True

def test_debug_log_file_created(client):
    """This makes the task runner"""
    root = os.getcwd() #os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs') 
    assert os.path.exists(logdir) == True
    assert os.path.exists(os.path.join(logdir, 'debug.log')) == True