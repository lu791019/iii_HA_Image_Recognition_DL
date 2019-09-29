
:a
python test_frcnn.py -p CT_img
python producer_CT_recog.py
timeout /t 3

python img_upload.py

timeout /t 3
rd /s /q CT_img

goto a
