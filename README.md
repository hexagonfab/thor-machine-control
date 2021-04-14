# thor-machine-control

## Table of contents
* [General information](#general-information)

## General information
This repo contains all of the firmware needed to operate the Thor CNC prototype. The build uses closed-loop stepper drivers from the Dutch-based company uStepper. In particular, the uStepper S contains a TMC5130 motor driver, rotary encoder, and ATmega328PB microcontroller. Instructions for flashing the board with firmware via the Arduino IDE may be found at the [uStepper S Github page](https://github.com/uStepper/uStepperS).

Each uStepper S is controlled with the closed-loop pins on a BigTreeTech SKR V1.4 Turbo motion control board. The firmware running on the board is a slightly customized version of Marlin ([Marlin-bugfix-v2.0.x](https://marlinfw.org/meta/download/)).
