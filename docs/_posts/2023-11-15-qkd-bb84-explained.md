---
layout: post
title: "How I Built a Quantum Key Distribution Simulator"
date: 2023-11-15
tags: [quantum-computing, qiskit, cryptography]
---

![BB84 Protocol]
```mermaid
flowchart TD
    A[Alice] -->|1. Prepares Qubits| B((" "))
    B -->|2. Sends| C[Bob]
    D[Eve] -.->|3. May Intercept| B
    C -->|4. Measures| E((" "))
    E -->|5. Reveals Bases| F{Key Sifting}
    F -->|6. Final Key| G[Shared Key]
    style D fill:#f9d5d5,stroke:#ff3333
    linkStyle 2 stroke:#ff3333,stroke-dasharray:3
```

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
```
---
Key Features
✅ Eavesdropping detection (25% error rate)

📊 Bloch sphere visualization (see below)
![Bloch Sphere](/assets/bloch_sphere.png)

---
Try It Yourself

git clone https://github.com/yourusername/QKD-BB84-Simulator.git
pip install -r requirements.txt
python qkd_simulation.py
---
