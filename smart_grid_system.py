import random
import time
from datetime import datetime

class SmartGridNode:
    def __init__(self, node_id, node_type):
        self.node_id = node_id
        self.node_type = node_type  # 'solar', 'wind', 'consumer'
        self.power = 0
        self.status = 'active'

class SmartGridSystem:
    def __init__(self):
        self.nodes = []
        
    def add_node(self, node):
        self.nodes.append(node)
        print(f"Added {node.node_type} node: {node.node_id}")
        
    def simulate_power_readings(self):
        for node in self.nodes:
            if node.node_type == 'solar':
                # Solar power varies between 20-80 MW
                node.power = random.uniform(20, 80)
            elif node.node_type == 'wind':
                # Wind power varies between 30-120 MW
                node.power = random.uniform(30, 120)
            else:  # consumer
                # Consumption varies between 50-150 MW
                node.power = random.uniform(50, 150)
                
    def monitor_grid(self):
        solar_power = sum(node.power for node in self.nodes 
                         if node.node_type == 'solar')
        wind_power = sum(node.power for node in self.nodes 
                        if node.node_type == 'wind')
        total_generation = solar_power + wind_power
        
        # Get individual consumer readings
        consumer_readings = {node.node_id: round(node.power, 2) 
                           for node in self.nodes 
                           if node.node_type == 'consumer'}
        total_consumption = sum(consumer_readings.values())
        
        balance = total_generation - total_consumption
        stability = "Stable" if abs(balance) < 50 else "Unstable"
        
        return {
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'solar_power': round(solar_power, 2),
            'wind_power': round(wind_power, 2),
            'total_generation': round(total_generation, 2),
            'consumer_readings': consumer_readings,
            'total_consumption': round(total_consumption, 2),
            'balance': round(balance, 2),
            'status': stability
        }

def main():
    # Initialize system
    grid = SmartGridSystem()
    
    # Add some nodes
    grid.add_node(SmartGridNode('SOLAR1', 'solar'))
    grid.add_node(SmartGridNode('WIND1', 'wind'))
    grid.add_node(SmartGridNode('CONSUMER1', 'consumer'))
    grid.add_node(SmartGridNode('CONSUMER2', 'consumer'))
    
    print("\nStarting grid monitoring (will run for 10 iterations)...")
    print("=" * 70)
    
    # Monitor for 10 iterations
    for i in range(10):
        grid.simulate_power_readings()
        status = grid.monitor_grid()
        
        print(f"\nIteration {i+1} - Timestamp: {status['timestamp']}")
        print("-" * 70)
        print("POWER GENERATION:")
        print(f"Solar Power: {status['solar_power']} MW")
        print(f"Wind Power: {status['wind_power']} MW")
        print(f"Total Generation: {status['total_generation']} MW")
        
        print("\nPOWER CONSUMPTION:")
        for consumer, power in status['consumer_readings'].items():
            print(f"{consumer}: {power} MW")
        print(f"Total Consumption: {status['total_consumption']} MW")
        
        print("\nGRID STATUS:")
        print(f"Power Balance: {status['balance']} MW")
        print(f"Grid Stability: {status['status']}")
        print("=" * 70)
        
        time.sleep(2)  # Wait 2 seconds before next reading
    
    print("\nMonitoring complete!")

if __name__ == "__main__":
    main()