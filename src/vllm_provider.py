# src/vllm_provider.py
import subprocess
import yaml
from config import settings
import os

# src/vllm_provider.py
import subprocess
import os
from config import settings

def start_vllm_server():
    command = [
        "python", "-m", "vllm.entrypoints.api_server",
        "--model", settings['model_path'],  # 여기서 '--model-path'를 '--model'로 변경
        "--host", settings['vllm_host'],
        "--port", str(settings['vllm_port'])
    ]

    # Mistral 모델은 토크나이저와 모델 파일을 로컬로 다운로드하여 사용합니다.
    # 사전 다운로드된 모델 경로를 지정해야 할 수 있습니다.
    if settings.get('model_path'):
        command.extend(["--model-path", settings['model_path']])

    # 환경 변수 설정 (필요한 경우)
    env = os.environ.copy()

    return subprocess.Popen(command, env=env)

if __name__ == "__main__":
    # 테스트 코드
    vllm_process = start_vllm_server()
    print("vLLM 서버가 시작되었습니다.")
    try:
        vllm_process.wait()
    except KeyboardInterrupt:
        print("vLLM 서버를 종료합니다.")
        vllm_process.terminate()
