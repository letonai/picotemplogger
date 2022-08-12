# picotemplogger
(WIP) Log temperature to a Google Spreadsheet
<img width="1107" alt="image" src="https://user-images.githubusercontent.com/4183879/184264848-943e3fd0-b2f1-4d31-b9fb-6342958a687c.png">


You will need

. Raspeberry pi Pico W
. Pico Display
. Google Account

To setup the google spreadsheet

1. Login into you Google Drive account
2. Create a new Spreadsheet
3. Set te current sheet name to Temp
4. Set C1 value as 1
5. Create a new appScript:
<img width="758" alt="image" src="https://user-images.githubusercontent.com/4183879/184265540-3a8ed038-8055-4d8b-b733-ef8fcddb8c76.png">
6. Copy the code from `code.gs` to the code editor on AppScript
7. Deploy the code:
<img width="264" alt="image" src="https://user-images.githubusercontent.com/4183879/184265741-eab82cd1-1002-4a92-898b-4d1b7af87356.png">
7.1 Select type as WebApp:
<img width="651" alt="image" src="https://user-images.githubusercontent.com/4183879/184265797-8a5da5d2-45d0-4875-b1aa-f279c76f6c61.png">
7.2 Set Access as "Anyone"
<img width="772" alt="image" src="https://user-images.githubusercontent.com/4183879/184265979-0d4ef43e-d9e3-4735-9b70-14c8f066d34f.png">
7.3 Deploy the code
7.4 Copy the WebApp URL 
8. On the main.py set the variable sheetURL to the new URL from the WebApp
9. Set the wifi SSID and Password on main.py
10. Upload the code to the Raspberry pi pico

The Temperature will be logged every 5 min
