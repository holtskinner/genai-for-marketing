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
Marketing Insights demonstration: 
- Render Looker Dashboards with marketing data
- Create personalized headlines and images for marketing campaigns
- Translate content
"""


import streamlit as st
import streamlit.components.v1 as components
import tomllib


# Load configuration file
with open("./app_config.toml", "rb") as f:
    data = tomllib.load(f)

st.set_page_config(
    page_title=data["pages"]["13_campaign_performance"]["page_title"], 
    page_icon=data["pages"]["13_campaign_performance"]["page_icon"],
    layout='wide'
)

import utils_styles
utils_styles.sidebar_apply_style(
    style=utils_styles.style_sidebar,
    image_path=data["pages"]["13_campaign_performance"]["sidebar_image_path"]
)

# Set project parameters 
PROJECT_ID = data["global"]["project_id"]
LOCATION = data["global"]["location"]
TEXT_MODEL_NAME = data["models"]["text"]["text_model_name"]
IMAGE_MODEL_NAME = data["models"]["image"]["image_model_name"]

DASHBOARDS = data["pages"]["13_campaign_performance"]["dashboards"]
INFOBOT = data["pages"]["13_campaign_performance"]["infobot"]

# State variables
PAGE_KEY_PREFIX = "CampaignPerformance"
DASHBOARD_KEY = f"{PAGE_KEY_PREFIX}_Dashboard"

cols = st.columns([15,70,15])
with cols[1]:
    cols = st.columns([10, 90])
    with cols[0]:
        st.image('/app/images/opt_icon.png')
    with cols[1]:
        st.title('Campaign Performance')

    st.write("This page presents visualizations of marketing data "
             "in the form of Looker Dashboards.")

    if DASHBOARDS:
        with st.form(key='generate_marketing_dashboard'):
            option = st.selectbox(
                'Select a dashboard to be displayed',
                tuple(DASHBOARDS.keys()))

            submit_button = st.form_submit_button(label='Generate Dashboard')

        if submit_button:
            st.session_state[DASHBOARD_KEY] = option
    else:
        st.info('Dashboards not available.')

if DASHBOARD_KEY in st.session_state:
    components.html(
        f'<iframe src="{DASHBOARDS.get(st.session_state[DASHBOARD_KEY])}" '
        f'frameborder="0" width="100%" height="800px"></iframe>{INFOBOT}', 
        height=800)
