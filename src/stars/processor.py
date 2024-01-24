# Imported all modules


checkpoints = {
  "classical" : active Q,
  "quantum" : passive Q
}

unit changes = []

def block(checkpoint, dataloader, splitter, merger):
  active, passive = checkpoint
  last state, hidden state = dataloader(active, passive)
  runtime = active(last_state, hidden_state)
  timerun = passive(hidden_state, last_state)
  schedule = splitter(runtime, timerun)
  callback = merger(timerun, runtime)
  return callback

[see the principle @ principle]
