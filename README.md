# Diphie_Helman_Scrpaer

Diphie Helman Algorithm for generating symetric key from an asymetric key.

Usually, asymetric keys validate high level encryption but also consume a lot of time and resources to handle the process.
Dipphie Helman Algorithem use mathematical proprties in order to generate 1 symetric key between to users.


Here is a more general description of the protocol

Alice and Bob agree on a finite cyclic group G of order n and a generating element g in G. (This is usually done long before the rest of the protocol;
g is assumed to be known by all attackers.) The group G is written multiplicatively.
Alice picks a random natural number a with 1 < a < n, and sends the element ga of G to Bob.
Bob picks a random natural number b with 1 < b < n, and sends the element gb of G to Alice.
Alice computes the element (gb)a = gba of G.
Bob computes the element (ga)b = gab of G.
Both Alice and Bob are now in possession of the group element gab = gba, which can serve as the shared secret key.


in this code I generated 256 bit prime number using selenium and execute Diphie Helman equations in order to generate 1 symetric key
