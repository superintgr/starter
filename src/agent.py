
# controllable model is restored with profile designated by auth and supplied voltage parameters from last participating state
agent = restore_state(auth, last_hidden_state)
# setup inferface with agent and other objects
substrate = Medium(agent, substrate)
# Release the channels
channels = substrate.get_channels()
# 
