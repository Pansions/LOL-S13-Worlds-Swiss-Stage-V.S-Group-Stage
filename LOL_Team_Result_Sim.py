import numpy as np
from matplotlib import pyplot as plt
from progress.bar import Bar

# Global variable: team ability and their number
# Make change to your variable here:
team_performance = np.array([9,8,7,6,            #1 League
                                 7,6,5,4,        #2 League
                                     5,4,3,2,    #3 League
                                       4,3,2,1]) #4 League
team_ab = np.sort(team_performance)[::-1]
team_no = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

round_try = 1000000


class team_struct():
    def __init__(self, ta):
        self.team_ability = ta
        self.team_win = 0
        self.team_lose = 0
        self.team_temp_win = 0
        self.team_temp_lose = 0
        
    def game(self, team_s_2):
        def self_win():
            self.team_temp_win += 1
            team_s_2.team_temp_lose += 1
        
        def self_lose():
            self.team_temp_lose += 1
            team_s_2.team_temp_win +=1
        # Team ability diff
        ability_diff = self.team_ability - team_s_2.team_ability
        
        
        # Blue has 56% percent of wining.
        # Ability diff can be make up if one gots blue.
        suprise2 = np.random.randint(-1,2)
        ability_diff += suprise2
        
        
        # Suprise factor, weaker team has 5% chance of wining
        suprise = np.random.randint(0,100)
        if ability_diff > 0:
            if suprise < 95:
                self_win()
            else:   
                self_lose()
        elif ability_diff < 0:
            if suprise < 95:
                self_lose()
            else:   
                self_win()
        elif ability_diff == 0:
            suprise3 = np.random.randint(0,100)
            if suprise3 > 56:
                self_lose()
            else:
                self_win()
    
        
    
