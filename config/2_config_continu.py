import pickle
import gymnasium as gym
import highway_env

config_dict = {
    "observation": {
        "type": "Kinematics",
        "vehicles_count": 5,
        "features": ["x", "y", "vx", "vy", "cos_h", "sin_h"],
        "absolute": False,
        "normalize": True,
    },
    "action": {
        "type": "ContinuousAction",
    },
    "lanes_count": 4,
    "vehicles_count": 10,
    "duration": 60,  # [s]
    "initial_spacing": 1.0,
    "collision_reward": -1.0,
    "right_lane_reward": 0.5,
    "high_speed_reward": 0.1,
    "lane_change_reward": 0,
    "reward_speed_range": [20, 30],
    "simulation_frequency": 15,  # [Hz]
    "policy_frequency": 5,  # [Hz]
    "other_vehicles_type": "highway_env.vehicle.behavior.IDMVehicle",
    "screen_width": 600,
    "screen_height": 150,
    "centering_position": [0.3, 0.5],
    "scaling": 5.5,
    "show_trajectories": False,
    "render_agent": True,
    "offscreen_rendering": False,
    "disable_collision_checks": False,
}

with open("2-highway-continuous-config.pkl", "wb") as f:
    pickle.dump(config_dict, f)

env = gym.make("highway-fast-v0", render_mode="human")
env.unwrapped.configure(config_dict)
env.reset()
while True:
    env.step([0,0])
