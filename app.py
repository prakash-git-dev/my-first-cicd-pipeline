import time

def calculate_tax(salary):
    return salary * 0.20

if __name__ == "__main__":
    print("Application successfully initialized!")
    print(f"Sanity Check: Tax on 1000 is {calculate_tax(1000)}")
    print("Container process entering active listening state...")
    
    # Simple non-terminating worker loop to keep the pod running
    while True:
        time.sleep(3600)



