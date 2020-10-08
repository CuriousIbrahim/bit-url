from app import app
import os
import sys

file_dir = "/usr/src/biturl"
sys.path.append(file_dir)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
