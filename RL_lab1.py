# Install packages
# !pip install gymnasium
# !pip install numpy
# !pip install matplotlib

import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

print("Gymnasium Version:", gym.__version__)


# Create the environment
env = gym.make("CartPole-v1")

# Reset the environment
observation, info = env.reset()

print("Initial Observation:")
print(observation)

print("\nEnvironment Information:")
print(info)

print("Observation Space:")
print(env.observation_space)

print("\nAction Space:")
print(env.action_space)

print("\nObservation Space Type:")
print(type(env.observation_space))

print("\nNumber of Possible Actions:")
print(env.action_space.n)



observation, info = env.reset()

done = False
step = 0
total_reward = 0

while not done:

    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

    step += 1
    total_reward += reward

    print(f"Step {step}")
    print(f"Action: {action}")
    print(f"Observation: {observation}")
    print(f"Reward: {reward}")
    print(f"Episode Finished: {done}")
    print("-"*40)

print("Episode Completed")
print("Total Steps:", step)
print("Total Reward:", total_reward)

env.close()



