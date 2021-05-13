import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Team_A = []
Team_B = []

trade = 1
p = 0.5 # Probability of Team A win the trade
q = 0.5 # Probability of Team B win the trade
advantage = 0.01 # Trade advantage
for i in range(100):
   won_mini_trade = np.random.choice(["A","B"],p=[p,q])
   if (won_mini_trade == "A"):
      if (p < 0.99):
         p += advantage
         q -= advantage
      Team_A.append(trade)
      Team_B.append(0)
   else :
      if (q < 0.99):
         p -= advantage
         q += advantage
      Team_B.append(trade)
      Team_A.append(0)
fig, ax = plt.subplots()
ax.plot([ sum(Team_A[:i]) for i in range(1,len(Team_A))], label="Team A") # Plot the summation of gold earned at every trade
ax.plot([ sum(Team_B[:i]) for i in range(1,len(Team_B))], label="Team B")
ax.set(xlabel='Time', ylabel='Gold', title='League of Legends Gold Stochastic Process')
ax.legend()
ax.grid()
plt.show()