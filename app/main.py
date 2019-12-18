#Copyright 2019 Google LLC
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import requests

from flask import Flask
from flask import render_template

app = Flask(__name__)
retry = Retry(
  total=5,
  read=5,
  connect=5,
  backoff_factor=0.3,
  status_forcelist=(000, 500)
)


@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
