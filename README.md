# CSE729 Project 1 - Modified BlockSim Simulator

This repository contains a modified version of the open-source **BlockSim** blockchain simulator. It was extended as part of the CSE729 Blockchain and Distributed Ledger coursework to analyze specific network parameters, transaction ordering mechanics, and economic incentives.

## Student Information
* **Name:** [Your Name]
* **Student ID:** [Your Student ID]
* **Group Member (if applicable):** [Member Name & ID]

## Custom Modifications (Section 2 Extensions)

This fork includes custom source code modifications to the Bitcoin model (`model = 1`) to simulate real-world blockchain design trade-offs:

### 1. FIFO Transaction Ordering (Experiment 3)
By default, the simulator uses a fee-priority ordering system. A toggle has been implemented in `Transaction.py` to allow the network to process transactions using a First-In-First-Out (FIFO) arrival-based order. 
* **How to configure:** Open `InputsConfig.py` and change the `ORDER_METHOD` variable to `"FEE"` for the default fee-priority, or `"FIFO"` to process transactions strictly by their arrival time.

### 2. Block Reward Halving (Experiment 4)
The default `Incentives.py` script provided a static, eternal block reward. The codebase has been modified to include a dynamic halving mechanism that exponentially decays the block reward over time, mimicking Bitcoin's disinflationary supply schedule.
* **How to configure:** Open `InputsConfig.py` and adjust the `HALVING_INTERVAL` variable (e.g., 20, 40, 60, 80) to dictate how many blocks must be mined before the block reward is cut in half.

---

## Original BlockSim Documentation

### What is BlockSim Simulator?
**BlockSim** is an open source blockchain simulator, capturing network, consensus and incentives layers of blockchain systems. BlockSim aims to provide simulation constructs that are intuitive, hide unnecessary detail and can be easily manipulated to be applied to a large set of blockchains design and deployment questions. BlockSim is implemented in **Python**.

### Installation and Requirements
Before you can use BlockSim simulator, you need to have **Python version 3 or above** installed in your machine as well as have the following packages installed:

- pandas (`pip install pandas`)
- numpy (`pip install numpy`)
- sklearn (`pip install scikit-learn`)
- xlsxwriter (`pip install xlsxwriter`)

### Running the simulator
Before you run the simulator, you can access the configuration file `InputsConfig.py` to choose the model of interest (Base Model 0, Bitcoin Model 1 and Ethereum Model 2) and to set up the related parameters. 

To run the simulator, trigger the main class `Main.py` from the command line:
> python Main.py

### Statistics and Results
The results of the simulator are printed in an Excel file at the end of the simulation. The results include the blockchain ledger, number of blocks mined, number of stale (uncles) blocks and the rewards gained by each miner.