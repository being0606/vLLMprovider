# src/api_gateway.py
from fastapi import FastAPI, Request
import httpx
from config import settings
from log_collector import log_interaction
from utils.helpers import format_prompt

app = FastAPI()
vllm_base_url = f"http://{settings['vllm_host']}:{settings['vllm_port']}"

@app.post("/v1/completions")
async def completions(request: Request):
    user_input = await request.json()
    original_prompt = user_input.get('prompt', '')
    formatted_prompt = format_prompt(original_prompt)
    user_input['prompt'] = formatted_prompt

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{vllm_base_url}/v1/completions", json=user_input)

    response_json = response.json()
    await log_interaction(user_input, response_json)
    return response_json

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    user_input = await request.json()
    messages = user_input.get('messages', [])
    if messages and messages[-1]['role'] == 'user':
        original_prompt = messages[-1]['content']
        formatted_prompt = format_prompt(original_prompt)
        messages[-1]['content'] = formatted_prompt
        user_input['messages'] = messages

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{vllm_base_url}/v1/chat/completions", json=user_input)

    response_json = response.json()
    await log_interaction(user_input, response_json)
    return response_json
