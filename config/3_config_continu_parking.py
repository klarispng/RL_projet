import pickle
import gymnasium as gym
import highway_env

config_dict = {
    "observation": {
        "type": "KinematicsGoal",
        "features": ['x', 'y', 'vx', 'vy', 'cos_h', 'sin_h'],
        "scales": [100, 100, 5, 5, 1, 1],
        "normalize": False
    },
    "action": {
        "type": "ContinuousAction"
    },
    "simulation_frequency": 15,
    "policy_frequency": 5,
    "screen_width": 600,
    "screen_height": 300,
    "centering_position": [0.5, 0.5],
    "scaling": 7,
    "show_trajectories": False,
    "render_agent": True,
    "offscreen_rendering": False
}

with open("3-parking-continuous-config.pkl", "wb") as f:
    pickle.dump(config_dict, f)

env = gym.make("parking-v0", render_mode="human")
env.unwrapped.configure(config_dict)
env.reset()
while True:
    env.step([0,0])
