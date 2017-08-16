import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os
from sklearn.decomposition import PCA, RandomizedPCA
from sklearn import manifold

# Look pretty...
matplotlib.style.use('ggplot')

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
samples = []
colors = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
for filename in os.listdir("Datasets/ALOI/32"):
    img = misc.imread("Datasets/ALOI/32/"+filename)
    img = img.reshape(-1)
    colors.append('b')
    samples.append(img)


# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
for filename in os.listdir("Datasets/ALOI/32i"):
    img = misc.imread("Datasets/ALOI/32i/"+filename)
    img = img.reshape(-1)
    colors.append('r')
    samples.append(img)


#
# TODO: Convert the list to a dataframe
#

df = pd.DataFrame.from_records(samples)



#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
Ti = iso.transform(df)
print(Ti[:,0])


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# Render the Original Armadillo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Bear 2D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(Ti[:,0],Ti[:,1], Ti[:,2], c=colors, marker='.', alpha=0.75)




#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()


