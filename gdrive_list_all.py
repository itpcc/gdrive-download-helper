import os
import re
import json

result = []

def list_folders(folderId, folderPath = '/'):
	for line in os.popen('drive list --no-header --max 3000 --name-width 3000 --query " \'%s\' in parents"' % folderId).read().split('\n'):
		if len(line) > 1:
			fileMetaStr = line.decode('UTF-8')
			fileMeta = re.split(r'\s{2,}', fileMetaStr)
			# print fileMeta
			if(fileMeta[2] == 'dir'):
				nextFolderPath = folderPath + fileMeta[1] +'/'
				print "Going to: %s" % nextFolderPath
				list_folders(fileMeta[0], nextFolderPath)
			else:
				filePath = folderPath + fileMeta[1]
				print "File:     %s" % filePath
				result.append([fileMeta[0], filePath])

def main():
	list_folders("<folderID>")
	print result
	with open('data.json', 'w') as outfile:
		json.dump(result, outfile)


if __name__ == "__main__":
	main()