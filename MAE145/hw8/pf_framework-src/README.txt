
The folder data contains the sensor (odometry/range/bearing) and
landmark information for a planar environment. This data is read as a
list of lists via some functions given to you in the folder. 

The folder python contains all of the functions that you need in order
to implement the particle filter. You have to fill out the ones that
have a TODO in them.

For this problem, it is advised that you implement the more advanced
sample with replacement method in the filter, which is the one for
which particle deprivation is the smallest. The other methods also
work for the first few iterations. Alternatively, you would have to
increase the number of your particles every now and then.

Note that a particle filter may diverge if all of the weights become
close to zero. To avoid this, you can make the noise larger in the
measurement model. 

The folder plots will store all of the snapshots of the particle
filter implementation.  Open them in sequence to see how the robot
moves. The motion of the robot should be "wander" around the landmarks
among the plot limits. However, due to randomness of the method, you
will obtain several and very different trajectories for your robot
from different runs.

librobotics is just a library that is used for several purposes, you
don't need to use all of the functions in there for the algorithm to
run, but just make it available from where you run the main py files.



