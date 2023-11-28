from matplotlib import pyplot as plt

plt.rc("font", family="Malgun Gothic")
print(plt.style.available)
plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
colors = ['#4787ed', '#45e68d', '#771182', '#de547b', '#d16d52']
explode = [0, 0, 0, 0.1, 0]


plt.pie(slices, labels=labels, wedgeprops={'edgecolor': '#a8ffeb'}, colors=colors, explode=explode,\
        shadow=True, startangle=90, autopct='%1.1f%%')


plt.title("my awesome pie chart")
#plt.tight_layout
#plt.legend()
plt.show()