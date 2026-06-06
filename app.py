import os
import time
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Kubernetes! The Sidecar Bridge works perfectly!\n"

def calculate_tax(salary):
    return salary * 0.20

# 🧵 This worker function will run safely in a background thread
def background_worker():
    env_mode = os.environ.get("APP_ENV", "development")
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    loop_interval = int(os.environ.get("LOOP_INTERVAL_SECONDS", 10))
    
    print(f"🚀 Background Worker starting up in [{env_mode}] mode with log level [{log_level}]...")
    print(f"⏱️ Dynamic loop interval configured to: {loop_interval} seconds")
    
    while True:
        print(f"⚙️ Running loop task... Secured API key is loaded into system environment.")
        time.sleep(loop_interval)

if __name__ == "__main__":
    print("Application successfully initialized!")
    print(f"Sanity Check: Tax on 1000 is {calculate_tax(1000)}")
    
    # 🏎️ Spin up the background thread before starting the web server
    worker_thread = threading.Thread(target=background_worker, daemon=True)
    worker_thread.daemon = True
    worker_thread.start()
    
    # 📡 Start our web service listener on port 5000
    app.run(host='0.0.0.0', port=5000)
