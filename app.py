import os
import time

def calculate_tax(salary):
    return salary * 0.20

if __name__ == "__main__":
    print("Application successfully initialized!")
    print(f"Sanity Check: Tax on 1000 is {calculate_tax(1000)}")
    print("Container process entering active listening state....")

    # 📡 Fetch variables inside the execution block
    env_mode = os.environ.get("APP_ENV", "development")
    db_string = os.environ.get("DATABASE_URL", "sqlite:///local.db")
    api_key = os.environ.get("API_SECRET_KEY", "fallback-key")
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    loop_interval = int(os.environ.get("LOOP_INTERVAL_SECONDS", 10))

    print(f"🚀 Worker starting up in [{env_mode}] mode with log level [{log_level}]...")
    print(f"⏱️ Dynamic loop interval configured to: {loop_interval} seconds")

    # ⚙️ This single loop keeps the worker pacing dynamically
    while True:
        print(f"⚙️ Running loop task... Secured API key is loaded into system environment.")
        time.sleep(loop_interval)
