# LOL Worlds S13: Swiss Stage V.S Group Stage

Riot games has switched from traditional group stage to swiss stage before knock-off stage. There are a lot of positive comment on swiss stage. Some would even describe it as the fairest method for electing the strongest team. However, is that so? I build a small program to test it.

## Dependent tools

I used following third-party dependent tools:

- [numpy] - Math tool
- [matplotlib] - For plotting the result
- [progress] - To show the progress bar

## Explanation

There are countless factors that can decide the comprehensive power for a team. Sometimes, a weaker team out-matches a stronger team as there are many examples at group stage in LOL worlds. For example, in S12, Top Esports lost to other teams which in paper, Top Esports is stronger.

Additionally, side choice of the map affects the overall winning rate, as in official ranked game, Blue side has the winning rate of 56%. In professional esports, this factor contributes more, as some time blue side tends to have more chance to lock a better champion composition. 

There are many studies on what contributes to the overall strength of a team. However, we would not discuss much about it in this team. In this simple program, I simply made those team to have different performance score.

## Method

There are 4 major league in LOL. LPL, LCK, LCS, LEC. Everytime, the LCK and LPL tends to perform better, hence having more seats. Consider the performance difference in the past few years, there is no much difference in LPL and LCK. Thus, we consider the TOP 1 and TOP 2 league to be LPL and LCK, having 4 seats. And we set the condition so that the #1 in the second league matches the #3 in the third league.

For the rest leagues, some of them are guaranteed a seat to the group/swiss stage. Some of them must fight through the Play-In stage in order to be in the group/swiss stage. Since they are already in, I will consider them as a member of the rest of the league for convience. I will rank their strength in decreasing order. The specific allocation is at below:

| Strength Level | #1 League | #2 League | #3 League | #4 League |
| :------: | :------: | :------: | :------: | :------: |
| 9 | Seed 1 |        |        |  |
| 8 | Seed 2 |        |        |  |
| 7 | Seed 3 | Seed 1 |        |  |
| 6 | Seed 4 | Seed 2 |        |  |
| 5 |        | Seed 3 | Seed 1 |  |
| 4 |        | Seed 4 | Seed 2 | Seed 1 |
| 3 |        |        | Seed 3 | Seed 2 |
| 2 |        |        | Seed 4 | Seed 3 |
| 1 |        |        |        | Seed 4 |

Thus, in decreasing order of the strength level, we have the team:
| Team# | Team Name | Strength Level | 
| :-: | :-: | :-: |
| 1  | Seed 1 / #1 League | 9 |
| 2  | Seed 2 / #1 League | 8 |
| 3  | Seed 3 / #1 League | 7 |
| 4  | Seed 1 / #2 League | 7 |
| 5  | Seed 4 / #1 League | 6 |
| 6  | Seed 2 / #2 League | 6 |
| 7  | Seed 3 / #2 League | 5 |
| 8  | Seed 1 / #3 League | 5 |
| 9  | Seed 4 / #2 League | 4 |
| 10 | Seed 2 / #3 League | 4 |
| 11 | Seed 1 / #4 League | 4 |
| 12 | Seed 3 / #3 League | 3 |
| 13 | Seed 2 / #4 League | 3 |
| 14 | Seed 4 / #3 League | 2 |
| 15 | Seed 3 / #4 League | 2 |
| 16 | Seed 4 / #4 League | 1 |

> Note: You can change to your own performance level at the top (line 6 to line 10).

Thus, with a performance level giving, we can decide which team is stronger conveniently. However, in real world, like I mentioned before, a strong team would not necessarily win. Thus, I design the following mechanism:

- There are 5% chance that the weaker team wins directly.
- A performance difference of 1 would have chance to be added to the game as another suprise factor.
- If performance difference is the same, there are 56% chance that the blue team wins, in this case, team 1. Since team 1 compares to team 1 is higher on the seed table, which has the right to choose side, which would grants them a advantage.

## Running

Install the python interpreter first, then install numpy and matplotlib in an open terminal. Press Win + R, type in "powershell", then hit enter.

Type the following command in each line to install:
```sh
python -m pip install --upgrade pip
pip install matplotlib
pip install numpy
pip install progress
```

Then run the code:

```sh
python LOL_Team_Result_Sim.py
```

