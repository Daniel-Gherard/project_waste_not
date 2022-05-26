from timer import Timer
import time

def sum():
    calculation = 0

    for i in range(0, 100):
        calculation += i

    return calculation

def minus():
    calculation = 0

    for i in range(0, 100):
        calculation -= i

    return calculation

def main():
    timer_sum = Timer()
    timer_sum.start_timer()
    print('Running Sum:')
    sum()
    timer_sum.end_timer()
    print('Duration: ' + str(timer_sum.duration()))
    print(timer_sum.human_readable_time())

    timer_minus = Timer()
    timer_minus.start_timer()
    print('Running Minus:')
    minus()
    timer_minus.end_timer()
    print('Duration: ' + str(timer_minus.duration()))
    print(timer_minus.human_readable_time())

    start = time.process_time()
    print('Running with Sum just time.process_time()')
    sum()
    end = time.process_time()
    duration = end - start
    print('Duration: ' + str(duration))
    print(timer_sum.human_readable_time(duration))

if __name__ == '__main__':
	main()