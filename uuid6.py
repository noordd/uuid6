import uuid
from os import urandom


# this function creates version 6 uuid from a version 1 uuid
def uuid6():
    u = uuid.uuid1(int.from_bytes(urandom(6), 'big'))
    uh = u.hex
    time_low_one = uh[:5]
    time_low_two = uh[5:8]
    time_mid = uh[8:12]
    time_high = uh[13:16]
    rest = uh[16:]

    uh6 = time_high + time_mid + time_low_one + '6' + time_low_two + rest

    return uuid.UUID(hex=uh6)
