from pydantic import BaseModel, validators
from typing import List, Optional
import logging #importar libreria para loging
from dotenv import load_dotenv
import os
#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')