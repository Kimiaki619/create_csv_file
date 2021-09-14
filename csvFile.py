import pandas as pd
import os
import shutil

#ラベルの保存をする
class label_csv():
	def __init__(self,path_label='image/',file_name='label'):
		self.path_label = path_label
		self.file_name = file_name
	def main(self,label_num=4):
		labels=[]
		for i in range(label_num):
			for path in os.listdir(self.path_label+str(i)):
				label = []
				label.append(path)
				label.append(i)
				labels.append(label)
		df = pd.DataFrame(labels)
		df.to_csv(self.file_name+".csv",index=False)
		

