from flet import *
# INSTALL matplotlib WITH PIP IN YOU PC
import matplotlib
import matplotlib.pyplot as plt

# NOW FOR RANDOM COLOR IN YOU BAR CHART I USE RANDOM COLOR
import random
import matplotlib.colors as mcolors
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page:page):
	page.theme_mode = "light"

	# INPUT NAME AND SALARY
	nametxt = TextField(label="name")
	salarytxt = TextField(label="salary")
	fig,ax = plt.subplots()

	employee = []
	count = []
	bar_labels = []
	bar_colors = []
	ax.bar(employee,count,label=bar_labels,color=bar_colors)
	ax.set_ylabel("employee my data")
	ax.set_title("my all data employeee")
	ax.legend(title="employeee salary")



	# NOW CREATE DIALOG FOR SEE CHARTYOU
	chartdialog = AlertDialog(
		content=MatplotlibChart(fig,expand=True)
		)




	# CREATE TABLE 
	mytable = DataTable(
		columns=[
			DataColumn(Text("name")),
			DataColumn(Text("salary")),
			],
		rows=[]
		)


	def addnewdata(e):
		mytable.rows.append(
			DataRow(
				cells=[
				DataCell(Text(nametxt.value)),
				DataCell(Text(salarytxt.value)),
				]
				)
			)

		# NOW ADD NAME AND SALARY TO CHART
		employee.append(nametxt.value)
		count.append(salarytxt.value)

		# NOW FOR COLOR BAR FOR RANDOM CHOICE
		colors = ['purple','red','pink','green','blue','orange']
		bar_random_color = random.choice(colors)
		bar_labels.append(bar_random_color)


		# NOW ADD COLOR TO BAR
		mycolor = mcolors.to_rgba("tab:" + bar_random_color  )
		bar_colors.append(mycolor)

		# NOW IF YOU CLICK ADD DATA AGAIN THEN 
		# CHART WILL CLEAR ALL THEN LOAD NEW CHART AGAIN
		# FROM YOU TABLE
		ax.clear()
		ax.bar(employee,count,label=bar_labels,color=bar_colors)
		ax.set_ylabel("employee my data")
		ax.set_title("my all data employeee")
		ax.legend(title="employeee salary")
		page.update()
		



		# SHOW SNACKBAR
		page.snack_bar = SnackBar(
			Text("success add",size=30),
			bgcolor="green"
			)
		page.snack_bar.open = True
		page.update()

	def openyouchart(e):
		page.dialog = chartdialog
		chartdialog.open = True
		page.update()		


	page.add(
	Text("Datatable to Chart",size=30,weight="bold"),
	nametxt,
	salarytxt,
	Row([
		ElevatedButton("add data",
			on_click=addnewdata
			),
		ElevatedButton("open chart",
			on_click=openyouchart
			),
		]),
	mytable

		)
flet.app(target=main)
