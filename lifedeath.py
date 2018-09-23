import matplotlib.pyplot as plt

plt.style.use('ggplot')

life = 0.1
death = 1 - life

lifedeath = [100 * life, 100 * death]

fig, ax = plt.subplots(1,1)

pie, labels = ax.pie(lifedeath, labels=('Life', 'Death'),
										 colors=['#1b9e77', '#d95f02'])


[p.set_linewidth(0) for p in pie]

# Add a circle to make it a donut chart
circle = plt.Circle((0,0), 0.7, color='w')

ax.add_artist(circle)
ax.set_aspect('equal')

# ax.legend(('Life', 'Death'))

plt.show()


