Boids -- Simulating animal flocking behaivour
==================================================

Authors
--------
Code: James Heatherington
Packaging: Sofia Qvarfort


Description
---------------------
This program simulates a number of so-called 'boids' which demonstrate flocking behaviour.


Usage
---------------------
boids takes two compulsory arguments: boid_no (int) and config.yaml (config yaml file). The config file contains input parameters, such as the spread of starting positions and starting velocities.

-ex will prompt the program to print an example config file to the console. This can be copied and altered by the user into a new config file. 


Examples
----------------------
Standard use:

    >> boids 10 config.yaml


Generating an example config file:

    >> boids 10 random_name.yaml -ex

Note that if no current config file exists, the input name is irrelevant.



Copyright and Licence
-----------------------
For licence and copyright, see LICENCE.md
