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

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)
We're going to use a new dataset here, to demonstrate how to deal with larger datasets. This is a subset of the of 311 service requests from NYC Open Data.

complaints = pd.read_csv('../data/311-service-requests.csv')
/opt/anaconda/lib/python2.7/site-packages/pandas/io/parsers.py:1070: DtypeWarning: Columns (8) have mixed types. Specify dtype option on import or set low_memory=False.
  data = self._reader.read(nrows)
Depending on your pandas version, you might see an error like "DtypeWarning: Columns (8) have mixed types". This means that it's encountered a problem reading in our data. In this case it almost certainly means that it has columns where some of the entries are strings and some are integers.

For now we're going to ignore it and hope we don't run into a problem, but in the long run we'd need to investigate this warning.

2.1 What's even in it? (the summary)
When you print a large dataframe, it will only show you the first few rows.

If you don't see this, don't panic! The default behavior for large dataframes changed between pandas 0.12 and 0.13. Previous to 0.13 it would show you a summary of the dataframe. This includes all the columns, and how many non-null values there are in each column.

complaints
Unique Key	Created Date	Closed Date	Agency	Agency Name	Complaint Type	Descriptor	Location Type	Incident Zip	Incident Address	Street Name	Cross Street 1	Cross Street 2	Intersection Street 1	Intersection Street 2	Address Type	City	Landmark	Facility Type	Status	Due Date	Resolution Action Updated Date	Community Board	Borough	X Coordinate (State Plane)	Y Coordinate (State Plane)	Park Facility Name	Park Borough	School Name	School Number	School Region	School Code	School Phone Number	School Address	School City	School State	School Zip	School Not Found	School or Citywide Complaint	Vehicle Type	Taxi Company Borough	Taxi Pick Up Location	Bridge Highway Name	Bridge Highway Direction	Road Ramp	Bridge Highway Segment	Garage Lot Name	Ferry Direction	Ferry Terminal Name	Latitude	Longitude	Location
0	26589651	10/31/2013 02:08:41 AM	NaN	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	11432	90-03 169 STREET	169 STREET	90 AVENUE	91 AVENUE	NaN	NaN	ADDRESS	JAMAICA	NaN	Precinct	Assigned	10/31/2013 10:08:41 AM	10/31/2013 02:35:17 AM	12 QUEENS	QUEENS	1042027	197389	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.708275	-73.791604	(40.70827532593202, -73.79160395779721)
1	26593698	10/31/2013 02:01:04 AM	NaN	NYPD	New York City Police Department	Illegal Parking	Commercial Overnight Parking	Street/Sidewalk	11378	58 AVENUE	58 AVENUE	58 PLACE	59 STREET	NaN	NaN	BLOCKFACE	MASPETH	NaN	Precinct	Open	10/31/2013 10:01:04 AM	NaN	05 QUEENS	QUEENS	1009349	201984	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.721041	-73.909453	(40.721040535628305, -73.90945306791765)
2	26594139	10/31/2013 02:00:24 AM	10/31/2013 02:40:32 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10032	4060 BROADWAY	BROADWAY	WEST 171 STREET	WEST 172 STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 10:00:24 AM	10/31/2013 02:39:42 AM	12 MANHATTAN	MANHATTAN	1001088	246531	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.843330	-73.939144	(40.84332975466513, -73.93914371913482)
3	26595721	10/31/2013 01:56:23 AM	10/31/2013 02:21:48 AM	NYPD	New York City Police Department	Noise - Vehicle	Car/Truck Horn	Street/Sidewalk	10023	WEST 72 STREET	WEST 72 STREET	COLUMBUS AVENUE	AMSTERDAM AVENUE	NaN	NaN	BLOCKFACE	NEW YORK	NaN	Precinct	Closed	10/31/2013 09:56:23 AM	10/31/2013 02:21:10 AM	07 MANHATTAN	MANHATTAN	989730	222727	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.778009	-73.980213	(40.7780087446372, -73.98021349023975)
4	26590930	10/31/2013 01:53:44 AM	NaN	DOHMH	Department of Health and Mental Hygiene	Rodent	Condition Attracting Rodents	Vacant Lot	10027	WEST 124 STREET	WEST 124 STREET	LENOX AVENUE	ADAM CLAYTON POWELL JR BOULEVARD	NaN	NaN	BLOCKFACE	NEW YORK	NaN	NaN	Pending	11/30/2013 01:53:44 AM	10/31/2013 01:59:54 AM	10 MANHATTAN	MANHATTAN	998815	233545	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.807691	-73.947387	(40.80769092704951, -73.94738703491433)
5	26592370	10/31/2013 01:46:52 AM	NaN	NYPD	New York City Police Department	Noise - Commercial	Banging/Pounding	Club/Bar/Restaurant	11372	37 AVENUE	37 AVENUE	84 STREET	85 STREET	NaN	NaN	BLOCKFACE	JACKSON HEIGHTS	NaN	Precinct	Open	10/31/2013 09:46:52 AM	NaN	03 QUEENS	QUEENS	1016948	212540	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.749989	-73.881988	(40.7499893014072, -73.88198770727831)
6	26595682	10/31/2013 01:46:40 AM	NaN	NYPD	New York City Police Department	Blocked Driveway	No Access	Street/Sidewalk	11419	107-50 109 STREET	109 STREET	107 AVENUE	109 AVENUE	NaN	NaN	ADDRESS	SOUTH RICHMOND HILL	NaN	Precinct	Assigned	10/31/2013 09:46:40 AM	10/31/2013 01:59:51 AM	10 QUEENS	QUEENS	1030919	187622	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.681533	-73.831737	(40.68153278675525, -73.83173699701601)
7	26595195	10/31/2013 01:44:19 AM	10/31/2013 01:58:49 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	11417	137-09 CROSSBAY BOULEVARD	CROSSBAY BOULEVARD	PITKIN AVENUE	VAN WICKLEN ROAD	NaN	NaN	ADDRESS	OZONE PARK	NaN	Precinct	Closed	10/31/2013 09:44:19 AM	10/31/2013 01:58:49 AM	10 QUEENS	QUEENS	1027776	184076	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.671816	-73.843092	(40.67181584567338, -73.84309181950769)
8	26590540	10/31/2013 01:44:14 AM	10/31/2013 02:28:04 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Talking	Club/Bar/Restaurant	10011	258 WEST 15 STREET	WEST 15 STREET	7 AVENUE	8 AVENUE	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 09:44:14 AM	10/31/2013 02:00:56 AM	04 MANHATTAN	MANHATTAN	984031	208847	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.739913	-74.000790	(40.73991339303542, -74.00079028612932)
9	26594392	10/31/2013 01:34:41 AM	10/31/2013 02:23:51 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	11225	835 NOSTRAND AVENUE	NOSTRAND AVENUE	UNION STREET	PRESIDENT STREET	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 09:34:41 AM	10/31/2013 01:48:26 AM	09 BROOKLYN	BROOKLYN	997941	182725	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.668204	-73.950648	(40.66820406598287, -73.95064760056546)
10	26595176	10/31/2013 01:25:12 AM	NaN	NYPD	New York City Police Department	Noise - House of Worship	Loud Music/Party	House of Worship	11218	3775 18 AVENUE	18 AVENUE	EAST 9 STREET	EAST 8 STREET	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Open	10/31/2013 09:25:12 AM	NaN	14 BROOKLYN	BROOKLYN	992726	170399	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.634378	-73.969462	(40.63437840816299, -73.96946177104543)
11	26591982	10/31/2013 01:24:14 AM	10/31/2013 01:54:39 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10003	187 2 AVENUE	2 AVENUE	EAST 11 STREET	EAST 12 STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 09:24:14 AM	10/31/2013 01:54:39 AM	03 MANHATTAN	MANHATTAN	988110	205533	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.730816	-73.986073	(40.73081644089586, -73.98607265739876)
12	26594169	10/31/2013 01:20:57 AM	10/31/2013 02:12:31 AM	NYPD	New York City Police Department	Illegal Parking	Double Parked Blocking Vehicle	Street/Sidewalk	10029	65 EAST 99 STREET	EAST 99 STREET	MADISON AVENUE	PARK AVENUE	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 09:20:57 AM	10/31/2013 01:42:05 AM	11 MANHATTAN	MANHATTAN	997470	226725	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.788974	-73.952259	(40.78897400211689, -73.95225898702977)
13	26594391	10/31/2013 01:20:13 AM	NaN	NYPD	New York City Police Department	Noise - Vehicle	Engine Idling	Street/Sidewalk	10466	NaN	NaN	NaN	NaN	STRANG AVENUE	AMUNDSON AVENUE	INTERSECTION	BRONX	NaN	Precinct	Open	10/31/2013 09:20:13 AM	NaN	12 BRONX	BRONX	1029467	264124	Unspecified	BRONX	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.891517	-73.836457	(40.89151738488846, -73.83645714593568)
14	26590917	10/31/2013 01:19:54 AM	NaN	DOHMH	Department of Health and Mental Hygiene	Rodent	Rat Sighting	1-2 Family Mixed Use Building	11219	63 STREET	63 STREET	13 AVENUE	14 AVENUE	NaN	NaN	BLOCKFACE	BROOKLYN	NaN	NaN	Pending	11/30/2013 01:19:54 AM	10/31/2013 01:29:26 AM	10 BROOKLYN	BROOKLYN	984467	167519	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.626477	-73.999218	(40.6264774690411, -73.99921826202639)
15	26591458	10/31/2013 01:14:02 AM	10/31/2013 01:30:34 AM	NYPD	New York City Police Department	Noise - House of Worship	Loud Music/Party	House of Worship	10025	NaN	NaN	NaN	NaN	WEST 99 STREET	BROADWAY	INTERSECTION	NEW YORK	NaN	Precinct	Closed	10/31/2013 09:14:02 AM	10/31/2013 01:30:34 AM	07 MANHATTAN	MANHATTAN	992454	229500	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.796597	-73.970370	(40.7965967075252, -73.97036973473399)
16	26594086	10/31/2013 12:54:03 AM	10/31/2013 02:16:39 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Music/Party	Street/Sidewalk	10310	173 CAMPBELL AVENUE	CAMPBELL AVENUE	HENDERSON AVENUE	WINEGAR LANE	NaN	NaN	ADDRESS	STATEN ISLAND	NaN	Precinct	Closed	10/31/2013 08:54:03 AM	10/31/2013 02:07:14 AM	01 STATEN ISLAND	STATEN ISLAND	952013	171076	Unspecified	STATEN ISLAND	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.636182	-74.116150	(40.63618202176914, -74.1161500428337)
17	26595117	10/31/2013 12:52:46 AM	NaN	NYPD	New York City Police Department	Illegal Parking	Posted Parking Sign Violation	Street/Sidewalk	11236	NaN	NaN	NaN	NaN	ROCKAWAY PARKWAY	SKIDMORE AVENUE	INTERSECTION	BROOKLYN	NaN	Precinct	Open	10/31/2013 08:52:46 AM	NaN	18 BROOKLYN	BROOKLYN	1015289	169710	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.632437	-73.888173	(40.63243692394328, -73.88817263437012)
18	26590389	10/31/2013 12:51:00 AM	NaN	DOT	Department of Transportation	Street Light Condition	Street Light Out	NaN	NaN	226 42 ST E	42 ST E	CHURCH AVE	SNYDER AVE	NaN	NaN	ADDRESS	NaN	NaN	NaN	Open	NaN	NaN	Unspecified BROOKLYN	BROOKLYN	NaN	NaN	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
19	26594210	10/31/2013 12:46:27 AM	NaN	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10033	NaN	NaN	NaN	NaN	WEST 184 STREET	BROADWAY	INTERSECTION	NEW YORK	NaN	Precinct	Assigned	10/31/2013 08:46:27 AM	10/31/2013 01:32:41 AM	12 MANHATTAN	MANHATTAN	1002294	249712	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.852058	-73.934776	(40.85205827756883, -73.93477640780834)
20	26592932	10/31/2013 12:43:47 AM	10/31/2013 12:56:20 AM	NYPD	New York City Police Department	Noise - House of Worship	Loud Music/Party	House of Worship	11216	778 PARK PLACE	PARK PLACE	ROGERS AVENUE	NOSTRAND AVENUE	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 08:43:47 AM	10/31/2013 12:56:20 AM	08 BROOKLYN	BROOKLYN	997608	184656	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.673505	-73.951844	(40.67350473678714, -73.95184414979961)
21	26594152	10/31/2013 12:41:17 AM	10/31/2013 01:04:37 AM	NYPD	New York City Police Department	Noise - Commercial	Banging/Pounding	Store/Commercial	10016	155 E 34TH ST	E 34TH ST	NaN	NaN	NaN	NaN	LATLONG	NEW YORK	NaN	Precinct	Closed	10/31/2013 08:41:17 AM	10/31/2013 01:04:38 AM	06 MANHATTAN	MANHATTAN	990133	211136	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.746194	-73.978769	(40.74619417253121, -73.97876853124392)
22	26589678	10/31/2013 12:39:55 AM	NaN	NYPD	New York City Police Department	Noise - Vehicle	Car/Truck Music	Street/Sidewalk	11419	NaN	NaN	NaN	NaN	112 STREET	ATLANTIC AVENUE	INTERSECTION	SOUTH RICHMOND HILL	NaN	Precinct	Open	10/31/2013 08:39:55 AM	NaN	09 QUEENS	QUEENS	1030314	191578	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.692394	-73.833891	(40.69239424979043, -73.8338912453996)
23	26592304	10/31/2013 12:38:00 AM	NaN	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	11216	371 TOMPKINS AVENUE	TOMPKINS AVENUE	MADISON STREET	PUTNAM AVENUE	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Assigned	10/31/2013 08:38:00 AM	10/31/2013 01:16:53 AM	03 BROOKLYN	BROOKLYN	999720	188825	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.684944	-73.944221	(40.6849442562592, -73.94422078036632)
24	26591892	10/31/2013 12:37:16 AM	NaN	NYPD	New York City Police Department	Blocked Driveway	Partial Access	Street/Sidewalk	10305	1496 BAY STREET	BAY STREET	LYMAN AVENUE	SCHOOL ROAD	NaN	NaN	ADDRESS	STATEN ISLAND	NaN	Precinct	Assigned	10/31/2013 08:37:16 AM	10/31/2013 12:52:10 AM	01 STATEN ISLAND	STATEN ISLAND	967283	160518	Unspecified	STATEN ISLAND	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.607245	-74.061106	(40.60724493456944, -74.06110566015863)
25	26591573	10/31/2013 12:35:18 AM	10/31/2013 02:41:35 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	10312	24 PRINCETON LANE	PRINCETON LANE	HAMPTON GREEN	DEAD END	NaN	NaN	ADDRESS	STATEN ISLAND	NaN	Precinct	Closed	10/31/2013 08:35:18 AM	10/31/2013 01:45:17 AM	03 STATEN ISLAND	STATEN ISLAND	929577	140964	Unspecified	STATEN ISLAND	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.553421	-74.196743	(40.55342078716953, -74.19674315017886)
26	26590509	10/31/2013 12:33:00 AM	NaN	DOT	Department of Transportation	Street Light Condition	Street Light Out	NaN	NaN	38 ST E	38 ST E	CHURCH AVE	LINDEN BLVD	NaN	NaN	BLOCKFACE	NaN	NaN	NaN	Open	NaN	NaN	Unspecified BROOKLYN	BROOKLYN	NaN	NaN	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
27	26591379	10/31/2013 12:32:44 AM	NaN	DOHMH	Department of Health and Mental Hygiene	Harboring Bees/Wasps	Bees/Wasps - Not a beekeper	3+ Family Mixed Use Building	10025	501 WEST 110 STREET	WEST 110 STREET	AMSTERDAM AVENUE	BROADWAY	NaN	NaN	ADDRESS	NEW YORK	NaN	NaN	Open	11/30/2013 12:32:44 AM	NaN	09 MANHATTAN	MANHATTAN	994143	231888	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.803149	-73.964266	(40.80314938553783, -73.96426608076082)
28	26594085	10/31/2013 12:32:08 AM	NaN	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	10026	121 WEST 116 STREET	WEST 116 STREET	LENOX AVENUE	7 AVENUE	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Assigned	10/31/2013 08:32:08 AM	10/31/2013 02:00:57 AM	10 MANHATTAN	MANHATTAN	997947	231613	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.802390	-73.950526	(40.80238950799943, -73.95052644123253)
29	26589201	10/31/2013 12:32:00 AM	NaN	DOT	Department of Transportation	Street Light Condition	Street Light Out	NaN	10309	295 BAYVIEW AVENUE	BAYVIEW AVENUE	VAIL AVENUE	BAYVIEW LANE	NaN	NaN	ADDRESS	STATEN ISLAND	NaN	NaN	Open	NaN	NaN	03 STATEN ISLAND	STATEN ISLAND	927687	127837	Unspecified	STATEN ISLAND	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.517378	-74.203435	(40.517377871705676, -74.20343466779575)
30	26591641	10/31/2013 12:31:17 AM	10/31/2013 02:41:36 AM	NYPD	New York City Police Department	Blocked Driveway	No Access	Street/Sidewalk	10312	24 PRINCETON LANE	PRINCETON LANE	HAMPTON GREEN	DEAD END	NaN	NaN	ADDRESS	STATEN ISLAND	NaN	Precinct	Closed	10/31/2013 08:31:17 AM	10/31/2013 01:43:09 AM	03 STATEN ISLAND	STATEN ISLAND	929577	140964	Unspecified	STATEN ISLAND	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.553421	-74.196743	(40.55342078716953, -74.19674315017886)
31	26595564	10/31/2013 12:30:36 AM	NaN	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Music/Party	Street/Sidewalk	11236	AVENUE J	AVENUE J	EAST 80 STREET	EAST 81 STREET	NaN	NaN	BLOCKFACE	BROOKLYN	NaN	Precinct	Open	10/31/2013 08:30:36 AM	NaN	18 BROOKLYN	BROOKLYN	1008937	170310	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.634104	-73.911055	(40.634103775951736, -73.91105541883589)
32	26591378	10/31/2013 12:30:31 AM	NaN	TLC	Taxi and Limousine Commission	Taxi Complaint	Driver Complaint	NaN	10036	645 10 AVENUE	10 AVENUE	WEST 45 STREET	WEST 46 STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	NaN	Open	NaN	NaN	04 MANHATTAN	MANHATTAN	985965	216868	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	Other	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.761929	-73.993809	(40.761928847500016, -73.99380918401052)
33	26593872	10/31/2013 12:29:47 AM	10/31/2013 12:38:29 AM	NYPD	New York City Police Department	Noise - House of Worship	Banging/Pounding	House of Worship	10025	NaN	NaN	NaN	NaN	WEST 99 STREET	AMSTERDAM AVENUE	INTERSECTION	NEW YORK	NaN	Precinct	Closed	10/31/2013 08:29:47 AM	10/31/2013 12:38:29 AM	07 MANHATTAN	MANHATTAN	992846	229279	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.795990	-73.968954	(40.795989749917204, -73.96895423714467)
34	26591420	10/31/2013 12:28:30 AM	10/31/2013 02:06:11 AM	NYPD	New York City Police Department	Homeless Encampment	NaN	Residential Building/House	10025	2754 BROADWAY	BROADWAY	WEST 105 STREET	WEST 106 STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 08:28:30 AM	10/31/2013 02:06:11 AM	07 MANHATTAN	MANHATTAN	993139	231139	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.801095	-73.967894	(40.8010946529914, -73.96789356094007)
35	26592976	10/31/2013 12:23:24 AM	10/31/2013 01:05:41 AM	NYPD	New York City Police Department	Blocked Driveway	No Access	Street/Sidewalk	11433	173-41 103 ROAD	103 ROAD	173 STREET	177 STREET	NaN	NaN	ADDRESS	JAMAICA	NaN	Precinct	Closed	10/31/2013 08:23:24 AM	10/31/2013 01:05:41 AM	12 QUEENS	QUEENS	1044124	195866	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.704081	-73.784054	(40.70408112125158, -73.78405385422116)
36	26590262	10/31/2013 12:23:00 AM	NaN	DOT	Department of Transportation	Traffic Signal Condition	Controller	NaN	11235	NaN	NaN	NaN	NaN	SHORE BOULEVARD	CASS PLACE	INTERSECTION	BROOKLYN	NaN	NaN	Open	NaN	NaN	15 BROOKLYN	BROOKLYN	997073	151225	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.581744	-73.953836	(40.5817444882428, -73.95383634845487)
37	26589606	10/31/2013 12:20:44 AM	10/31/2013 02:10:24 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	11216	826 ST JOHN'S PLACE	ST JOHN'S PLACE	ROGERS AVENUE	NOSTRAND AVENUE	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 08:20:44 AM	10/31/2013 02:10:24 AM	08 BROOKLYN	BROOKLYN	997865	183985	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.671663	-73.950919	(40.671662601079895, -73.95091901534035)
38	26592083	10/31/2013 12:20:00 AM	NaN	DOT	Department of Transportation	Traffic Signal Condition	Controller	NaN	11213	NaN	NaN	NaN	NaN	BUFFALO AVENUE	PARK PLACE	INTERSECTION	BROOKLYN	NaN	NaN	Open	NaN	NaN	08 BROOKLYN	BROOKLYN	1004987	184136	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.672063	-73.925244	(40.67206324438088, -73.92524432147842)
39	26593840	10/31/2013 12:19:48 AM	NaN	NYPD	New York City Police Department	Blocked Driveway	No Access	Street/Sidewalk	11379	78-41 68 ROAD	68 ROAD	78 STREET	79 STREET	NaN	NaN	ADDRESS	MIDDLE VILLAGE	NaN	Precinct	Open	10/31/2013 08:19:48 AM	NaN	05 QUEENS	QUEENS	1019062	198120	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.710402	-73.874433	(40.71040190143904, -73.8744325577748)
40	26589646	10/31/2013 12:18:05 AM	10/31/2013 01:26:15 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	11101	34-19 STEINWAY STREET	STEINWAY STREET	34 AVENUE	35 AVENUE	NaN	NaN	ADDRESS	LONG ISLAND CITY	NaN	Precinct	Closed	10/31/2013 08:18:05 AM	10/31/2013 01:26:15 AM	01 QUEENS	QUEENS	1006080	214807	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.756245	-73.921205	(40.75624514774764, -73.92120466494264)
41	26593296	10/31/2013 12:16:25 AM	NaN	DOHMH	Department of Health and Mental Hygiene	Food Establishment	Rodents/Insects/Garbage	Restaurant/Bar/Deli/Bakery	10014	12 CHRISTOPHER STREET	CHRISTOPHER STREET	GREENWICH AVENUE	GAY STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	NaN	Open	12/07/2013 12:16:25 AM	NaN	02 MANHATTAN	MANHATTAN	984181	206685	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.733979	-74.000249	(40.73397924003587, -74.0002489720853)
42	26590480	10/31/2013 12:15:06 AM	10/31/2013 03:00:20 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Store/Commercial	11231	325 COLUMBIA STREET	COLUMBIA STREET	NaN	NaN	NaN	NaN	LATLONG	BROOKLYN	NaN	Precinct	Closed	10/31/2013 08:15:06 AM	10/31/2013 02:58:55 AM	06 BROOKLYN	BROOKLYN	982995	187440	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.681156	-74.004525	(40.68115617695543, -74.00452481832494)
43	26589626	10/31/2013 12:14:42 AM	10/31/2013 01:39:00 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	11234	2192 FLATBUSH AVENUE	FLATBUSH AVENUE	EAST 46 STREET	AVENUE O	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 08:14:42 AM	10/31/2013 01:39:00 AM	18 BROOKLYN	BROOKLYN	1003628	163910	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.616550	-73.930202	(40.61655032892211, -73.93020153359745)
44	26592898	10/31/2013 12:12:08 AM	10/31/2013 01:13:45 AM	NYPD	New York City Police Department	Noise - Park	Loud Talking	Park/Playground	10457	CROTONA PARK NORTH	CROTONA PARK NORTH	CLINTON AVENUE	PROSPECT AVENUE	NaN	NaN	BLOCKFACE	BRONX	NaN	Precinct	Closed	10/31/2013 08:12:08 AM	10/31/2013 01:13:45 AM	06 BRONX	BRONX	1013947	245819	Unspecified	BRONX	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.841342	-73.892672	(40.841341641554614, -73.89267161957397)
45	26590446	10/31/2013 12:11:58 AM	10/31/2013 01:54:38 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Music/Party	Street/Sidewalk	10459	819 EAST 167 STREET	EAST 167 STREET	UNION AVENUE	PROSPECT AVENUE	NaN	NaN	ADDRESS	BRONX	NaN	Precinct	Closed	10/31/2013 08:11:58 AM	10/31/2013 01:54:38 AM	03 BRONX	BRONX	1011935	240454	Unspecified	BRONX	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.826623	-73.899965	(40.826622810177874, -73.8999653556452)
46	26595546	10/31/2013 12:09:07 AM	10/31/2013 12:53:12 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10465	4005 EAST TREMONT AVENUE	EAST TREMONT AVENUE	SAMPSON AVENUE	GERBER PLACE	NaN	NaN	ADDRESS	BRONX	NaN	Precinct	Closed	10/31/2013 08:09:07 AM	10/31/2013 12:53:12 AM	10 BRONX	BRONX	1034640	238172	Unspecified	BRONX	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.820259	-73.817942	(40.820259030934515, -73.81794234356029)
47	26595944	10/31/2013 12:08:47 AM	NaN	TLC	Taxi and Limousine Commission	Taxi Complaint	Driver Complaint	NaN	10036	NaN	NaN	NaN	NaN	WEST 46 STREET	10 AVENUE	INTERSECTION	NEW YORK	NaN	NaN	Open	11/14/2013 12:08:47 AM	NaN	04 MANHATTAN	MANHATTAN	986020	216961	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	Other	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.762184	-73.993611	(40.76218409774632, -73.99361062023596)
48	26595084	10/31/2013 12:07:45 AM	10/31/2013 01:43:11 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10014	12 CHRISTOPHER STREET	CHRISTOPHER STREET	GREENWICH AVENUE	GAY STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 08:07:45 AM	10/31/2013 01:43:11 AM	02 MANHATTAN	MANHATTAN	984181	206685	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.733979	-74.000249	(40.73397924003587, -74.0002489720853)
49	26595553	10/31/2013 12:05:10 AM	10/31/2013 02:43:43 AM	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	11225	25 LEFFERTS AVENUE	LEFFERTS AVENUE	WASHINGTON AVENUE	BEDFORD AVENUE	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 08:05:10 AM	10/31/2013 01:29:29 AM	09 BROOKLYN	BROOKLYN	995366	180388	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.661793	-73.959934	(40.6617931276793, -73.95993363978067)
50	26594087	10/31/2013 12:04:50 AM	10/31/2013 01:09:38 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Store/Commercial	10011	258 WEST 15TH STREET	WEST 15TH STREET	NaN	NaN	NaN	NaN	LATLONG	NEW YORK	NaN	Precinct	Closed	10/31/2013 08:04:50 AM	10/31/2013 01:09:38 AM	04 MANHATTAN	MANHATTAN	983789	208891	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.740034	-74.001664	(40.74003415280169, -74.00166357336052)
51	26595572	10/31/2013 12:03:27 AM	NaN	DOT	Department of Transportation	Broken Muni Meter	No Receipt	Street	10003	NaN	NaN	NaN	NaN	EAST 10 STREET	2 AVENUE	INTERSECTION	NEW YORK	NaN	NaN	Open	11/21/2013 12:03:27 AM	NaN	03 MANHATTAN	MANHATTAN	987906	205154	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.729776	-73.986809	(40.72977626532991, -73.98680891976119)
52	26590848	10/31/2013 12:02:01 AM	10/31/2013 01:02:28 AM	NYPD	New York City Police Department	Blocked Driveway	No Access	Street/Sidewalk	11207	422 WYONA STREET	WYONA STREET	SUTTER AVENUE	BLAKE AVENUE	NaN	NaN	ADDRESS	BROOKLYN	NaN	Precinct	Closed	10/31/2013 08:02:01 AM	10/31/2013 01:02:28 AM	05 BROOKLYN	BROOKLYN	1014188	182855	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.668521	-73.892081	(40.66852085465471, -73.89208096944678)
53	26590413	10/31/2013 12:01:47 AM	10/31/2013 12:39:31 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10002	121 RIVINGTON STREET	RIVINGTON STREET	ESSEX STREET	NORFOLK STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 08:01:47 AM	10/31/2013 12:39:31 AM	03 MANHATTAN	MANHATTAN	987766	201503	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.719755	-73.987316	(40.71975521311322, -73.98731595609806)
54	26591287	10/31/2013 12:01:45 AM	10/31/2013 12:02:37 AM	HRA	HRA Benefit Card Replacement	Benefit Card Replacement	Medicaid	NYC Street Address	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Closed	NaN	NaN	0 Unspecified	Unspecified	NaN	NaN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
55	26595001	10/31/2013 12:01:34 AM	10/31/2013 01:32:43 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Store/Commercial	10034	524 WEST 207TH STREET	WEST 207TH STREET	NaN	NaN	NaN	NaN	LATLONG	NEW YORK	NaN	Precinct	Closed	10/31/2013 08:01:34 AM	10/31/2013 01:32:43 AM	01 MANHATTAN	MANHATTAN	1006481	254514	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.865229	-73.919626	(40.86522877164924, -73.91962575276823)
56	26591162	10/31/2013 12:01:00 AM	NaN	DSNY	BCC - Brooklyn South	Sanitation Condition	15 Street Cond/Dump-Out/Drop-Off	Street	11231	135 COLUMBIA STREET	COLUMBIA STREET	KANE STREET	IRVING STREET	NaN	NaN	ADDRESS	BROOKLYN	NaN	DSNY Garage	Open	NaN	NaN	06 BROOKLYN	BROOKLYN	983797	189648	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.687217	-74.001633	(40.68721671044577, -74.00163340956126)
57	26593459	10/31/2013 12:00:00 AM	NaN	HPD	Department of Housing Preservation and Develop...	ELECTRIC	ELECTRIC-SUPPLY	RESIDENTIAL BUILDING	11233	199 HOWARD AVENUE	HOWARD AVENUE	BAINBRIDGE STREET	CHAUNCEY STREET	NaN	NaN	ADDRESS	BROOKLYN	NaN	NaN	Open	NaN	10/31/2013 12:00:00 AM	03 BROOKLYN	BROOKLYN	1006513	187623	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.681631	-73.919732	(40.68163056217252, -73.91973166452124)
58	26592634	10/31/2013 12:00:00 AM	NaN	HPD	Department of Housing Preservation and Develop...	PLUMBING	BASIN/SINK	RESIDENTIAL BUILDING	11233	199 HOWARD AVENUE	HOWARD AVENUE	BAINBRIDGE STREET	CHAUNCEY STREET	NaN	NaN	ADDRESS	BROOKLYN	NaN	NaN	Open	NaN	10/31/2013 12:00:00 AM	03 BROOKLYN	BROOKLYN	1006513	187623	Unspecified	BROOKLYN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.681631	-73.919732	(40.68163056217252, -73.91973166452124)
59	26591688	10/31/2013 12:00:00 AM	NaN	HPD	Department of Housing Preservation and Develop...	HEATING	HEAT	RESIDENTIAL BUILDING	10453	150 WEST 179 STREET	WEST 179 STREET	ANDREWS AVENUE	LORING PLACE	NaN	NaN	ADDRESS	BRONX	NaN	NaN	Open	NaN	10/31/2013 12:00:00 AM	05 BRONX	BRONX	1008161	250940	Unspecified	BRONX	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.855415	-73.913565	(40.855414830918306, -73.91356461276855)
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
111069 rows × 52 columns

