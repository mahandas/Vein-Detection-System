##############
##
##automation script
##
##############
Foldername=$(date "+%Y.%m.%d-%H.%M.%S")
python RaspberryPi_cam.py
python Processing.py
python OutputFEED.py
rm temp.jpg
rm out.jpg
cd VeinDetectionData
mkdir Foldername
cd ..
mv *.jpg VeinDetectionData/Foldername/
cd VeinDetectionData
mv Foldername $Foldername

