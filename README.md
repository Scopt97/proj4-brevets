# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax.

Credits to Michal Young.

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must
arrive at the location.

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html .  Additional background information
is in https://rusa.org/pages/rulesForRiders . The description is ambiguous,
but the examples help.  Part of finishing this project is clarifying
anything that is not clear about the requirements, and documenting it
clearly.

We are essentially replacing the calculator at
https://rusa.org/octime_acp.html .  We can also use that calculator
to clarify requirements and develop test data.

## AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes
an HTML form and emits a text page. The reimplementation will fill in
times as the input fields are filled.  Each time a distance is filled
in, the corresponding open and close times should be filled in.

I will leave much of the design to you. You'll turn the implementation that you
do. See below for more information.

## Use

In a command line, cd to the brevets directory , build the docker file, and run it

### Author: Kyle Nielsen  Contact: kylen@uoregon.edu
