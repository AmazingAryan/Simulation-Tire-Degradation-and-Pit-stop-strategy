import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Initial settings
total_laps = 50  # Total number of laps in the race
initial_lap_time = 90  # Base lap time in seconds (without degradation)

# Degradation rates for different tire types
tire_degradation_rates = {
    'soft': 0.1,   # Soft tires degrade faster
    'medium': 0.05,  # Medium tires
    'hard': 0.02    # Hard tires degrade slower
}

pit_stop_time = 20  # Time lost during a pit stop in seconds

def simulate_lap_times(total_laps, degradation_rate):
    # Each lap, the tire wears down and lap time increases
    lap_times = []
    for lap in range(total_laps):
        lap_time = initial_lap_time + lap * degradation_rate
        lap_times.append(lap_time)
    return lap_times

def simulate_race_with_pit_stops(total_laps, pit_stop_laps, tire_degradation_rate):
    lap_times = []
    for lap in range(total_laps):
        if lap in pit_stop_laps:
            lap_times.append(pit_stop_time + initial_lap_time)  # Reset tire after pit stop
        else:
            lap_time = initial_lap_time + lap * tire_degradation_rate
            lap_times.append(lap_time)
    return lap_times

def optimize_pit_stop_strategy(total_laps, tire_degradation_rate, pit_lap_options):
    best_time = float('inf')
    best_strategy = None

    for pit_lap in pit_lap_options:
        lap_times = simulate_race_with_pit_stops(total_laps, [pit_lap], tire_degradation_rate)
        total_race_time = sum(lap_times)
        if total_race_time < best_time:
            best_time = total_race_time
            best_strategy = pit_lap

    return best_strategy, best_time

if __name__ == "__main__":
    # Optimize the pit stop strategy for soft tires
    pit_lap_options = [15, 25, 35]  # Example pit stop lap options
    best_pit_lap, best_time = optimize_pit_stop_strategy(total_laps, tire_degradation_rates['soft'], pit_lap_options)

    print(f"Best pit stop lap: {best_pit_lap} with total race time: {best_time} seconds")
    
    # Use the best pit stop lap to simulate and plot the race
    soft_tire_lap_times = simulate_race_with_pit_stops(total_laps, [best_pit_lap], tire_degradation_rates['soft'])

    # Plot lap times
    plt.plot(soft_tire_lap_times, label=f'Soft Tires with Pit Stop at Lap {best_pit_lap}')
    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (seconds)')
    plt.title('Tire Degradation and Pit Stop Strategy')
    plt.legend()
    plt.show()
