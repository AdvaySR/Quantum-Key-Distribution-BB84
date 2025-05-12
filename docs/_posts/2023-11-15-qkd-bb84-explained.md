---
layout: post
title: "How I Built a Quantum Key Distribution Simulator"
date: 2023-11-15
tags: [quantum-computing, qiskit, cryptography]
---

![BB84 Protocol]({{ site.baseurl }}/assets/protocol.png)

## Why Quantum Cryptography?
- Traditional encryption (RSA) will be broken by quantum computers
- BB84 protocol uses quantum mechanics for **provable security**

## How My Simulator Works
```python
# Key generation snippet
def encode_qubit(bit, basis):
    qc = QuantumCircuit(1)
    if basis == '×': qc.h(0)
    if bit == 1: qc.x(0)
    return qc 


