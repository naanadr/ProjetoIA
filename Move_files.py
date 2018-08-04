import os
import random
import shutil

fetchdir_nod = "D:\\Bases\\Pulmao\\LUNA_raissa\\Luna_worked\\Cortes_png\\Nodule\\All"
fetchdir_nnod = "D:\\Bases\\Pulmao\\LUNA_raissa\\Luna_worked\\Cortes_png\\Nan_Nodule\\All"
outputdir = "D:\\Bases\\Pulmao\\LUNA_raissa\\Luna_worked\\5_fold\\"

for x in range(5):
	outputdir = "D:\\Bases\\Pulmao\\LUNA_raissa\\Luna_worked\\5_fold\\"
	outputdir = outputdir + str(x)+"fold\\"
	print outputdir
	for i in range(975):
		file = random.choice(os.listdir(fetchdir_nod))
		fileu = "nod."+file
		source = fetchdir_nod+"\\"+file
		destiny = outputdir+fileu
		
		
		shutil.move(source, destiny)
	for i in range (1416):
		file = random.choice(os.listdir(fetchdir_nnod))
		fileu = "nnod."+file
		source = fetchdir_nnod+"\\"+file
		destiny = outputdir+fileu
	

		shutil.move(source, destiny)
