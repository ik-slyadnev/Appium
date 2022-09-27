import allure
from allure_commons.types import AttachmentType
import requests
import os


def get_url_video(session_id: str):
    API_BROWSERSTACK = os.getenv('API_BROWSERSTACK')
    session = requests.Session()
    session.auth = (os.getenv('LOGIN'), os.getenv('KEY'))
    response = session.get(
        f'{API_BROWSERSTACK}/sessions/{session_id}.json')
    return response.json().get('automation_session').get('video_url')


def add_video(browser):
    video_url = f"https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.eu-west-1/{browser.driver.session_id}/video-" + browser.driver.session_id + ".mp4"
    html = f"<html><body><video width='100%' height='100%' controls autoplay><source src='{video_url}' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')