You can change the team_performance parameter for your own performance standard in line 6 through 10. You can also change the round_try parameter at line 12 to decide how many iteration you want. Larger the number, more accurate the result.

## Results:

Following is the result of a sample run with 1,000,000 iteration for both stage.
> Note: From team 1 to 16, their performance is level is in decreasing order.

### Swiss Stage:

| Team# | Team Name | Strength Level | % of promotion
| :-: | :-: | :-: | :-: |
| 1  | Seed 1 / #1 League | 9 | 98.84% |
| 2  | Seed 2 / #1 League | 8 | 95.16% |
| 3  | Seed 3 / #1 League | 7 | 82.78% |
| 4  | Seed 1 / #2 League | 7 | 82.83% |
| 5  | Seed 4 / #1 League | 6 | 63.55% |
| 6  | Seed 2 / #2 League | 6 | 63.28% |
| 7  | Seed 3 / #2 League | 5 | 46.67% |
| 8  | Seed 1 / #3 League | 5 | 46.67% |
| 9  | Seed 4 / #2 League | 4 | 29.74% |
| 10 | Seed 2 / #3 League | 4 | 29.75% |
| 11 | Seed 1 / #4 League | 4 | 29.79% |
| 12 | Seed 3 / #3 League | 3 | 10.71% |
| 13 | Seed 2 / #4 League | 3 | 10.69% |
| 14 | Seed 4 / #3 League | 2 | 1.65% |
| 15 | Seed 3 / #4 League | 2 | 1.64% |
| 16 | Seed 4 / #4 League | 1 | 0.20% |

### Traditional Group Stage:

| Team# | Team Name | Strength Level | % of promotion
| :-: | :-: | :-: | :-: |
| 1  | Seed 1 / #1 League | 9 | 90.66% |
| 2  | Seed 2 / #1 League | 8 | 90.60% |
| 3  | Seed 3 / #1 League | 7 | 90.61% |
| 4  | Seed 1 / #2 League | 7 | 90.64% |
| 5  | Seed 4 / #1 League | 6 | 90.87% |
| 6  | Seed 2 / #2 League | 6 | 90.88% |
| 7  | Seed 3 / #2 League | 5 | 83.60% |
| 8  | Seed 1 / #3 League | 5 | 83.63% |
| 9  | Seed 4 / #2 League | 4 | 13.98% |
| 10 | Seed 2 / #3 League | 4 | 13.99% |
| 11 | Seed 1 / #4 League | 4 | 13.98% |
| 12 | Seed 3 / #3 League | 3 | 14.99% |
| 13 | Seed 2 / #4 League | 3 | 12.15% |
| 14 | Seed 4 / #3 League | 2 | 9.32% |
| 15 | Seed 3 / #4 League | 2 | 6.50% |
| 16 | Seed 4 / #4 League | 1 | 3.61% |

### Figure:
![Figure_1](https://github.com/Pansions/LOL-S13-Worlds-Swiss-Stage-V.S-Group-Stage/assets/53805355/e2f4e247-1004-46ac-aae4-be8764bfbd59)

### Original output text:

> For the Swiss stage, The percentage for promotion from team 1 to team 16 with decreasing performance level is:
Team 1: 98.84%;   Team 2: 95.16%;   Team 3: 82.78%;   Team 4: 82.83%;   Team 5: 63.55%;   Team 6: 63.28%;   Team 7: 46.67%;   Team 8: 46.67%;   Team 9: 29.74%;   Team 10: 29.75%;   Team 11: 29.79%;   Team 12: 10.71%;   Team 13: 10.69%;   Team 14: 1.65%;   Team 15: 1.64%;   Team 16: 0.20%.

> For the traditional group stage, The percentage for promotion from team 1 to team 16 with decreasing performance level is:
Team 1: 90.66%;   Team 2: 90.60%;   Team 3: 90.61%;   Team 4: 90.64%;   Team 5: 90.87%;   Team 6: 90.88%;   Team 7: 83.60%;   Team 8: 83.63%;   Team 9: 13.98%;   Team 10: 13.99%;   Team 11: 13.98%;   Team 12: 14.99%;   Team 13: 12.15%;   Team 14: 9.32%;   Team 15: 6.50%;   Team 16: 3.61%.

