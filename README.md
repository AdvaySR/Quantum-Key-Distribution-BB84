# 🔐 Quantum Key Distribution (BB84) Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Simulates quantum-secured key exchange with eavesdropping detection using Qiskit.

![BB84 Protocol](assets/protocol.png)
*(Diagram: BB84 key exchange process)*

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

## Features
- 🎯 **BB84 Protocol** implementation
- 🔍 **25% error rate** eavesdropping detection
- 📊 **Bloch sphere visualization** of qubit states
- ⚡ **Interactive key verification**

## Usage
```bash
# Clone repository
git clone https://github.com/yourusername/QKD-BB84-Simulator.git
cd QKD-BB84-Simulator

# Install dependencies
pip install -r requirements.txt

# Run simulation
python qkd_simulation.py
