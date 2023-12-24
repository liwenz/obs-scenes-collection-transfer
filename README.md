# obs-scenes-collection-transfer
obs is Open Broadcaster Software(https://obsproject.com/)

This software help transfer scene collection from A to B, and let it run.

It list all the source file: folder and file name by the export scene collection file.Then you copy all the files to a new folder,eg:c:\church.

The software also change the new point to the new folder, eg c:\church

Usage: 
python obs-scenescollection.py source-scene-collection-filename dest-folder dest-scene-collection-filename

At first: mkdir c:\church

eg python obs-scenescollection.py \jupyter\tcmc.json c:\church tcmc2.json

Then:
C:\python>python obs-scenescollection.py \jupyter\tcmc.json
from:  \jupyter\tcmc.json

C:/Users/Dmatt/Downloads 主祷文  The Lord's Prayer.mp4

C:/Users/Dmatt/Documents/Worship/video countdown60digital.mp4

C:/Users/Dmatt/Documents/Worship/video 国语堂主日崇拜 AUG.mp4

C:/Users/Dmatt/Documents/Worship/songs WhatafriendJesus.mp4

C:/Users/Dmatt/Pictures/Video Projects back yart project 1.mp4

C:/Users/rkhoo/Videos/Captures 2020-07-19 12-22-53.mkv

C:/Users/Dmatt/Downloads 2021-01-23 19-35-18.mkv

C:/Users/Dmatt/Downloads 0.Opening Music Before Worship - Doxology - Solo Piano Instrumental Hymn - Eric Schrotenboer.webm

C:/Users/Dmatt/Downloads Rock Of Ages (Instrumeantal).mp4

C:/Users/Dmatt/Downloads Rock Of Ages (Instrumeantal).mp4

C:/Users/Dmatt/Documents/Worship/video 国语堂主日崇拜 (1).mp4

C:/Users/rkhoo/Documents/Worship/video videoplayback (6).mp4

C:/Users/Dmatt/Documents/Worship/songs Because He Lives 살아 계신주 - Jennifer Jeon 제니퍼 전(영은).mp3

C:/church X2Download.app-【讓讚美飛揚  Let Praise Arise 古典版】官方歌詞版MV (Official Lyrics MV) - 讚美之泉敬拜讚美 (1).mp4

C:/church X2Download.app-【信靠每一句應許 Trusting in Your Promises】官方歌詞版MV (Official Lyrics MV) - 讚美之泉敬拜讚 美 (22).mp4

C:/church X2Download.app-再次將我更新 _ 小羊詩歌《再次將我更新》專輯.mp4

C:/church X2Download.app-勝過萬有-盛曉玫(幸福).mp4

C:/Users/Dmatt/Downloads 每一天 Day By Day  _ 台北靈糧堂雅音詩班 (1).mp4

copy all the files to c:\church

in obs menu: scene collection->Import 

the  file is c:\church\tcmc2.json

Then it's ok
