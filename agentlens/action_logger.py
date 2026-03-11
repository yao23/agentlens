import json
from datetime import datetime

LOG_FILE = "agent_actions.log"

def log_action(action_type, detail):

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": action_type,
        "detail": detail
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