2.2 Selecting columns and rows
To select a column, we index with the name of the column, like this:

complaints['Complaint Type']
0      Noise - Street/Sidewalk
1              Illegal Parking
2           Noise - Commercial
3              Noise - Vehicle
4                       Rodent
5           Noise - Commercial
6             Blocked Driveway
7           Noise - Commercial
8           Noise - Commercial
9           Noise - Commercial
10    Noise - House of Worship
11          Noise - Commercial
12             Illegal Parking
13             Noise - Vehicle
14                      Rodent
...
111054    Noise - Street/Sidewalk
111055         Noise - Commercial
111056      Street Sign - Missing
111057                      Noise
111058         Noise - Commercial
111059    Noise - Street/Sidewalk
111060                      Noise
111061         Noise - Commercial
111062               Water System
111063               Water System
111064    Maintenance or Facility
111065            Illegal Parking
111066    Noise - Street/Sidewalk
111067         Noise - Commercial
111068           Blocked Driveway
Name: Complaint Type, Length: 111069, dtype: object
To get the first 5 rows of a dataframe, we can use a slice: df[:5].

This is a great way to get a sense for what kind of information is in the dataframe -- take a minute to look at the contents and get a feel for this dataset.

complaints[:5]
Unique Key	Created Date	Closed Date	Agency	Agency Name	Complaint Type	Descriptor	Location Type	Incident Zip	Incident Address	Street Name	Cross Street 1	Cross Street 2	Intersection Street 1	Intersection Street 2	Address Type	City	Landmark	Facility Type	Status	Due Date	Resolution Action Updated Date	Community Board	Borough	X Coordinate (State Plane)	Y Coordinate (State Plane)	Park Facility Name	Park Borough	School Name	School Number	School Region	School Code	School Phone Number	School Address	School City	School State	School Zip	School Not Found	School or Citywide Complaint	Vehicle Type	Taxi Company Borough	Taxi Pick Up Location	Bridge Highway Name	Bridge Highway Direction	Road Ramp	Bridge Highway Segment	Garage Lot Name	Ferry Direction	Ferry Terminal Name	Latitude	Longitude	Location
0	26589651	10/31/2013 02:08:41 AM	NaN	NYPD	New York City Police Department	Noise - Street/Sidewalk	Loud Talking	Street/Sidewalk	11432	90-03 169 STREET	169 STREET	90 AVENUE	91 AVENUE	NaN	NaN	ADDRESS	JAMAICA	NaN	Precinct	Assigned	10/31/2013 10:08:41 AM	10/31/2013 02:35:17 AM	12 QUEENS	QUEENS	1042027	197389	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.708275	-73.791604	(40.70827532593202, -73.79160395779721)
1	26593698	10/31/2013 02:01:04 AM	NaN	NYPD	New York City Police Department	Illegal Parking	Commercial Overnight Parking	Street/Sidewalk	11378	58 AVENUE	58 AVENUE	58 PLACE	59 STREET	NaN	NaN	BLOCKFACE	MASPETH	NaN	Precinct	Open	10/31/2013 10:01:04 AM	NaN	05 QUEENS	QUEENS	1009349	201984	Unspecified	QUEENS	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.721041	-73.909453	(40.721040535628305, -73.90945306791765)
2	26594139	10/31/2013 02:00:24 AM	10/31/2013 02:40:32 AM	NYPD	New York City Police Department	Noise - Commercial	Loud Music/Party	Club/Bar/Restaurant	10032	4060 BROADWAY	BROADWAY	WEST 171 STREET	WEST 172 STREET	NaN	NaN	ADDRESS	NEW YORK	NaN	Precinct	Closed	10/31/2013 10:00:24 AM	10/31/2013 02:39:42 AM	12 MANHATTAN	MANHATTAN	1001088	246531	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.843330	-73.939144	(40.84332975466513, -73.93914371913482)
3	26595721	10/31/2013 01:56:23 AM	10/31/2013 02:21:48 AM	NYPD	New York City Police Department	Noise - Vehicle	Car/Truck Horn	Street/Sidewalk	10023	WEST 72 STREET	WEST 72 STREET	COLUMBUS AVENUE	AMSTERDAM AVENUE	NaN	NaN	BLOCKFACE	NEW YORK	NaN	Precinct	Closed	10/31/2013 09:56:23 AM	10/31/2013 02:21:10 AM	07 MANHATTAN	MANHATTAN	989730	222727	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.778009	-73.980213	(40.7780087446372, -73.98021349023975)
4	26590930	10/31/2013 01:53:44 AM	NaN	DOHMH	Department of Health and Mental Hygiene	Rodent	Condition Attracting Rodents	Vacant Lot	10027	WEST 124 STREET	WEST 124 STREET	LENOX AVENUE	ADAM CLAYTON POWELL JR BOULEVARD	NaN	NaN	BLOCKFACE	NEW YORK	NaN	NaN	Pending	11/30/2013 01:53:44 AM	10/31/2013 01:59:54 AM	10 MANHATTAN	MANHATTAN	998815	233545	Unspecified	MANHATTAN	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	Unspecified	N	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	40.807691	-73.947387	(40.80769092704951, -73.94738703491433)
5 rows × 52 columns

