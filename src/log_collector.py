# src/log_collector.py
import json
from datetime import datetime
import os
import aiofiles

async def log_interaction(request_data, response_data):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "request": request_data,
        "response": response_data
    }
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    log_dir = "data/userlogs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{date_str}.log")
    async with aiofiles.open(log_file, "a") as f:
        await f.write(json.dumps(log_entry) + "\n")
