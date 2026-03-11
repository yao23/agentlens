import time
from .action_logger import log_action
from .token_tracker import track_tokens

class Monitor:

    def __init__(self):
        self.start_time = time.time()

    def action(self, action_type, detail):
        log_action(action_type, detail)

    def tokens(self, model, tokens, cost):
        track_tokens(model, tokens, cost)


monitor = Monitor()
