# Copyright 2022 The Casdoor Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from casdoor import CasdoorSDK

certificate = '''-----BEGIN CERTIFICATE-----
MIIE+TCCAuGgAwIBAgIDAeJAMA0GCSqGSIb3DQEBCwUAMDYx...
-----END CERTIFICATE-----'''

class Config:
    CASDOOR_SDK = CasdoorSDK(
        endpoint='http://localhost:8000',
        client_id='<client_id>',
        client_secret='<client_secret>',
        certificate=certificate,
        org_name='built-in',
        application_name='app-built-in',
        front_endpoint='http://localhost:8000'
    )
    REDIRECT_URI = 'http://localhost:5000/api/signin'
    SECRET_TYPE = 'filesystem'
    SECRET_KEY = os.urandom(24)
