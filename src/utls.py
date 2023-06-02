import datetime
import time

def wait_for_next_round_hour():
    current_time = datetime.datetime.now()
    next_hour = current_time.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(hours=0.5)+ datetime.timedelta(seconds=10) 
    time_to_wait = round((next_hour - current_time).total_seconds(), 0)
    print(f'Waiting {time_to_wait} seconds for next hour candles...')
    time.sleep(time_to_wait)
    # Optional: Print a message once the waiting is over
    print("Next hour candles has arrived!")