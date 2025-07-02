# CP216 ARM/Thumb Instruction Set Simulator

This project is a modular ARMv7 and 16-bit Thumb instruction set simulator developed for academic use in CP216: Introduction to Microprocessors. It simulates a simplified CPU with support for a subset of ARM and Thumb instructions, providing an environment for understanding instruction execution, register operations, memory interaction, and condition flags.

## Overview

The simulator executes ARM and Thumb binary programs at the instruction level. It is designed for educational purposes, allowing users to trace and analyze low-level instruction behavior through a Python-based simulation environment. The simulator emphasizes clarity, extensibility, and modular design.

## Features

* Supports both ARMv7 32-bit and Thumb 16-bit instruction sets
* Simulates a register file (R0–R15) including PC, LR, SP
* Emulates CPSR flags: Negative (N), Zero (Z), Carry (C), Overflow (V)
* Includes memory simulation (byte- and word-addressable)
* Implements condition code handling for conditional execution
* Modular architecture for ease of extension
* Instruction logging and post-execution state dump
* Designed for step-by-step debugging and educational clarity

## Supported Instructions

### ARM (32-bit)

* Data processing: `MOV`, `ADD`, `SUB`, `CMP`, `AND`, `ORR`, `EOR`, `MVN`, `TST`
* Memory access: `LDR`, `STR` (supports pre/post-indexing with offsets)
* Branching: `B`, `BL`, including conditional execution (e.g., `BEQ`, `BNE`, `BGE`)

### Thumb (16-bit)

* Arithmetic: `MOV`, `ADD`, `SUB`
* Comparison and control: `CMP`, `B`, `BL`, conditional branches
* Memory (limited): `LDR`, `STR`

## Getting Started

### Prerequisites

* Python 3.8 or higher
* Git and pip

### Installation

```bash
git clone https://github.com/sebasajeed/CP216-ARM-SIMULATOR.git
cd CP216-ARM-SIMULATOR
pip install -r requirements.txt
```

## Usage

Run the simulator with a compiled binary input:

```bash
cd simulator-python-files
python cpu_simulator/main.py path/to/test_arm.bin
```

Replace `test_arm.bin` with a compiled ARM or Thumb binary file. Sample binaries are provided in the repository for demonstration.

## Project Structure

```
simulator-python-files/
├── cpu/                  # Core CPU logic (registers, ALU, pipeline)
├── isa/                  # Decoding and instruction set implementation
├── memory/               # Memory handling
├── cpu_simulator/        # Entry point and configuration
├── output/               # Debugging and register dump utilities
├── test_programs/        # Sample binaries and test cases (user-provided)
```

## Sample Output

At the end of execution, the simulator prints the state of all general-purpose registers, the PC (program counter), SP (stack pointer), LR (link register), and the CPSR flags.

Example:

```
R0  : 00000001    R1  : 00000003    R2  : 00000000
...
SP  : 00000FF0    LR  : 00000018    PC  : 0000001C
CPSR: N=0 Z=1 C=0 V=0
```

## Contributing

Contributions are encouraged. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make changes with clear commit messages
4. Open a pull request describing your changes

Please ensure that any new instruction implementations follow the project's modular structure and are tested thoroughly.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
