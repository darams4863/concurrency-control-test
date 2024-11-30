import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()


class Settings:
    class BaseUrl:
        HOTPARTNERS = os.getenv("HOTPARTNERS_API_BASE_URL")
        PAYMENT_VALIDATE_SERVER = os.getenv("PAYMENT_VALIDATE_SERVER_API_BASE_URL")

    class Endpoint:
        DEFAULT = os.getenv("DEFAULT_ENDPOINT")
