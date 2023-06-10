# python-graph
## About
This project implements a graphical interface for graphing mathematical functions or differential equations.<br>
The input of any mathematical expression **must be done in python syntax**.<br>
***This doesn't work***<br>
> 3x+4<br>
***This works***<br>
> 3\*x+4
## Mathematical expressions
You can use mathematical expressions included in numpy and the math library, such as sin() or cos(), just express them as np.sin() for example. <br>
This also works
> 2\*np.sin(x)\*\*2-3
## Installation
All the dependencies are listed in the `requirements.txt` file. To install them you can run this command inside a python virtual environment or install them globally if you prefer to do so.<br>
`pip install -r requirements.txt`<br>
### Database
By default, the project uses a MySql database hosted in db4free.net. The structure of the database is the following: https://dbdiagram.io/d/6484d783722eb77494be2299<br>
If you want to use your own database, either local or hosted, look for the following line in the main.py file and change it to your needs. The class that contains the connector structure can also be modified, as well as the queries needed.<br>
`connector = sql.SqlConnector("host", "user", "userPassword", "databaseName")`
