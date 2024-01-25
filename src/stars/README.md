```BASIC
100 'CONVOLUTION USING THE INPUT SIDE ALGORITHM
110
120 DIM X[80] 'The input signal, 81 points
130 DIM H[30] 'The impulse response, 31 points
140 DIM Y[110] 'The output signal, 111 points
150
160 GOSUB XXXX 'Mythical subroutine to load X[ ] and H[ ] '
170
180 FOR I% = 0 TO 110 'Zero the output array
190     Y(I%) = 0
200 NEXT I%
210
220 FOR I% = 0 TO 80 'Loop for each point in X[ ]
230     FOR J% = 0 TO 30 'Loop for each point in H[ ]
240         Y[I% + J%] = Y[I% + J%] + X[I%] * H[I%]
250     NEXT J%
260 NEXT I%
270 
280 GOSUB XXXX 'Mythical subroutine to store Y[ ]
290
300 END
```
