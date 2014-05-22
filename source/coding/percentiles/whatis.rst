What is 95th Percentile?
========================

    The 95th percentile value of a set is the smallest value in that set which
    is larger than 95% of the other values in the set.

Putting this in less formal terminology, you spend 5% of your time above the
95th percentile bandwidth, and 95% of your time below it.

There are two common uses of this statistic. Firstly it can be used as a trend
analysis tool (a rolling calcualtion of the 95% percentile will be a fairly
straight line, making projection of future usage possible). Secondly, it is
quite often used by ISPs to calculate resource usage for customers allowed to
burst to high bandwidths for short periods of time.

When used as a resource limit for bursting you are basically saying "You may
use as much bandwidth as you want for approx 36 hours per month, and you will
be charged for the remaining hours of the month."

This script has been released under the GPL for use in trend analysis. Usage
for billing purposes is not recommended by the Author.

Current Implementation
----------------------

My cricket-95.pl script calculates the 95th percentile in the following way:

1. Retrieve all values for the first 2 datasources in the RRD for the past
calendar month

2 Place all numeric values into 2 lists (one for each datasource)

3 Sort the lists in ascending numerical order

4 Find index of 95th percentile using the calculation:

  n = int((elements*0.05)+0.5);

  The nth value in each sorted list is the 95th percentile value of that list

5 Report the larger of the two 95th percentile values

Alternative calculations
------------------------

Treatment of Unknown / NaN values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This implementation ignores Unknown/NaN values in the set. Doing this gives a
line that is a pretty good approximation to the 95th percentile very quickly
after a new data-source is added.

A second option is to treat Unknown/NaN values as zero. With this method it
takes longer for the 95th percentile line to stabilize, but in the case of a
failure in data collection, it works more in the customer's favour, so is less
likely to cause bills to be contested.

A third option is a hybrid of the 2... Ignore any unknown values at the front
of the set, but count any that occur after the first numeric value in the set
as zero. This allows the 95th percentile to converge rapidly in new graphs, and
gives a more accurate result in the case of missed values.

Choice of index value
^^^^^^^^^^^^^^^^^^^^^

My implementation rounds the index to the nearest integer value to chose the
95th percentile index.

One possible alternative is to calculate an average of the two surrounding
values when elements*0.05 is not an integer.

e.g.

x = (S(floor(elements*0.05)) + S(ceil(elements*0.05)))/2

Another alternative would be to use a weighted average

e.g.

x = S(floor(elements*0.05))*frac(elements*0.05) + S(ceil(elements*0.05)) * (1 - frac(elements*0.05))

As the values surrounting the nth element are usually pretty similar, these
don't give much benefit in my experience.
