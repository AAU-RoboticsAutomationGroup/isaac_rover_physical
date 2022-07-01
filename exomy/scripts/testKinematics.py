from utils.model import Policy, Value
import torch
from skrl.agents.torch.ppo import PPO, PPO_DEFAULT_CONFIG
from typing import Union
from gym.spaces import Box
import gym
import math
from utils.kinematics import Ackermann
from utils.initRobot import Rover
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time
from utils.kinematicsCPU import kinematicsCPU

def load_checkpoint(checkpoint, model):
    print("=> Loading checkpoint")
    model.load_state_dict(checkpoint["state_dict"])



def load_model(model_name, features=[512,256,128]):
    observation_space = Box(-math.inf,math.inf,(3,))
    action_space = Box(-1.0,1.0,(2,))
    model = Policy(observation_space=observation_space, action_space=action_space, features=features)
    checkpoint = torch.load(model_name)
   # model.load_state_dict(checkpoint['state_dict'])
    model.eval()
    model.cuda()
    return model

def load_value(model_name, features=[512,256,128]):
    observation_space = Box(-math.inf,math.inf,(3,))
    action_space = Box(-1.0,1.0,(2,))
    model = Value(observation_space=observation_space, action_space=action_space, features=features)
    checkpoint = torch.load(model_name)
   # model.load_state_dict(checkpoint['state_dict'])
   # model.eval()
    #model.cuda()
    return model


# model = load_model('../resource/policies/822000_policy.pt', features=[512,256,128])
# value = load_value('../resource/policies/822000_policy.pt', features=[512,256,128])
# a = torch.tensor([ [3.2,2.38,1.7]])

# cfg_ppo = PPO_DEFAULT_CONFIG.copy()
# test = {"policy" : model,
#        "value" : value}
# b = [3]
# observation_space = Box(-math.inf,math.inf,(3,))
# action_space = Box(-1.0,1.0,(2,))
# print(a)
# print(action_space)
# print(observation_space.shape[0])
# agent = PPO(models=test,
#             memory=None, 
#             cfg=cfg_ppo, 
#             observation_space=observation_space, 
#             action_space=action_space,
#             device='cuda:0')


# i2c_bus = busio.I2C(SCL, SDA)
# pwm = PCA9685(i2c_bus)

# # For most motors a pwm frequency of 50Hz is normal
# pwm_frequency = 50.0  # Hz
# pwm.frequency = pwm_frequency

robot = Rover()
#robot.setMotorsFromKinematics(Ackermann(torch.tensor(0).unsqueeze(), torch.tensor(1).unsqueeze() ))
#observation_space[2]
#vel = agent.policy.act(a,inference=True)
#print(vel)
# print(torch.unsqueeze(vel[0][0][0], 0))
# print(torch.unsqueeze(vel[0][0][1], 0))

#steering_angles, motor_velocities = Ackermann(torch.tensor( [1.0], device='cuda:0'), torch.tensor([ 0.2], device='cuda:0'))
start = time.perf_counter()
steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(1.0, 0.0)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
finish = time.perf_counter() - start
print(finish)
time.sleep(5)

steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(-1.0, 0.0)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
time.sleep(5)

steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(0.0, 1.0)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
time.sleep(5)

steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(0.0, -1.0)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
time.sleep(5)

steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(1.0, 0.25)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
time.sleep(5)

steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(-1.0, -0.25)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
time.sleep(5)

steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(1.0, -0.25)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
time.sleep(5)

steering_anglesCPU, motor_velocitiesCPU = kinematicsCPU(-1.0, 0.25)
robot.setMotorsFromKinematics(steering_anglesCPU, motor_velocitiesCPU)
time.sleep(5)


#a = torch.tensor([ [1.2,1.38,0.7]])
#vel = agent.policy.act(a,inference=True)
#print(vel)

#steering_angles, motor_velocities = Ackermann(torch.tensor( [0.0], device='cuda:0'), torch.tensor( [1.0], device='cuda:0'))

#a = torch.tensor([4,4,4])
#print(model)
#print(model([1, 2, 3]))
#torch.load("./runs/22-03-29_06-59-09-455859_PPO/checkpoints/3000_policy.pt")
