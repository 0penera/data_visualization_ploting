import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
import numpy as np

sns.dark_palette("r")

# dot and line plot
tips = sns.load_dataset("tips")
p = so.Plot(data=tips, x="total_bill", y="tip", color="sex")\
.add(so.Dot(alpha=0.5), pointsize="size")\
.add(so.Line(linewidth=2.5, color=".8"), so.PolyFit())\
.scale(pointsize=(2, 15))
# p.show()

# dot plot
tips = sns.load_dataset("tips")
p = so.Plot(data=tips, x="total_bill", y="size", color="time")\
.add(so.Dot(alpha=.7), so.Dodge(), so.Jitter(0.4), orient="y")
# p.show()

# bar plot
from matplotlib import style
tips = sns.load_dataset("tips")
(
    so.Plot(data=tips, y="day", color="sex", x="tip")
    .add(so.Bar(), so.Agg(), so.Dodge())
    .add(so.Text(color="w", halign="right"))
    .label(title="tips week")
    .theme({**style.library["fivethirtyeight"]})
    # .show()
)

# bar, hist plot
from matplotlib import style
tips = sns.load_dataset("tips")
(
    so.Plot(data=tips, y="day", color="sex")
    .add(so.Bar(), so.Hist(), so.Dodge())
    .label(title="tips week")
    .theme({**style.library["fivethirtyeight"]})
    # .show()
)

# subplots
tips = sns.load_dataset("tips")
(
    so.Plot(data=tips, x="total_bill", y="tip", color="day")
    .facet(col="day", wrap=2)
    .label(title="{} grade".format)
    .share(x=False, y =True)
    .label(color=str.capitalize)
    .add(so.Dot(color="gray", alpha=0.3), col=None, color=None)
    .add(so.Dot()).scale(color="summer", pointsize=(2, 10))
    # .show()
)

# facet
mpg = sns.load_dataset("mpg")
p = (
    so.Plot(data=mpg, x="weight")
    .pair(y=["horsepower", "acceleration"])
    .label(x="weight_0", y0="accelerations_0", y1="accerations_1")
    .facet(col="origin").label(col="cars: ")
    .label(title=str.upper)
    .add(so.Dots())
    .layout(size=(8, 4))
)
# p.show()

# pair plot
mpg = sns.load_dataset("mpg")
(
    so.Plot(data=mpg)
    .pair(x=["displacement", "weight"], y=["horsepower", "acceleration"])
    .add(so.Dots())
    # .show()
)

# dot plots
tips = sns.load_dataset("tips")
(
    so.Plot(data=tips, x="total_bill", y="tip")
    .add(so.Dot(color="#aabc"))
    .add(so.Dot(), data=tips.query("size == 2"), color="time")
    # .show()
)

# bar plot
tips= sns.load_dataset("tips")
(
    so.Plot(data=tips, x="day")
    .add(so.Bar(), so.Hist(), weight="size")
    .label(y="Total patrons", x="day_of_week")
    # .show()
)

# facetgrid
tips = sns.load_dataset("tips")
g = sns.FacetGrid(data=tips)
g.map_dataframe(sns.histplot, x="tip")
g.set_xlabels("ss")
g.set_titles("dds")
g.refline(y=tips["tip"].mean())
g.tight_layout()

# scatter plot
sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
g = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", size="size", style="sex", )
