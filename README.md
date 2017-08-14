# GDRive download helper
Just a little script to help me for downloading files via [gdrive](https://github.com/prasmussen/gdrive) without interrupted by Google API error.

# Origin
 
I used to have an ASUS's free quota for Google drive. But today, the quota was expired. I have to immidietly ~~~evacuate~~~ copy files to the another Google drive account. But :

- Google doesn't provide an easy option for copying the whole drive to another account.
- My dormitory's internet is suck! I can't make it done easily. :(
- I have a cloud server with very fast internet connection. But I can use via SSH only.
- `GDrive` CLI has no option for skip downloaded file.

So, I have to write this scripts in the middle of the night. 

# Usage

1. Download and install `[gdrive](https://github.com/prasmussen/gdrive)`. Don't forget to allow access by run `gdrive list` and follow the instruction. 
2. Get `folderID` from your drive. The easiest way is browse the folder in the browser. You'll see URL like this: `https://drive.google.com/drive/u/0/folders/<folderID>`.
3. Prepare folder in your local computer and get an absolute folder path.
4. Fill `<folderID>` in `ist_folders("<folderID>")` (line 23) in `gdrive_list_all.py` ***without parenthesis***.
5. Fill `<rootFolder without tail slash>` in `rootFolder = '<rootFolder without tail slash>'` (line 4) in `gdrive_download_check.py` ***without parenthesis***.
6. Run :
```shell
python gdrive_list_all.py
python gdrive_download_check.py
```

- `gdrive_list_all.py` will generate arrays of fileID and file path into `data.json`
- `gdrive_download_check.py` will read `data.json`, check whether file is existed. If not, it'll download files from your Google drive

