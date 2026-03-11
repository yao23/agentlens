import json

TOKEN_FILE = "token_usage.log"

def daily_cost():

    total = 0

    try:
        with open(TOKEN_FILE) as f:
            for line in f:
                event = json.loads(line)
                total += event["cost"]
    except FileNotFoundError:
        return 0

    return total
