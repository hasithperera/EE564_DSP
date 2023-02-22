# Day1-2: Basic Tips and tricks

- *Current setup: Linux mint 20.04 + Matlab 2021a + Vivado 2022.1*
- when running Vivado/Model Composer set sources. I have an alias to do this setup.
- Do not install matlab compiles module it doesn't work well 

# Day 3

## Simulink basics (01/18)

- System Generator block needs to match your board
	- Compilation: **HDL Netlist** (this option will show you editable vhdl code. If you select **IP Catalog** internal operation will be hidden
  - Target Directory: on windows long file path may lead to error. set to some thing short eg. `c:/Xilinx/`
  - Clocking tab: set to 5 ns
- To show data type on connections: Right click > other Displays > Signals and Ports > Port Units
- Obs: my setup gave weird data types starting fresh fixed it
- I/O: **Gateway In** and **Gateway out** (yellow blocks). Don't add any nonXilinx blocks here since it will not compile well and ultimately it will not be implemented in the fpga.
- After you generate using the system generator block it will make a vivado project

## Vivado Project

- I had a bug where I couldn't open 
- Need a top.vhdl file to handle the differential clock signals.
	- When adding this linking the file without copying is the best option since is you copy every time you regenerate using Simulink all the project becomes unusable
  - Set the module as top.
  -  
