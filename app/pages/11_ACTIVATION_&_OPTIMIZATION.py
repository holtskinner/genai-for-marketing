# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Initial page with an overview architecture and a description of each demo page.
"""

import streamlit as st
import base64
import tomllib


# Load configuration file
with open("./app_config.toml", "rb") as f:
    data = tomllib.load(f)

st.set_page_config(
    page_title=data["pages"]["11_activation_optimization"]["page_title"], 
    page_icon=data["pages"]["11_activation_optimization"]["page_icon"]
)

import utils_styles
utils_styles.sidebar_apply_style(
    style=utils_styles.style_sidebar,
    image_path=data["pages"]["11_activation_optimization"]["sidebar_image_path"]
)

file_name = data["pages"]["11_activation_optimization"]["file_name"]

with open(file_name, "rb") as fp:
    contents = fp.read()
    main_image = base64.b64encode(contents).decode("utf-8")
    main_image = 'data:image/png;base64,'+main_image

st.image(image=main_image)
