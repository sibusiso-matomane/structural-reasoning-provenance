import os
import json
from datetime import datetime

class ProvenanceEngine:

    def __init__(self, base_dir="runs"):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def create_run(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_path = os.path.join(self.base_dir, timestamp)
        os.makedirs(run_path, exist_ok=True)
        return run_path

    def save_input(self, run_path, text):
        with open(os.path.join(run_path, "input.txt"), "w") as f:
            f.write(text)

    def save_json(self, run_path, filename, data):
        with open(os.path.join(run_path, filename), "w") as f:
            json.dump(data, f, indent=2)

    def save_report(self, run_path, report_text):
        with open(os.path.join(run_path, "fragility_report.md"), "w") as f:
            f.write(report_text)
