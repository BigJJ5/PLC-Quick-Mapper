HOW TO USE THESE PROGRAMS
-----------------------
v0.5
----------------
If Siemens is Slave, and AB is Master -
    1) Export AB Tag DB
    2) Save AB File as .L5K (optional)
    3) Export Siemens DB
    4) Run AB2RedLionTags.py
    5) Run Siemens2RedLionBlocks.py
    6) Connect AB PLC to DSP and import tags (or through L5K file)
    7) Quick map AB tags with abconversionINPUT.csv                             ---PART THAT SPEEDS UP PROCESS
    8) Import 2 new blocks in Siemens Slave (Crimson)
    9) Click Block 1, import mapping, and import "SiemensInputs.txt"
    10) Click Block 2, import mapping, and import "SiemensOutputs.txt"
    NOTE : IMPORTING MAPPING WILL NOT WORK IF FILE IS OPEN
If Siemens is Master, and AB is Slave-
    1) Export Siemens DB
    2) Import Data Tags from Siemens to AB                                      -???????????????????????
    2) Export AB DB
    3) Run Siemens2RedLionTags.py
    4) Run AB2RedLionBlocks.py
    5) Import tags from SiemensTags.csv                                         -????????????????????
    6) Quick map Siemens Tags with SiemensConversion.csv
    6) Import 2 new blocks in AB Slave (Crimson)
    7) Click Block 1, import mapping, and import "ABInputs.txt"
    8) Click Block 2, import mapping, and import "ABOutputs.txt" 