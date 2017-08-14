import json
import os

rootFolder = '<rootFolder without tail slash>'

def main():
	with open('data.json') as data_file:    
		data = json.load(data_file)

	for file in data:
		absPath = rootFolder + file[1]
		if not os.path.isfile(absPath):
			print "%s\t%s" % (file[0], absPath)
			(folderPath, fileName) = os.path.split(os.path.abspath(absPath))
			if not os.path.isdir(folderPath):
				os.mkdir(folderPath)
			os.system("drive download --path %s %s" % (folderPath, file[0]))


if __name__ == "__main__":
	main()