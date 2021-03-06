import shelve
import os
from pathlib import Path
import re
import random

s = """
Alabama	AL	1819	Montgomery	1846	159.8	198,218	373,903	2	119
Alaska	AK	1959	Juneau	1906	2716.7	31,275		3		Largest capital by municipal land area.
Arizona	AZ	1912	Phoenix	1889	517.6	1,660,272	4,857,962	1	5	Largest capital by population.
Arkansas	AR	1836	Little Rock	1821	116.2	193,524	699,757	1	117
California	CA	1850	Sacramento	1854	97.9	508,529	2,345,210	6	35	Largest capital by population to not be the most populated city in its state.
Colorado	CO	1876	Denver	1867	153.3	716,492	2,932,415	1	19
Connecticut	CT	1788	Hartford	1875	17.3	124,775	1,212,381	3	199
Delaware	DE	1787	Dover	1777	22.4	36,047	162,310	2		Longest-serving capital in terms of statehood.
Florida	FL	1845	Tallahassee	1824	95.7	181,376	367,413	7	125
Georgia	GA	1788	Atlanta	1868	133.5	498,044	5,949,951	1	37	Largest capital by metropolitan area population.
Hawaii	HI	1959	Honolulu	1845	68.4	359,870	953,207	1	56
Idaho	ID	1890	Boise	1865	63.8	205,671	616,561	1	103
Illinois	IL	1818	Springfield	1837	54.0	116,250	210,170	6	221
Indiana	IN	1816	Indianapolis	1825	361.5	867,125	2,004,230	1	16
Iowa	IA	1846	DesMoines	1857	75.8	203,433	569,633	1	105
Kansas	KS	1861	Topeka	1856	56.0	127,473	230,870	4	193
Kentucky	KY	1792	Frankfort	1792	14.7	25,527	70,758	14
Louisiana	LA	1812	BatonRouge	1880	76.8	225,374	830,480	2	99
Maine	ME	1820	Augusta	1832	55.4	19,136	117,114	8
Maryland	MD	1788	Annapolis	1694	6.73	38,394		7		Smallest capital by land area.
Massachusetts	MA	1788	Boston	1630	89.6	694,583	4,628,910	1	21	Longest continuously serving capital.
Michigan	MI	1837	Lansing	1847	35.0	114,297	464,036	5	226
Minnesota	MN	1858	SaintPaul	1849	52.8	285,068	3,348,659	2	67
Mississippi	MS	1817	Jackson	1821	104.9	173,514	567,122	1	134
Missouri	MO	1821	JeffersonCity	1826	27.3	43,079	149,807	15
Montana	MT	1889	Helena	1875	14.0	28,190	74,801	6
Nebraska	NE	1867	Lincoln	1867	74.6	258,379	302,157	2	72
Nevada	NV	1864	CarsonCity	1861	143.4	55,274		6
NewHampshire	NH	1788	Concord	1808	64.3	42,695	146,445	3
NewJersey	NJ	1787	Trenton	1784	7.66	84,913	366,513	10
NewMexico	NM	1912	SantaFe	1610	37.3	75,764	183,732	4		Longest-serving capital.
NewYork	NY	1788	Albany	1797	21.4	97,856	857,592	6
NorthCarolina	NC	1789	Raleigh	1792	114.6	403,892	1,130,490	2	43
NorthDakota	ND	1889	Bismarck	1883	26.9	61,272	108,779	2
Ohio	OH	1803	Columbus	1816	210.3	892,553	2,078,725	1	14
Oklahoma	OK	1907	Oklahoma City	1910	620.3	649,021	1,396,445	1	27	Shortest-serving current state capital.
Oregon	OR	1859	Salem	1855	45.7	154,637	390,738	3	149
Pennsylvania	PA	1787	Harrisburg	1812	8.11	49,528	647,390	9
RhodeIsland	RI	1790	Providence	1900	18.5	178,042	1,600,852	1	130
SouthCarolina	SC	1788	Columbia	1786	125.2	129,272	767,598	2	191
SouthDakota	SD	1889	Pierre	1889	13.0	13,646		8
Tennessee	TN	1796	Nashville	1826	525.9	691,243	1,903,045	1	24
Texas	TX	1845	Austin	1839	305.1	964,254	2,168,316	4	11
Utah	UT	1896	SaltLakeCity	1858	109.1	186,440	1,087,873	1	124
Vermont	VT	1791	Montpelier	1805	10.2	7,855		6		Smallest capital by population.
Virginia	VA	1788	Richmond	1780	60.1	204,214	1,208,101	4	104
Washington	WA	1889	Olympia	1853	16.7	46,478	234,670	24
WestVirginia	WV	1863	Charleston	1885	31.6	51,400	304,214	1		Smallest capital by population to also be the most populated city in its state.
Wisconsin	WI	1848	Madison	1838	68.7	233,209	605,435	2	82
Wyoming	WY	1890	Cheyenne	1869	21.1	59,466	91,738	1
"""

state_capitals = {}
L = s.splitlines()
L.pop(0)
r = re.compile(r'(\w+)\t(\w+)\t(\w+)\t(\w+)')
for l in L:
    mo = r.search(l)
    state_capitals[mo.group(1)] = mo.group(4)
# print(state_capitals)

# start by making a dir where all quizzes will be stored
# os.mkdir('9_quiz_dir')
cwd = Path.cwd()
p = cwd / '9_quiz_dir'
print(p)

state_capitals_list = list(state_capitals.items())

# create 5 quizzes
for k in range(5):
    # write questions / answers to 2 separate files
    with open(p/f'{k+1} questions.txt', 'w') as f1, open(p/f'{k+1} answers.txt', 'w') as f2:
        # shuffles the 50 questions / answers for each quiz
        random.shuffle(state_capitals_list)
        i = 0
        # take the 50 states and generate 50 questions
        for state, capital in state_capitals_list:
            i += 1  # start counting at 1
            Q = f'What is the capital of {state}?'
            correct_A = capital
            As = [correct_A]
            # for each shows the correct answer and 3 random ones
            for j in range(3):
                As.append(random.choice(list(state_capitals.values())))
            # shuffle the anwsers too
            random.shuffle(As)
            # write to 2 files
            f1.write(f'{i}) {Q} -> {As}\n')
            f2.write(f'{i}) {Q} -> {correct_A}\n')