We can combine these to get the first 5 rows of a column:

complaints['Complaint Type'][:5]
0    Noise - Street/Sidewalk
1            Illegal Parking
2         Noise - Commercial
3            Noise - Vehicle
4                     Rodent
Name: Complaint Type, dtype: object
and it doesn't matter which direction we do it in:

complaints[:5]['Complaint Type']
0    Noise - Street/Sidewalk
1            Illegal Parking
2         Noise - Commercial
3            Noise - Vehicle
4                     Rodent
Name: Complaint Type, dtype: object
2.3 Selecting multiple columns
What if we just want to know the complaint type and the borough, but not the rest of the information? Pandas makes it really easy to select a subset of the columns: just index with list of columns you want.

complaints[['Complaint Type', 'Borough']]
Complaint Type	Borough
0	Noise - Street/Sidewalk	QUEENS
1	Illegal Parking	QUEENS
2	Noise - Commercial	MANHATTAN
3	Noise - Vehicle	MANHATTAN
4	Rodent	MANHATTAN
5	Noise - Commercial	QUEENS
6	Blocked Driveway	QUEENS
7	Noise - Commercial	QUEENS
8	Noise - Commercial	MANHATTAN
9	Noise - Commercial	BROOKLYN
10	Noise - House of Worship	BROOKLYN
11	Noise - Commercial	MANHATTAN
12	Illegal Parking	MANHATTAN
13	Noise - Vehicle	BRONX
14	Rodent	BROOKLYN
15	Noise - House of Worship	MANHATTAN
16	Noise - Street/Sidewalk	STATEN ISLAND
17	Illegal Parking	BROOKLYN
18	Street Light Condition	BROOKLYN
19	Noise - Commercial	MANHATTAN
20	Noise - House of Worship	BROOKLYN
21	Noise - Commercial	MANHATTAN
22	Noise - Vehicle	QUEENS
23	Noise - Commercial	BROOKLYN
24	Blocked Driveway	STATEN ISLAND
25	Noise - Street/Sidewalk	STATEN ISLAND
26	Street Light Condition	BROOKLYN
27	Harboring Bees/Wasps	MANHATTAN
28	Noise - Street/Sidewalk	MANHATTAN
29	Street Light Condition	STATEN ISLAND
30	Blocked Driveway	STATEN ISLAND
31	Noise - Street/Sidewalk	BROOKLYN
32	Taxi Complaint	MANHATTAN
33	Noise - House of Worship	MANHATTAN
34	Homeless Encampment	MANHATTAN
35	Blocked Driveway	QUEENS
36	Traffic Signal Condition	BROOKLYN
37	Noise - Commercial	BROOKLYN
38	Traffic Signal Condition	BROOKLYN
39	Blocked Driveway	QUEENS
40	Noise - Commercial	QUEENS
41	Food Establishment	MANHATTAN
42	Noise - Commercial	BROOKLYN
43	Noise - Commercial	BROOKLYN
44	Noise - Park	BRONX
45	Noise - Street/Sidewalk	BRONX
46	Noise - Commercial	BRONX
47	Taxi Complaint	MANHATTAN
48	Noise - Commercial	MANHATTAN
49	Noise - Street/Sidewalk	BROOKLYN
50	Noise - Commercial	MANHATTAN
51	Broken Muni Meter	MANHATTAN
52	Blocked Driveway	BROOKLYN
53	Noise - Commercial	MANHATTAN
54	Benefit Card Replacement	Unspecified
55	Noise - Commercial	MANHATTAN
56	Sanitation Condition	BROOKLYN
57	ELECTRIC	BROOKLYN
58	PLUMBING	BROOKLYN
59	HEATING	BRONX
...	...
111069 rows × 2 columns

