from matplotlib import pyplot as plt


print(plt.style.available)
plt.style.use('_mpl-gallery')


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['#4e09ed', '#7759bd', '#a699c4']

#plt.pie([1, 1, 1], labels=['player 1', 'player 2', 'player3'])
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.title('My Awesome stack plot')
plt.tight_layout()
plt.legend(loc=(0.07, 0.05))
plt.show()