# Swiss Stage Game Play
def ss(team_ss):
    # Assign the group
    
    # Round 1: 0-0:
    team_order_0_0 = np.random.permutation(team_no)
    
    for i in range(0,15,2):
        team_ss[team_order_0_0[i]].game(team_ss[team_order_0_0[i+1]])
    
    
    # Round 2: 
    team_order_1_0 = []
    team_order_0_1 = []
    for i, t in enumerate(team_ss):
        if t.team_temp_win == 1:
            team_order_1_0.append(i)
        elif t.team_temp_lose == 1:
            team_order_0_1.append(i)
    team_order_1_0 = np.random.permutation(np.array(team_order_1_0))
    team_order_0_1 = np.random.permutation(np.array(team_order_0_1))
        # 1-0:
    for i in range(0,8,2):
        team_ss[team_order_1_0[i]].game(team_ss[team_order_1_0[i+1]])
        # 0-1:
    for i in range(0,8,2):
        team_ss[team_order_0_1[i]].game(team_ss[team_order_0_1[i+1]])
        
    # Round 3:
    team_order_2_0 = []
    team_order_1_1 = []
    team_order_0_2 = []
    for i, t in enumerate(team_ss):
        if t.team_temp_win == 2 and t.team_temp_lose == 0:
            team_order_2_0.append(i)
        elif t.team_temp_win == 1 and t.team_temp_lose == 1:
            team_order_1_1.append(i)
        elif t.team_temp_win == 0 and t.team_temp_lose == 2:
            team_order_0_2.append(i)
    team_order_2_0 = np.random.permutation(np.array(team_order_2_0))
    team_order_1_1 = np.random.permutation(np.array(team_order_1_1))
    team_order_0_2 = np.random.permutation(np.array(team_order_0_2))
        # 2-0:
    for i in range(0,4,2):
        team_ss[team_order_2_0[i]].game(team_ss[team_order_2_0[i+1]])
        # 1-1:
    for i in range(0,8,2):
        team_ss[team_order_1_1[i]].game(team_ss[team_order_1_1[i+1]])
        # 0-2:
    for i in range(0,4,2):
        team_ss[team_order_0_2[i]].game(team_ss[team_order_0_2[i+1]])
    
    # Round 4:
    team_order_3_0 = []
    team_order_2_1 = []
    team_order_1_2 = []
    team_order_0_3 = []
    for i, t in enumerate(team_ss):
        if t.team_temp_win == 3 and t.team_temp_lose == 0:
            team_order_3_0.append(i)
        elif t.team_temp_win == 2 and t.team_temp_lose == 1:
            team_order_2_1.append(i)
        elif t.team_temp_win == 1 and t.team_temp_lose == 2:
            team_order_1_2.append(i)
        elif t.team_temp_win == 0 and t.team_temp_lose == 3:
            team_order_0_3.append(i)
    # Win = 3 = Upgrade to play-off. Otherwise out
    for t in team_order_3_0:
        team_ss[t].team_win += 1
    for t in team_order_0_3:
        team_ss[t].team_lose += 1
            
    team_order_1_2 = np.random.permutation(np.array(team_order_1_2))
    team_order_2_1 = np.random.permutation(np.array(team_order_2_1))
        # 2-1:
    for i in range(0,6,2):
        team_ss[team_order_2_1[i]].game(team_ss[team_order_2_1[i+1]])
        # 1-2:
    for i in range(0,6,2):
        team_ss[team_order_1_2[i]].game(team_ss[team_order_1_2[i+1]])
    
    # Round 5:
    team_order_3_1 = []
    team_order_2_2 = []
    team_order_1_3 = []
    for i, t in enumerate(team_ss):
        if t.team_temp_win == 3 and t.team_temp_lose == 1:
            team_order_3_1.append(i)
        elif t.team_temp_win == 2 and t.team_temp_lose == 2:
            team_order_2_2.append(i)
        elif t.team_temp_win == 1 and t.team_temp_lose == 3:
            team_order_1_3.append(i)
    # Win = 3 = Upgrade to play-off. Otherwise out
    for t in team_order_3_1:
        team_ss[t].team_win += 1
    for t in team_order_1_3:
        team_ss[t].team_lose += 1
            
    team_order_2_2 = np.random.permutation(np.array(team_order_1_2))
        # 2-2:
    for i in range(0,6,2):
        team_ss[team_order_2_2[i]].game(team_ss[team_order_2_2[i+1]])
    
    # Round 6:
    team_order_3_2 = []
    team_order_2_3 = []
    for i, t in enumerate(team_ss):
        if t.team_temp_win == 3 and t.team_temp_lose == 2:
            team_order_3_2.append(i)
        elif t.team_temp_win == 2 and t.team_temp_lose == 3:
            team_order_2_3.append(i)
    # Win = 3 = Upgrade to play-off. Otherwise out
    for t in team_order_3_2:
        team_ss[t].team_win += 1
    for t in team_order_2_3:
        team_ss[t].team_lose += 1
        
    # Clear the temp variable
    for t in team_ss:
        t.team_temp_win = 0
        t.team_temp_lose = 0

