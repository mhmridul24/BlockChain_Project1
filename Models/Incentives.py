from InputsConfig import InputsConfig as p
from Models.Consensus import Consensus as c

class Incentives:
    
    @staticmethod
    def distribute_rewards():
        # Map node IDs to node objects for faster lookup
        node_map = {m.id: m for m in p.NODES}

        # Use enumerate to get the 'block_height' (0, 1, 2, 3...) as the chain grows
        for block_height, bc in enumerate(c.global_chain):
            miner_node = node_map.get(bc.miner)
            
            if miner_node:
                miner_node.blocks += 1
                
                # --- TASK 4A HALVING LOGIC ---
                # Calculate how many times the interval has passed
                halvings_occurred = block_height // p.HALVING_INTERVAL
                
                # Calculate the new reward (Original reward divided by 2^halvings)
                current_reward = p.Breward / (2 ** halvings_occurred)
                
                # Add the newly calculated reward instead of the static p.Breward
                miner_node.balance += current_reward 
                # ------------------------------
                
                tx_fee = Incentives.transactions_fee(bc)
                miner_node.balance += tx_fee # add transaction fees to balance

    @staticmethod
    def transactions_fee(bc):
        return sum(tx.fee for tx in bc.transactions)