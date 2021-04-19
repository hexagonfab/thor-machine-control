# thor-machine-control

## Table of contents
* [General information](#general-information)

## General information
This repo contains all of the firmware needed to operate the Thor CNC prototype. The build uses closed-loop stepper drivers from the Dutch-based company uStepper. In particular, the uStepper S contains a TMC5130 motor driver, rotary encoder, and ATmega328PB microcontroller. Instructions for flashing the board with firmware via the Arduino IDE may be found at the [uStepper S Github page](https://github.com/uStepper/uStepperS).

Each uStepper S is controlled with the closed-loop pins on a BigTreeTech SKR V1.4 Turbo motion control board. The firmware running on the board is a slightly customized version of Marlin ([Marlin-bugfix-v2.0.x](https://marlinfw.org/meta/download/)).

Calculating the movement settings, specifically the axis steps/mm, can be done using the online calculator from [RepRap](https://blog.prusaprinters.org/calculator_3416/). The information needed will be step angle, driver microstepping, belt pitch and presets, and pulley tooth count, all of which are determined by the part selection:
* Step angle - 1.8deg
* Microstepping - 1/16
* Belt - GT2 with 2mm pitch
* Tooth count - 30
The two stepper motors are [1702HS133A Nema17 steppers](https://ooznest.co.uk/product/nema17-stepper-motors/) with 1.33A rated (max) current and 1.8 degree step angle. The belt is a 6mm wide [GT2 timing belt with 2mm pitch](https://ooznest.co.uk/product/2gt-gates-open-timing-belt-per-metre/). Attached to each motor spindle is a [30-tooth GT2 pully](https://ooznest.co.uk/product/2gt-pulleys/). Based on these part specs, the Thor CNC has a theoretical resolution of 18.75um.