# Group Stage Game Play
def gs(team_gs):
    # Assign Groups:
    team_order_1st_sec = np.random.permutation(np.array([0,1,2,3]))
    team_order_2nd_sec = np.random.permutation(np.array([0,1,2,3]))
    team_order_3rd_sec = np.random.choice(4,3,replace = False)
    
    # Calculate the missing number for the rest of the sector
    missing_no = int(6 - np.sum(team_order_3rd_sec))
    team_order_4th_sec = np.random.permutation(np.array([0,1,2,3,missing_no]))
    
    groups = [[],[],[],[]]    
    
    for i,i2 in enumerate(team_order_1st_sec):
        groups[team_order_1st_sec[i]].append(np.where(team_order_1st_sec == i2)[0][0])
    for i,i2 in enumerate(team_order_2nd_sec):
        groups[team_order_2nd_sec[i]].append(np.where(team_order_2nd_sec == i2)[0][0] + 4)
    for i,i2 in enumerate(team_order_3rd_sec):
        groups[team_order_3rd_sec[i]].append(np.where(team_order_3rd_sec == i2)[0][0] + 8)
    for i,i2 in enumerate(team_order_4th_sec):
        groups[team_order_4th_sec[i]].append(np.where(team_order_4th_sec == i2)[0][0] + 11)
    
    # Start group stage
    for i in range(0,4):
        # 6 games
        team_gs[groups[i][0]].game(team_gs[groups[i][1]])
        team_gs[groups[i][0]].game(team_gs[groups[i][2]])
        team_gs[groups[i][0]].game(team_gs[groups[i][3]])
        team_gs[groups[i][1]].game(team_gs[groups[i][2]])
        team_gs[groups[i][1]].game(team_gs[groups[i][3]])
        team_gs[groups[i][2]].game(team_gs[groups[i][3]])
        
        # Top 2 goes to knock-out stage, rest is out
        group_wins = np.array([team_gs[groups[i][0]].team_temp_win, team_gs[groups[i][1]].team_temp_win, 
                               team_gs[groups[i][2]].team_temp_win, team_gs[groups[i][3]].team_temp_win])
        
        sorted_group_wins = np.argsort(group_wins)
        
        # Get the team wining the game
        team_gs[groups[i][np.where(sorted_group_wins == 3)[0][0]]].team_win += 1
        team_gs[groups[i][np.where(sorted_group_wins == 2)[0][0]]].team_win += 1
        team_gs[groups[i][np.where(sorted_group_wins == 1)[0][0]]].team_lose += 1
        team_gs[groups[i][np.where(sorted_group_wins == 0)[0][0]]].team_lose += 1
        
        for j in range(0,4):
            team_gs[groups[i][j]].team_temp_win = 0
            team_gs[groups[i][j]].team_temp_lose = 0
    
    

def main():
    # Generate Teams:
    # 16 teams in total, ability ranked in orders.
    # Team with greater ability out ranks the lower ones. However, the lower one has 5% chance of wining.
    team_no = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    
    # Swiss Stage Teams
    team_ss = []
    for i in team_ab:
        team = team_struct(i)
        team_ss.append(team)
    
    # Swiss System Plays
    ss_count = 0
    with Bar('Calculating Swiss Stage...', max = round_try) as bar:
        for i in range(0, round_try):
            ss(team_ss)
            ss_count += 1
            bar.next()
    
    # Traditional Group stage
    team_gs = []
    for i in team_ab:
        team = team_struct(i)
        team_gs.append(team)
    
    # Group stage plays
    gs_count = 0
    with Bar('Calculating Group Stage...', max = round_try) as bar2:
        for i in range(0, round_try):
            gs(team_gs)
            gs_count += 1
            bar2.next()
    
    # Calculate the win rates
    win_rate_ss = np.zeros((16))
    for i, t in enumerate(team_ss):
        win_rate_ss[i] = t.team_win / ss_count
        
    win_rate_gs = np.zeros((16))
    for i, t in enumerate(team_gs):
        win_rate_gs[i] = t.team_win / gs_count
        
    # Text output:
    print()
    print("For the swiss stage, The percentage for promption from team 1 to team 16 with decreasing performance level is:")
    for i, wr in enumerate(win_rate_ss):
        print(f"Team {i+1}: {wr*100:.2f}%", end = "")
        if i != len(win_rate_ss)-1: print(";", end = "   ")
        else: print(".")
    
    print()
    print("For the traditional group stage, The percentage for promotion from team 1 to team 16 with decreasing performance level is:")
    for i, wr in enumerate(win_rate_gs):
        print(f"Team {i+1}: {wr*100:.2f}%", end = "")
        if i != len(win_rate_ss)-1: print(";", end = "   ")
        else: print(".", end = "\n\n")
    
    # Plot the figures
    plt.figure()
    plt.grid()
    # Plot the swiss stage
    plt.plot(team_no, (win_rate_ss*100), label = 'swiss')
    # for i, j in zip(team_no, (win_rate_ss*100)):
    #     plt.text(i, j, f'{j:.1f}', ha = 'right')
    # Plot the group stage
    plt.plot(team_no, (win_rate_gs*100), label = 'group')
    # Name the axis
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16',])
    plt.yticks([0,10,20,30,40,50,60,70,80,90,100], ['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%',])
    plt.xlabel("team number")
    plt.ylabel("percentage of promotion")
    plt.legend()
    plt.show()
    
    
    
    
if __name__ == "__main__":
    main()