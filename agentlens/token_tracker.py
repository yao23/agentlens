import json
from datetime import datetime

TOKEN_FILE = "token_usage.log"

def track_tokens(model, tokens, cost):

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "model": model,
        "tokens": tokens,
        "cost": cost
    }

    with open(TOKEN_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
