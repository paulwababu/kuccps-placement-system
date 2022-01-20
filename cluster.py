from math import sqrt
from xxlimited import Str

"""
To calculate kcse cluster points, we use the formular below

C = √(X/48 * Y/84) * 48

where, C = Cluster Points
       X = points obtained in the four main subjects required in the course you want to do,
       eg computer science
       Y = total points of the seven subjects
       
       ***EXAMPLE**
       1. Nursing Course Cluster Calculation
        - Nursing course needs Biology, Chemistry, Maths and English as Compulsory subjects
          The subjects above when converted to points , eg A for 12, adds up to X in the equation above
          Lets say you got: Biology C+(7) History C+(7) Maths B-(8) English B+(10)  
          Your total X will be 32
        - For the other subjects, lets say you score:
          Kiswahili A(12) Business C(5) History D(2)
          Your total for Y will be 19

        * Keep in mind KNEX dictates that a candiate can sit for a minimum of 7 subjects to
          a maximum of 9 subjects
          
        * We now have everything we need to calculate the cluster point for the nursing student

        * The code below is a function that will implement the cluster calculation based on the number of subjects done
          (in the case above it should bring 30.5380)

        * Before getting into how the function works, lets start by understaing how our whole app will work
          The web application is a mordern kuccps placement portal which addresses the issue of calculating 
          cluster points to determine what courses you can do and also the issue of people placing to courses
          they cannot do. 
          It starts by asking the user to sign up and put thier results and name
          Once logged in, they can apply for a course and view all avaliable courses and universities
           and there is a button showing them whether or not they can apply for the courses shown
          Once they click a course, they can see their results and cluster calculate for that unit
          Once they apply for that course, the system blocks them from appyling again
          If the course has been fully applied, they do not take any more people!!
        
        * The function will have arguements for a total of 9 subjects, however, when it comes to cluster,
          some of the subjects wont be taken into account
          This means that our funtion will take both optional arguements as subjects, as only 7 are required
          and for the 7 will be mandatory arguements. 
          Having the above,the function applies the formula above and returns the cluster points
          Having the cluster points, we can now make a new function that shows you whether you qualify
          for a course or not by comparing the cutoff points for the courses with all universities
"""

##implement the formular for cluster point above, c

#map grade, g, to points. eg A for 12 points, this is the raw cluster
#g = {'A':12, 'A-':11, 'B+':10, 'B':9, 'B-':8, 'C+':7, 'C':6, 'C-':5, 'D+':4, 'D':3, 'D-':2, 'E':1}
#X for four main subjects in our case and Y
#X = {'biology', 'chemistry', 'mathematics', 'english'}
#Y = {'kiswahili', 'business', 'history'}

#list all subjects by groups
"""
#group1
english = {}
kiswahili = {}
maths = {}

#group2
biology = {}
chemistry = {}
physics = {}
generalscience = {}

#group 3
cre = {}
geography = {}
hre = {}
history = {}
ire = {}

#group4
agriculture = {}
art = {}
aviation = {}
building = {}
computer = {}
drawing = {}
electricity = {}
homescience = {}
metalwork = {}
power = {}
woodwork = {}

#group5
arabic = {}
business = {}
french = {}
german = {}
sign = {}
music = {}

#ask user for subjects taken
#for this example,we assume the cluster we are searching for is 4 a nursing course 
biology = input('Enter Biology grade: ')
chemistry = input('Enter Chemistry grade: ')
maths = input('Enter Mathematics grade: ')
english = input('Enter English grade: ')
kiswahili = input('Enter kiswahili grade: ')
business = input('Enter business grade: ')
history = input('Enter history grade: ')

#map function of grade to points instead of suing if else statements
g = {'A':12, 'A-':11, 'B+':10, 'B':9, 'B-':8, 'C+':7, 'C':6, 'C-':5, 'D+':4, 'D':3, 'D-':2, 'E':1}
biology = g[biology]
chemistry = g[chemistry]
maths = g[maths]
english = g[english]
kiswahili = g[kiswahili]
business = g[business]
history = g[history]

#this is the total grades of the four main subjects, X
raw_cluster = (biology+chemistry+maths+english)
aggregate_cluster = (biology+chemistry+maths+english+kiswahili+business+history)
rcp = raw_cluster / 48 #raw_cluster is X
acp = aggregate_cluster / 84 #aggregate cluster is Y
wcp = sqrt(rcp * acp) * 48 #wcp is the cluster points
print(wcp)"""

"""
- Now that the system is working for people who do nursing only,
we head over to the next part, asking for all units done
Then the code goes through all courses and calculates the cluster
according to the major four units, X, to show you all courses you can do 
in their consecutive universities
We need a csv for subjects required for all courses across all Universities
We need cluster calculating function according to units done
"""

import pandas as pd

course_guide = pd.read_csv("course_guide.csv")
#print(course_guide.head())

cut_off_15 = course_guide['2015_cut_off'].dropna()
