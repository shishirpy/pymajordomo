

"""
Majordomo Protocol client example. Uses the mdcli API to hide all MDP aspects

Author : Min RK <benjaminrk@gmail.com>

"""

import sys
import time
import random
from mdcliapi import MajorDomoClient

def main():
    verbose = '-v' in sys.argv
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    count = 0
    while count < 10:
        request = str(random.randint(20, 99)).encode()
        try:
            reply = client.send(b"square", request)
            print(request.decode(), reply[0].decode())
            time.sleep(1)
        except KeyboardInterrupt:
            break
        else:
            # also break on failure to reply:
            if reply is None:
                break
        count += 1
    print ("%i requests/replies processed" % count)

if __name__ == '__main__':
    main()
