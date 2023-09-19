import matplotlib.pyplot as plt

#Glydril is water-based drilling fluid and the other one is oil-based)
OilBased = open("H-sand43-V0,5-test2.txt", "r")
WaterBased = open("GlyDril-H-Sand43-V0,5-test1.txt", "r")

#Row 
print("Data:")

Time_OBM = [] #Sec
DPT1_OBM = [] #mBar
DPT2_OBM = [] #mBar
Torque_OBM = [] #N/m
Density_OBM = [] #kg/m3
TankWeight_OBM = [] #kg
TempTank_OBM = [] #Deg C
FrqSandFeeder_OBM = [] #Hz
Flow_OBM = [] #m3/h
DPT4_OBM = [] #mBar
DPR1_OBM = [] #mBar
DPR2_OBM = [] #mBar
TestSectionW_OBM = [] #kg
SetPoint = []
RPM_OBM = [] #r per min
USL = [] #m/s

# Read the file and extract data
lines = OilBased.readlines()
for line in lines[9:]:  # Skip the first 7 rows
    columns = line.split()  # Assuming columns are separated by whitespace
    #if len(columns) >= 17:  # Make sure there are at least 17 columns in the 
    Time_OBM.append(columns[0])
    DPT1_OBM.append(columns[1])
    DPT2_OBM.append(columns[2])
    Torque_OBM.append(columns[4])
    Density_OBM.append(columns[5])
    TankWeight_OBM.append(columns[6])
    TempTank_OBM.append(columns[7])
    FrqSandFeeder_OBM.append(columns[8])
    Flow_OBM.append(columns[9])
    DPT4_OBM.append(columns[10])
    DPR1_OBM.append(columns[11])
    DPR2_OBM.append(columns[12])
    TestSectionW_OBM.append(columns[13])
    SetPoint.append(columns[14])
    USL.append(columns[15])
    RPM_OBM.append(columns[16])
    

#Plots

plt.plot(RPM_OBM, DPT1_OBM)
plt.xlabel('RPM')
plt.ylabel('DPT1') 
plt.title('RPM vs DPT1')
#Show the plot
plt.show()