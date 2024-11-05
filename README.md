# vLLMprovider
vLLM라이브러리를 이용한 엔드포인트 제공자.


project/
├── data/
│   └── userlogs/          # 시간별로 로그를 저장
├── src/
│   ├── main.py            # 애플리케이션 진입점
│   ├── vllm_provider.py   # 모델 설정 및 vLLM 서버 관리
│   ├── api_gateway.py     # API 게이트웨이, 엔드포인트 관리
│   ├── log_collector.py   # 로그 수집 및 저장
│   ├── config.py          # 설정 관리
│   └── utils/
│       └── helpers.py     # 유틸리티 함수들
├── config/
│   └── settings.yaml      # 설정 파일
├── tests/
│   └── test_main.py       # 테스트 코드
├── requirements.txt       # 필요한 패키지 목록
├── README.md              # 프로젝트 설명서
└── .gitignore             # Git에서 제외할 파일들