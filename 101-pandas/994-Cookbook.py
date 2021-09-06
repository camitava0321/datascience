# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
"""
"""
pandas Cookbook
"""
# The usual preamble
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)


# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)
Let's continue with our NYC 311 service requests example.

complaints = pd.read_csv('../data/311-service-requests.csv')
3.1 Selecting only noise complaints
I'd like to know which borough has the most noise complaints. First, we'll take a look at the data to see what it looks like:

complaints[:5]
Unique Key	Created Date	Closed Date	Agency	Agency Name	Complaint Type	Descriptor	Location Type	Incident Zip	Incident Address	Street Name	Cross Street 1	Cross Street 2	Intersection Street 1	Intersection Street 2	Address Type	City	Landmark	Facility Type	Status	Due Date	Resolution Action Updated Date	Community Board	Borough	X Coordinate (State Plane)	Y Coordinate (State Plane)	Park Facility Name	Park Borough	School Name	School Number	School Region	School Code	School Phone Number	School Address	School City	School State	School Zip	School Not Found	School or Citywide Complaint	Vehicle Type	Taxi Company Borough	Taxi Pick Up Location	Bridge Highway Name	Bridge Highway Direction	Road Ramp	Bridge Highway Segment	Garage Lot Name	Ferry Direction	Ferry Terminal Name	Latitude	Longitude	Location
0	26589651	10/31/2013 02:08:41 AM	NaN	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	11432	90-03 169 STREET	169 STREET	90 AVENUE	91 AVENUE	NaN	NaN	ADDRESS	JAMAICA	NaN	Precinct	Assigned	10/31/2013 10:08:41 AM	10/31/2013 02:35:17 AM	12 QUEENS	QUEENS	1042027	197389	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.708275	-73.791604	(40.70827532593202, -73.79160395779721)
1	26593698	10/31/2013 02:01:04 AM	NaN	NYPD	New York City Police Department	Illegal Parking	Commercial Overnight Parking	Street/Sidewalk	11378	58 AVENUE	58 AVENUE	58 PLACE	59 STREET	NaN	NaN	BLOCKFACE	MASPETH	NaN	Precinct	Open	10/31/2013 10:01:04 AM	NaN	05 QUEENS	QUEENS	1009349	201984	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.721041	-73.909453	(40.721040535628305, -73.90945306791765)
2	26594139	10/31/2013 02:00:24 AM	10/31/2013 02:40:32 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10032	4060 BROADWAY	BROADWAY	WEST 171 STREET	WEST 172 STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 10:00:24 AM	10/31/2013 02:39:42 AM	12 MANHATTAN	MANHATTAN	1001088	246531	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.843330	-73.939144	(40.84332975466513, -73.93914371913482)
3	26595721	10/31/2013 01:56:23 AM	10/31/2013 02:21:48 AM	NYPD	New York City Police Department	Noise - Vehicle	Car/Truck Horn	Street/Sidewalk	10023	WEST 72 STREET	WEST 72 STREET	COLUMBUS AVENUE	AMSTERDAM AVENUE	NaN	NaN	BLOCKFACE	NEW YORK	NaN	Precinct	Closed	10/31/2013 09:56:23 AM	10/31/2013 02:21:10 AM	07 MANHATTAN	MANHATTAN	989730	222727	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.778009	-73.980213	(40.7780087446372, -73.98021349023975)
4	26590930	10/31/2013 01:53:44 AM	NaN	DOHMH	Department of Health and Mental Hygiene	Rodent	Condition Attracting Rodents	Vacant Lot	10027	WEST 124 STREET	WEST 124 STREET	LENOX AVENUE	ADAM CLAYTON POWELL JR BOULEVARD	NaN	NaN	BLOCKFACE	NEW YORK	NaN	NaN	Pending	11/30/2013 01:53:44 AM	10/31/2013 01:59:54 AM	10 MANHATTAN	MANHATTAN	998815	233545	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.807691	-73.947387	(40.80769092704951, -73.94738703491433)
5 rows × 52 columns

To get the noise complaints, we need to find the rows where the "Complaint Type" column is "Noise - Street/Sidewalk". I'll show you how to do that, and then explain what's going on.

noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]
noise_complaints[:3]
Unique Key	Created Date	Closed Date	Agency	Agency Name	Complaint Type	Descriptor	Location Type	Incident Zip	Incident Address	Street Name	Cross Street 1	Cross Street 2	Intersection Street 1	Intersection Street 2	Address Type	City	Landmark	Facility Type	Status	Due Date	Resolution Action Updated Date	Community Board	Borough	X Coordinate (State Plane)	Y Coordinate (State Plane)	Park Facility Name	Park Borough	School Name	School Number	School Region	School Code	School Phone Number	School Address	School City	School State	School Zip	School Not Found	School or Citywide Complaint	Vehicle Type	Taxi Company Borough	Taxi Pick Up Location	Bridge Highway Name	Bridge Highway Direction	Road Ramp	Bridge Highway Segment	Garage Lot Name	Ferry Direction	Ferry Terminal Name	Latitude	Longitude	Location
0	26589651	10/31/2013 02:08:41 AM	NaN	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	11432	90-03 169 STREET	169 STREET	90 AVENUE	91 AVENUE	NaN	NaN	ADDRESS	JAMAICA	NaN	Precinct	Assigned	10/31/2013 10:08:41 AM	10/31/2013 02:35:17 AM	12 QUEENS	QUEENS	1042027	197389	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.708275	-73.791604	(40.70827532593202, -73.79160395779721)
16	26594086	10/31/2013 12:54:03 AM	10/31/2013 02:16:39 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Music/Party	Street/Sidewalk	10310	173 CAMPBELL AVENUE	CAMPBELL AVENUE	HENDERSON AVENUE	WINEGAR LANE	NaN	NaN	ADDRESS	STATEN ISLAND	NaN	Precinct	Closed	10/31/2013 08:54:03 AM	10/31/2013 02:07:14 AM	01 STATEN ISLAND	STATEN ISLAND	952013	171076	Unspecified	STATEN ISLAND	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.636182	-74.116150	(40.63618202176914, -74.1161500428337)
25	26591573	10/31/2013 12:35:18 AM	10/31/2013 02:41:35 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	10312	24 PRINCETON LANE	PRINCETON LANE	HAMPTON GREEN	DEAD END	NaN	NaN	ADDRESS	STATEN ISLAND	NaN	Precinct	Closed	10/31/2013 08:35:18 AM	10/31/2013 01:45:17 AM	03 STATEN ISLAND	STATEN ISLAND	929577	140964	Unspecified	STATEN ISLAND	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.553421	-74.196743	(40.55342078716953, -74.19674315017886)
3 rows × 52 columns

If you look at noise_complaints, you'll see that this worked, and it only contains complaints with the right complaint type. But how does this work? Let's deconstruct it into two pieces

complaints['Complaint Type'] == "Noise - Street/Sidewalk"
0      True
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9     False
10    False
11    False
12    False
13    False
14    False
...
111054     True
111055    False
111056    False
111057    False
111058    False
111059     True
111060    False
111061    False
111062    False
111063    False
111064    False
111065    False
111066     True
111067    False
111068    False
Name: Complaint Type, Length: 111069, dtype: bool
This is a big array of Trues and Falses, one for each row in our dataframe. When we index our dataframe with this array, we get just the rows where our boolean array evaluated to True. It's important to note that for row filtering by a boolean array the length of our dataframe's index must be the same length as the boolean array used for filtering.

You can also combine more than one condition with the & operator like this:

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaints['Borough'] == "BROOKLYN"
complaints[is_noise & in_brooklyn][:5]
Unique Key	Created Date	Closed Date	Agency	Agency Name	Complaint Type	Descriptor	Location Type	Incident Zip	Incident Address	Street Name	Cross Street 1	Cross Street 2	Intersection Street 1	Intersection Street 2	Address Type	City	Landmark	Facility Type	Status	Due Date	Resolution Action Updated Date	Community Board	Borough	X Coordinate (State Plane)	Y Coordinate (State Plane)	Park Facility Name	Park Borough	School Name	School Number	School Region	School Code	School Phone Number	School Address	School City	School State	School Zip	School Not Found	School or Citywide Complaint	Vehicle Type	Taxi Company Borough	Taxi Pick Up Location	Bridge Highway Name	Bridge Highway Direction	Road Ramp	Bridge Highway Segment	Garage Lot Name	Ferry Direction	Ferry Terminal Name	Latitude	Longitude	Location
31	26595564	10/31/2013 12:30:36 AM	NaN	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Music/Party	Street/Sidewalk	11236	AVENUE J	AVENUE J	EAST 80 STREET	EAST 81 STREET	NaN	NaN	BLOCKFACE	BROOKLYN	NaN	Precinct	Open	10/31/2013 08:30:36 AM	NaN	18 BROOKLYN	BROOKLYN	1008937	170310	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.634104	-73.911055	(40.634103775951736, -73.91105541883589)
49	26595553	10/31/2013 12:05:10 AM	10/31/2013 02:43:43 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	11225	25 LEFFERTS AVENUE	LEFFERTS AVENUE	WASHINGTON AVENUE	BEDFORD AVENUE	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 08:05:10 AM	10/31/2013 01:29:29 AM	09 BROOKLYN	BROOKLYN	995366	180388	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.661793	-73.959934	(40.6617931276793, -73.95993363978067)
109	26594653	10/30/2013 11:26:32 PM	10/31/2013 12:18:54 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Music/Party	Street/Sidewalk	11222	NaN	NaN	NaN	NaN	DOBBIN STREET	NORMAN STREET	INTERSECTION	BROOKLYN	NaN	Precinct	Closed	10/31/2013 07:26:32 AM	10/31/2013 12:18:54 AM	01 BROOKLYN	BROOKLYN	996925	203271	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.724600	-73.954271	(40.724599563793525, -73.95427134534344)
236	26591992	10/30/2013 10:02:58 PM	10/30/2013 10:23:20 PM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	11218	DITMAS AVENUE	DITMAS AVENUE	NaN	NaN	NaN	NaN	LATLONG	BROOKLYN	NaN	Precinct	Closed	10/31/2013 06:02:58 AM	10/30/2013 10:23:20 PM	01 BROOKLYN	BROOKLYN	991895	171051	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.636169	-73.972455	(40.63616876563881, -73.97245504682485)
370	26594167	10/30/2013 08:38:25 PM	10/30/2013 10:26:28 PM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Music/Party	Street/Sidewalk	11218	126 BEVERLY ROAD	BEVERLY ROAD	CHURCH AVENUE	EAST 2 STREET	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 04:38:25 AM	10/30/2013 10:26:28 PM	12 BROOKLYN	BROOKLYN	990144	173511	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.642922	-73.978762	(40.6429222774404, -73.97876175474585)
5 rows × 52 columns

Or if we just wanted a few columns:

complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10]
Complaint Type	Borough	Created Date	Descriptor
31	Noise - Street/Sidewalk	BROOKLYN	10/31/2013 12:30:36 AM	Loud Music/Party
49	Noise - Street/Sidewalk	BROOKLYN	10/31/2013 12:05:10 AM	Loud Talking
109	Noise - Street/Sidewalk	BROOKLYN	10/30/2013 11:26:32 PM	Loud Music/Party
236	Noise - Street/Sidewalk	BROOKLYN	10/30/2013 10:02:58 PM	Loud Talking
370	Noise - Street/Sidewalk	BROOKLYN	10/30/2013 08:38:25 PM	Loud Music/Party
378	Noise - Street/Sidewalk	BROOKLYN	10/30/2013 08:32:13 PM	Loud Talking
656	Noise - Street/Sidewalk	BROOKLYN	10/30/2013 06:07:39 PM	Loud Music/Party
1251	Noise - Street/Sidewalk	BROOKLYN	10/30/2013 03:04:51 PM	Loud Talking
5416	Noise - Street/Sidewalk	BROOKLYN	10/29/2013 10:07:02 PM	Loud Talking
5584	Noise - Street/Sidewalk	BROOKLYN	10/29/2013 08:15:59 PM	Loud Music/Party
10 rows × 4 columns

3.2 A digression about numpy arrays
On the inside, the type of a column is pd.Series

pd.Series([1,2,3])
0    1
1    2
2    3
dtype: int64
and pandas Series are internally numpy arrays. If you add .values to the end of any Series, you'll get its internal numpy array

np.array([1,2,3])
array([1, 2, 3])
pd.Series([1,2,3]).values
array([1, 2, 3])
So this binary-array-selection business is actually something that works with any numpy array:

arr = np.array([1,2,3])
arr != 2
array([ True, False,  True], dtype=bool)
arr[arr != 2]
array([1, 3])
3.3 So, which borough has the most noise complaints?
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints['Borough'].value_counts()
MANHATTAN        917
BROOKLYN         456
BRONX            292
QUEENS           226
STATEN ISLAND     36
Unspecified        1
dtype: int64
It's Manhattan! But what if we wanted to divide by the total number of complaints, to make it make a bit more sense? That would be easy too:

noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()
noise_complaint_counts / complaint_counts
BRONX            0.014833
BROOKLYN         0.013864
MANHATTAN        0.037755
QUEENS           0.010143
STATEN ISLAND    0.007474
Unspecified      0.000141
dtype: float64
Oops, why was that zero? That's no good. This is because of integer division in Python 2. Let's fix it, by converting complaint_counts into an array of floats.

noise_complaint_counts / complaint_counts.astype(float)
BRONX            0.014833
BROOKLYN         0.013864
MANHATTAN        0.037755
QUEENS           0.010143
STATEN ISLAND    0.007474
Unspecified      0.000141
dtype: float64
(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')
<matplotlib.axes.AxesSubplot at 0x113a628d0>

So Manhattan really does complain more about noise than the other boroughs! Neat.