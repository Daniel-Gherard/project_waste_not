# Problem 01

## timer.py

Contains the class and methods to instanciate and run the timer.

This code will start the timer:
```
timer = Timer()
timer.start_timer()
```

This code will end the timer:
```
timer.end_timer()
```

This code will show the difference:
```
timer.duration()
```

This code will return the human readable value:
```
timer.human_readable_time()
```

## test.py

Contains some test cases for the class.

## test_application.py

Contains 2 functions using the timer and another function using just time.time() to validate the results further.