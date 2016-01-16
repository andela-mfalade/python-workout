import threading
import time

"""How does the timer_lock class work

To the best of my knowledge, I think it locks down resources shared
by multiple threads such that when one thread acquires the Lock, the
other thread does not have access to the resources but has to wait till
the first timer releases the lock.
"""
timer_lock = threading.Lock()


def timer(name, delay, repeat):
    print "Timer: {} Started.".format(name)
    timer_lock.acquire()
    print "{} has acquired the lock.".format(name)
    while repeat > 0:
        time.sleep(delay)
        print "{}: {} ".format(name, str(time.ctime(time.time())))
        repeat -= 1
    print "{} is releasing the lock.".format(name)
    timer_lock.release()
    print "TImer, {} Completed.".format(name)


def main():
    t1 = threading.Thread(target=timer, args=("Thread1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Thread2", 2, 5))
    t1.start()
    t2.start()
    print "Main complete."


if __name__ == "__main__":
    main()
