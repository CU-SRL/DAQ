import json
import numpy as np
from hashlib import *

# cheemscoin impl 

cheems_ledger_1 = '{"palmer" : ["lyon", "100"], "palmer" : ["lyon", "200"], "lyon" : ["palmer", "300"], "nonce" : 69}'

cheems_ledger_1 = json.loads(cheems_ledger_1)


while( ((myHash := sha1(json.dumps(cheems_ledger_1).encode('utf-8')).hexdigest())[-2:]) != "00"):

    randINT = np.random.randint(1,1e8)
    print(randINT)

    cheems_ledger_1["nonce"] = randINT

    print(myHash)


print("mined")
print(myHash)

