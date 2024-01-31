"""[basic format]

[inverted high] image ..
[inverted low] description ..
[controlled low] object ..
[controlled high] method ..
"""


block = {
    "-1" : "+1",
    "-0" : "+0",
    "+0" : "-0",
    "+1" : "-1"
}

>>> step = next(sequencer)
... [+1]
    [+0]
    [-0]
    [-1]

>>> step = next(sequencer)
... [+1]
    [+0]
    [-1]
    [-0]

>>> step = next(sequencer)
... [+1]
    [-1]
    [+0]
    [-0]

>>> step = next(sequencer)
... [-1]
    [+1]
    [+0]
    [-0]


[see dynamic object @ dynamic.py]
