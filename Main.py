import random
from Peer import Peer
from Prime import Prime



peer1 = Peer()
peer2 = Peer()

pInstance = Prime()
prime = pInstance.GetPrime()
g = random.randint(1,prime)

peer1.Set_DH_Parameter(prime,g)
peer2.Set_DH_Parameter(prime,g)
peer1.CalculateSymetricKey(peer2.CalculateValueForOther())
peer2.CalculateSymetricKey(peer1.CalculateValueForOther())
print("PRIME NUMBER GENERETED:  " + str(prime))
print("KEY OF PEER1 (SYMETRIC):  " + str(peer1.GetSymetricKey()))
print("KEY OF PEER1 (SYMETRIC):  " + str(peer2.GetSymetricKey()))