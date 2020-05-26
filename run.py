#!/usr/bin/env python3

import platform
import os
from flaskr import create_app

os.system("export FLASK_APP=flaskr & export FLASK_ENV=production")

app = create_app()

app.run(host='0.0.0.0', debug=True, threaded=True)
