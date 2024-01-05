# This module is intended to include a definition of analog wave signals and provide a structure that procedurally constructs the waveforms.

===Hardware
Analog hardware will have to allow digital means of recording the physical observables. We will use the analog device as computation substrate whenever we need to construct a waveform and in the digital media we will specify the logic through which the sampling event is going to be defined.

===Software
Programming an interface will require the following:
1. Selecting directionality and channels,
2. Streaming data through output ports of selected channels,
3. Sampling and recording channel states with specified frequency.

We can have two parallel processes handling all outflow (digital to analog) and inflow (analog to digital) states.
