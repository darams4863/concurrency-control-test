# concurrency-control-test
Concurrency control test using Locust


## 실행 환경 구축
```bash
./scripts/setup.sh
```

## 테스트 실행
```bash
locust -f locustfile.py --host=http://localhost:8000
```