
from asyncio.windows_events import NULL
import random

maxValueOfPrivateKey = 10000

class Peer:
    
    secret_key = NULL
    prime = NULL
    g_base = NULL
    symetric_key = NULL

    def __init__(self):
        self.secret_key = self.GenereteSecretKey()


    def GenereteSecretKey(self):
        secret_key = random.randint(1,maxValueOfPrivateKey)
        return secret_key

    def Set_DH_Parameter(self, p,g):
        self.prime = p
        self.g_base = g
    
    def CalculateValueForOther(self):
        value = (self.g_base**self.secret_key) % self.prime
        return value 

    def CalculateSymetricKey(self, value):
        self.symetric_key = (value**self.secret_key) % self.prime
    
    def GetSymetricKey(self):
        return self.symetric_key
        
