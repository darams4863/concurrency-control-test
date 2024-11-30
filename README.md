# concurrency-control-test
Concurrency control test using Locust


## 실행 환경 구축
```bash
./scripts/setup.sh
```

## 테스트 실행
```bash
# 웹 인터페이스로 실행
locust -f test_cases/locustfile.py --host=http://localhost:8000

# 웹 인터페이스 없이 명령줄에서 직접 테스트 (cf. 5명의 가상 사용자가 1초당 5명의 사용자를 시뮬레이션)
locust -f test_cases/locustfile.py --host=http://localhost:8000 -u 5 -r 5 --run-time 1s --headless
```