import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#

servo = pd.read_csv("Datasets/servo.data", names=['motor', 'screw', 'pgain', 'vgain', 'class'])

print (servo.count())

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
slice1 = servo[servo.vgain == 5]
print (slice1.count())#servo.loc[servo.vgain == 5,:])

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#

slice2 = servo[(servo.motor == "E") & (servo.screw == "E")]

print (slice2.count())

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#

slice3 = servo[servo.pgain == 4]

print (slice3.count(), slice3.vgain.mean())

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!

print servo.dtypes

