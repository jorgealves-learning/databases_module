#Imports
import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import pyscopg2


#Variables
process_number = 10
record_number = 1000
JSON_PATH = Path(__file__).parent / "jsonChallenge1.json"
env_path = find_dotend(raise_error_if_not_found=True)
load_dotenv(env_path)