That showed us a summary, and then we can look at the first 10 rows:

complaints[['Complaint Type', 'Borough']][:10]
Complaint Type	Borough
0	Noise - Street/Sidewalk	QUEENS
1	Illegal Parking	QUEENS
2	Noise - Commercial	MANHATTAN
3	Noise - Vehicle	MANHATTAN
4	Rodent	MANHATTAN
5	Noise - Commercial	QUEENS
6	Blocked Driveway	QUEENS
7	Noise - Commercial	QUEENS
8	Noise - Commercial	MANHATTAN
9	Noise - Commercial	BROOKLYN
10 rows × 2 columns

2.4 What's the most common complaint type?
This is a really easy question to answer! There's a .value_counts() method that we can use:

complaints['Complaint Type'].value_counts()
HEATING                     14200
GENERAL CONSTRUCTION         7471
Street Light Condition       7117
DOF Literature Request       5797
PLUMBING                     5373
PAINT - PLASTER              5149
Blocked Driveway             4590
NONCONST                     3998
Street Condition             3473
Illegal Parking              3343
Noise                        3321
Traffic Signal Condition     3145
Dirty Conditions             2653
Water System                 2636
Noise - Commercial           2578
...
Opinion for the Mayor                2
Window Guard                         2
DFTA Literature Request              2
Legal Services Provider Complaint    2
Open Flame Permit                    1
Snow                                 1
Municipal Parking Facility           1
X-Ray Machine/Equipment              1
Stalled Sites                        1
DHS Income Savings Requirement       1
Tunnel Condition                     1
Highway Sign - Damaged               1
Ferry Permit                         1
Trans Fat                            1
DWD                                  1
Length: 165, dtype: int64
If we just wanted the top 10 most common complaints, we can do this:

complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]
HEATING                   14200
GENERAL CONSTRUCTION       7471
Street Light Condition     7117
DOF Literature Request     5797
PLUMBING                   5373
PAINT - PLASTER            5149
Blocked Driveway           4590
NONCONST                   3998
Street Condition           3473
Illegal Parking            3343
dtype: int64
But it gets better! We can plot them!

complaint_counts[:10].plot(kind='bar')