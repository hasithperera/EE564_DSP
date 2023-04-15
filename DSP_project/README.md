## Documentation - Project


## Getting data from ethernet

- This was first tested as a part of HW5
- Need to match the mac of the capturing computer. If not even though wireshark can see it python was not able to pick it up
- Incomming data is saved in to a binary file.
- Converted values gave the same variation but the start time was not correct. This is fine since I grabbed some random bit of data.
- The  bit stream was stopping after some interval. It shouldn't do that. (Pending need to check)


## Things to do

- [ ] Send data with python and store a 128 X 128 image.
- [ ] Add serial read write for commanding
- [ ] Process the image. (basic, eg: add a constant and send it back)
	- This will verify that I every thing working other than the final image processing 
	- [ ] Python implementation for the algorithm (IIR filter)



