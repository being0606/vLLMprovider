from vllm import LLM


def create_llm_instance(model_path, tensor_parallel_size=2, gpu_memory_utilization=0.9):
    """
    LLM 인스턴스를 생성하는 공통 함수.
    """
    return LLM(
        model=model_path,
        tensor_parallel_size=tensor_parallel_size,  # 사용하려는 GPU 수
        gpu_memory_utilization=gpu_memory_utilization,  # GPU 메모리 사용률 제한
        max_num_seqs=32,  # 동시에 처리할 최대 시퀀스 수
        cpu_offload_gb=128,  # 부족한 메모리를 CPU로 오프로드
    )

def start_server(model_path):
    """
    vLLM 서버를 시작하는 함수.
    """
    llm = create_llm_instance(model_path)
    print("Starting vLLM server on port 8000...")
    llm.serve(
        host="0.0.0.0",  # 모든 네트워크 인터페이스에서 접근 가능
        port=8000,  # 서버 포트
        enforce_eager=True,  # Eager Mode 활성화
    )


def run_interactive_mode(model_path):
    """
    대화형 모드를 실행하는 함수.
    """
    print("Initializing model for interactive mode...")
    llm = create_llm_instance(model_path, gpu_memory_utilization=0.9)

    while True:
        user_input = input("\n[Input] Enter your prompt (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting interactive mode. Goodbye!")
            break

        # 모델 응답 생성
        print("[Processing] Generating response...")
        outputs = llm.generate(user_input)
        response = outputs[0].outputs[0].text
        print(f"[Output] {response}")


if __name__ == "__main__":
    # 공통된 모델 경로 설정
    model_path = "/home/huggingface_cache/hub/models--Qwen--Qwen2.5-72B-Instruct-GPTQ-Int4/snapshots/da6e9d45661b91e02782f4ae2c6bb39c4a5b4821"

    # 모드 선택
    mode = input("Choose mode (1: Server, 2: Interactive): ").strip()
    if mode == "1":
        start_server(model_path)
    elif mode == "2":
        run_interactive_mode(model_path)
    else:
        print("Invalid mode. Please choose 1 or 2.")
