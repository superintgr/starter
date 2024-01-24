initial state = None
final state = None
hidden state = None
evolution = []

class Computation: pass
class Construction: pass
class Measurement: pass
class Preparation: pass

tasks = {
  start : (computation, contruction)
  end : (measurement, prepration)
  switch : ('step', 'integrate')
  callback : (filer,)
}

schedules = {
  (start, not(start)) : (not(end), end),
  (filer, switch) : (switch, filer),
  (not(start), end)) : (start, not(end)),
}


[see processor @ processor.py]
