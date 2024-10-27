# Smart Grid Monitoring System

## Overview
The Smart Grid Monitoring System is a Python-based simulation tool that models and monitors a smart electrical grid network. It simulates power generation from renewable sources (solar and wind) and power consumption by multiple consumers, providing real-time monitoring of grid stability and power balance.

## Features
- Real-time power generation monitoring for solar and wind sources
- Consumer power consumption tracking
- Grid stability analysis
- Power balance calculations
- Timestamped monitoring reports

## System Components

### SmartGridNode
The basic building block of the system, representing different types of grid participants:
- **Solar Nodes**: Generate between 20-80 MW of power
- **Wind Nodes**: Generate between 30-120 MW of power
- **Consumer Nodes**: Consume between 50-150 MW of power

#### Node Properties
- `node_id`: Unique identifier for each node
- `node_type`: Type of node ('solar', 'wind', 'consumer')
- `power`: Current power generation/consumption
- `status`: Operational status of the node

### SmartGridSystem
The main system class that manages the entire grid:

#### Key Methods
- `add_node()`: Adds new nodes to the grid
- `simulate_power_readings()`: Generates simulated power readings for all nodes
- `monitor_grid()`: Analyzes grid status and generates monitoring reports

## Monitoring Metrics
The system tracks several key metrics:
1. **Power Generation**
   - Solar power output
   - Wind power output
   - Total power generation

2. **Power Consumption**
   - Individual consumer readings
   - Total power consumption

3. **Grid Status**
   - Power balance (generation - consumption)
   - Grid stability status (Stable/Unstable)

## Grid Stability Criteria
- The grid is considered **Stable** when the power balance is within ±50 MW
- The grid is marked as **Unstable** when the power balance exceeds these limits

## Sample Usage
```python
# Initialize the system
grid = SmartGridSystem()

# Add nodes
grid.add_node(SmartGridNode('SOLAR1', 'solar'))
grid.add_node(SmartGridNode('WIND1', 'wind'))
grid.add_node(SmartGridNode('CONSUMER1', 'consumer'))

# Start monitoring
grid.simulate_power_readings()
status = grid.monitor_grid()
```

## Output Format
The system generates detailed monitoring reports including:
- Timestamp of readings
- Power generation breakdown (solar and wind)
- Individual consumer consumption
- Total power generation and consumption
- Grid stability status
- Power balance

## Implementation Details
- Written in Python 3.x
- Uses `random` for power simulation
- Uses `datetime` for timestamping
- Includes a 2-second delay between monitoring iterations
- Default monitoring runs for 10 iterations

## Dependencies
- Python 3.x
- Standard Python libraries:
  - `random`
  - `time`
  - `datetime`

## Notes
- This is a simulation tool and generates randomized power readings
- Power values are in Megawatts (MW)
- The system can be extended by adding more nodes of any type
- Monitoring interval can be adjusted by modifying the sleep duration
