# cv-people-detector
A project for detecting people in video data.

## Background 
Have you ever wondered how people move around your city? Do you want to measure the foot traffic in front of your store? How about how often certain areas of a public park is used? That is the question we proposed in the beginning of this project. We were tasked to tally the patrons and the areas that were most commonly used in Weequahic park. With this data, park managers can address requests for additional facilities and better manage resources.

In the first phase of this project, we chose to use an urban intelligence platform called Placemeter. It uses video information to quantify pedestrian, cyclist and vehicle movement. As a first step, we chose to measure the traffic of the jungle gym right below the fieldhouse.

In the second phase of this project, we will be developing software for detecting people from video feeds. This could be used to count how many people use walking paths, sports fields, or tracks. 

## Progress from phase I
We used Placemeter to moniter the traffic at the Weequahic park jungle gym for a month (August). We collected the resulting data into a Google fusion table. Just for fun we compared the number of people walking through the jungle gym area to the daily temperature. Our results below seem to suggest fewer people go to the park when it's hot out.
![plot of people at park](https://github.com/davidruffner/cv-people-detector/blob/master/resources/wpaData.png?raw=true)
The interative version of this plot can be found [here](https://fusiontables.google.com/embedviz?containerId=googft-gviz-canvas&q=select+col0%3E%3E0%2C+col2%3E%3E1%2C+col1%3E%3E0+from+1PwQxHhKM9-Hcp6hvVbiiqsbNKN6-nreYcVtAMkvz+order+by+col0%3E%3E0+asc&viz=GVIZ&t=AREA&rmax=250&uiversion=2&gco_forceIFrame=true&gco_hasLabelsColumn=true&gco_vAxes=%5B%7B%22title%22%3A%22Temperature+(deg+F)%22%2C+%22minValue%22%3Anull%2C+%22maxValue%22%3Anull%2C+%22useFormatFromData%22%3Atrue%2C+%22viewWindow%22%3A%7B%22max%22%3Anull%2C+%22min%22%3Anull%7D%2C+%22logScale%22%3Afalse%7D%2C%7B%22useFormatFromData%22%3Atrue%2C+%22viewWindow%22%3A%7B%22max%22%3Anull%2C+%22min%22%3Anull%7D%2C+%22minValue%22%3Anull%2C+%22maxValue%22%3Anull%2C+%22logScale%22%3Afalse%2C+%22title%22%3A%22People+count%22%7D%5D&gco_useFirstColumnAsDomain=true&gco_legacyScatterChartLabels=true&gco_isStacked=false&gco_booleanRole=certainty&gco_hAxis=%7B%22useFormatFromData%22%3Atrue%2C+%22viewWindow%22%3A%7B%22max%22%3Anull%2C+%22min%22%3Anull%7D%2C+%22minValue%22%3Anull%2C+%22maxValue%22%3Anull%2C+%22title%22%3A%22Day%22%7D&gco_legend=top&gco_series=%7B%220%22%3A%7B%22targetAxisIndex%22%3A1%7D%7D&gco_title=Weequahic+Playground+Traffic+versus+max+temperature+in+August&width=500&height=300)
from this Google fusion tables [spreadsheet](https://www.google.com/fusiontables/DataSource?docid=1PwQxHhKM9-Hcp6hvVbiiqsbNKN6-nreYcVtAMkvz).


## Beginnings of next phase
We have followed a [few](https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/) [blogs](http://www.codeproject.com/Articles/10248/Motion-Detection-Algorithms) to utilize some motion detection algorithms. Below is an image showing the detection of a walker using differences between frames and thresholding. We hope to implement more advanced algorithms soon...

![walker](https://github.com/davidruffner/cv-people-detector/blob/master/resources/frame71.png?raw=true)

## Under construction...

We are hoping that this will be a collaborative project
so we will try to structure it in a way that makes
it easy to contribute. Some ideas for making this happen:
  * Follow Hitchhiker's Guide to Python [on how to structure the project](http://docs.python-guide.org/en/latest/writing/structure/#structure-of-the-repository)
  * Document code and create tutorials
  * We used sphinx to generate [documentation pages](https://readthedocs.org/projects/cv-people-detector/) on Read-the-Docs.
