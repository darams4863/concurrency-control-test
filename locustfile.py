from locust import HttpUser, TaskSet, task, between
from config.settings import Settings
import logging


# 로깅 설정
logging.basicConfig(level=logging.INFO)


"""
HttpUser: Locust의 기본 사용자 클래스입니다. HTTP 요청을 보낼 수 있습니다.
TaskSet: 사용자 행동을 정의하는 클래스입니다.
@task: Locust가 실행할 작업을 정의합니다. 데코레이터의 인수는 작업의 우선순위를 나타냅니다.
self.client.get("/api/endpoint"): 지정된 경로로 GET 요청을 보냅니다. 여기서 /api/endpoint는 테스트할 외부 API의 경로로 변경해야 합니다.
wait_time: 각 요청 사이의 대기 시간을 설정합니다.
"""

class UserBehavior(TaskSet):
    @task
    def call_hotpartners_api(self):
        # HOTPARTNERS API 호출
        self.client.get(Settings.BaseUrl.HOTPARTNERS + Settings.Endpoint.DEFAULT)

    @task
    def call_payment_validate_api(self):
        # PAYMENT_VALIDATE_SERVER API 호출
        self.client.get(Settings.BaseUrl.PAYMENT_VALIDATE_SERVER + Settings.Endpoint.DEFAULT)

    @task
    # def call_api(self):
    #     # 외부 API 호출
    #     self.client.get(Settings.BaseUrl.HOTPARTNERS + Settings.Endpoint.DEFAULT)
    def call_api(self):
        url = Settings.BaseUrl.HOTPARTNERS + Settings.Endpoint.DEFAULT
        response = self.client.get(url)
        if response.status_code == 200:
            logging.info(f"Success: {url}")
        else:
            logging.error(f"Failed: {url} with status code {response.status_code}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # 각 요청 사이의 대기 시간 (초)