import random
def simulate_payment():
    success = random.choice([True, False])
    if success:
        print("Payment successful!")
    else:
        print("Payment failed!")
    return success
