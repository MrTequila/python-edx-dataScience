import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
df = pd.read_html("http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2",
                  header = 1)

#header = ["RK", "PLAYER", "TEAM", "GP", "G", "A", "PTS", "+/-", "PIM", "PTS/G", "SOG", "PCT", "GWG", "PP/G", "PP/A", "SH/G", "SH/A"])  

#print (df)

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#



# TODO: Get rid of any row that has at least 4 NANs in it
#
df = df[0].dropna(axis=0, thresh=4)
#print df


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
df = df[df.RK != "RK"]

#print df
# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(labels=["RK"], axis=1)

#print df
# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
df = df.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
for i, col in enumerate(df):
    if i>1:
        print i, df[col].dtypes
        df[col]=pd.to_numeric(df[col], errors="coerce")
        
print df.dtypes

print df.describe()

print df.PCT.unique()
print len(df.PCT.unique())

print df.GP[15]+df.GP[16]
# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

