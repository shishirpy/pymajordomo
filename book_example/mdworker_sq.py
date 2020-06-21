import sys
from mdwrkapi import MajorDomoWorker

def main():
    """
    This is the main function
    """
    print(main.__doc__)
    verbose = '-v' in sys.argv
    worker = MajorDomoWorker("tcp://localhost:5555", b"square", verbose)
    reply = None
    while True:
        request = worker.recv(reply)
        if request is None:
            break

        # print(request)
        num = int(request[0].decode())
        # print(num)
        reply = [str(num ** 2).encode()]


if __name__ == "__main__":
    main()