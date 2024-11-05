# src/main.py
from vllm_provider import start_vllm_server
import uvicorn
from config import settings

if __name__ == "__main__":
    vllm_process = start_vllm_server()
    try:
        uvicorn.run("api_gateway:app", host=settings['api_host'], port=settings['api_port'])
    except KeyboardInterrupt:
        pass
    finally:
        vllm_process.terminate()
