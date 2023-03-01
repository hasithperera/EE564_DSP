# Home Work 4.

## Q1 - ADC (Theoretical version)

- Assuming a 6bit ADC
 - What is the increase in variance due to quantization of a Gaussian signal where the input RMS level is set to 2 bits/5bits?
 - Make a plot across the range from ‘0.25 – 6 bits’.
 - What is the optimal input RMS to minimize noise increase due to quantization for a gaussian noise source with the 6bit ADC?  For this you can use the equations from class and from the book, assuming the quantization error is uncorrelated with the input.  How is this different from a single tone (sine wave input) input optimal signal level?

## Q2.- ADC (Computer Simulation verification)

- Using your favorite programming language or Simulink, simulate the effects of sampling.  
 - Quantize the signal at both 6bits and 8 bits (and explain your exact quantization choices).
 - Feed in Gaussian noise as your signal.
 - Use input signal RMS levels of 2bits, 4bits, and 6bits.  
 - What is the ratio of input to output RMS power for each case?    
 - Make plots of input and output timestream.  
 - Histogram the input and  output.  
 - How often does the ADC ‘saturate’ in each case (percentage of time at the highest/lowest level).   
 - What percentage of those are ‘correct’ samples, and what percentage should have been at a higher quantization?  
 - Again, plot <x^>/<xx^> from 0.25 to 6bit input RMS.  

## Q3: Filter design activity
- Use the provided files and run the basic simulation
	- Build the logic looking at the impulse response.

- file: [final simulink file](HW4_direct.slx.r2020b)
