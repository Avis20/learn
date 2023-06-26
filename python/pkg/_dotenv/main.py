import os
from dotenv import load_dotenv

load_dotenv()

debug = os.getenv('DEBUG', False)
print(debug)
print(os.getenv('DEBUG'))

debugG = os.getenv('DEBUGG', False)
print(debugG)
print(os.getenv('DEBUGG'))
