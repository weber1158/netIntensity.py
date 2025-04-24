#This script calculates and prints the net intensity
#values of each EDS spectrum in DTSA-II. In particular,
#it calculates the net intensities of the 14 most
#common mineral-forming elements; the same elements
#that are used in the EDS Classification algorithms
#by Weber (2025).
#
# Copyright 2025 Austin M. Weber
#
#How to use:
# 1. Open DTSA-II
# 2. Import one or more EDS spectral data files (.msa)
# 3. In the Command tab, type `ls()` then CTRL+Enter
# 4. A table of all spectra will be printed. The table
#    will have two columns: Name and Spectrum. The values
#    in the Name column will be "s1", "s2", "s3", etc.
# 5. Click the Open button and navigate to the 
#    `netIntensity.py` file and then open it. The script
#    should run automatically without errors (assuming 
#    that you have fewer than 255 spectra open in the
#    application).
# 6. Copy-paste the ouput into Excel or another spreadsheet
#    program. You will need to use the Data>Text to Columns
#    tool in order to separate the elements from the data, 
#    and the main data from the error estimates (the error
#    estimates will follow the +/- sign). 
#
#Limitations:
# This script does not work when there are more than 255
# spectra open in DTSA-II, but this can be adjusted by up-
# dating the range in the first line of code to whatever
# you want. | Secondly, this script is written in Python 2
# because DTSA-II is not integrated with Python 3. If you 
# are to make any modifications, you may need to consult 
# some very old resources to ensure that your modifications
# will work. | Third, often times the integrated areas for
# certain elements will be negative. You will need to change
# these values to zeros before processing the data.
#
#Example output:
#  Running C:/User/Desktop/DTSA-II/Spectra/netIntensity.py
#  Results for s1:
#  F: -1264.7106660345307 +/- 339.81691045633244
#  Na: 151514.4594755366 +/- 711.1105681000709
#  Mg: -1939.0 +/- 609.087568964157
#  Al: 254548.0693810525 +/- 853.8164509258012
#  Si: 743199.7909370344 +/- 1281.7793546791888
#  P: -18780.192521293822 +/- 902.9392631005135
#  S: 15430.477216293402 +/- 489.4995977895619
#  Cl: -5642.627922910473 +/- 242.455420647977
#  K: -8130.725621301135 +/- 346.42704252123525
#  Ca: -2379.887801308727 +/- 274.7477675357197
#  Ti: 391.09707488713684 +/- 122.01525623073252
#  Cr: -111.20914266257387 +/- 120.26536440032089
#  Mn: 242.18039957582914 +/- 105.40462267324303
#  Fe: 276.1589262191428 +/- 119.48766595493062
#  () ...
#
#References
# DTSA-II. https://www.cstl.nist.gov/div837/837.02/epq/dtsa2/index.html
# Weber, A. M. Algorithms for SEM-EDS Mineral Dust Classification. Journal of Open Source Software 10, 7533 (2025).

# Generate list of spectrum names from "s1" to "s255"
spectrum_names = ["s{}".format(i) for i in range(1, 256)]

# Function to process each spectrum
def process_spectrum(spectrum, name):
    F  = spectrum.peakIntegral(658, 780)
    Na = spectrum.peakIntegral(974, 1096)
    Mg = spectrum.peakIntegral(1179, 1364)
    Al = spectrum.peakIntegral(1382, 1614)
    Si = spectrum.peakIntegral(1614, 1912)
    P  = spectrum.peakIntegral(1880, 2156)
    S  = spectrum.peakIntegral(2205, 2424)
    Cl = spectrum.peakIntegral(2503, 2741)
    K  = spectrum.peakIntegral(3210, 3435)
    Ca = spectrum.peakIntegral(3563, 3839)
    Ti = spectrum.peakIntegral(4404, 4620)
    Cr = spectrum.peakIntegral(5289, 5566)
    Mn = spectrum.peakIntegral(5771, 6024)
    Fe = spectrum.peakIntegral(6224, 6590)

    print("Results for {}:".format(name))
    print("F: {}".format(F))
    print("Na: {}".format(Na))
    print("Mg: {}".format(Mg))
    print("Al: {}".format(Al))
    print("Si: {}".format(Si))
    print("P: {}".format(P))
    print("S: {}".format(S))
    print("Cl: {}".format(Cl))
    print("K: {}".format(K))
    print("Ca: {}".format(Ca))
    print("Ti: {}".format(Ti))
    print("Cr: {}".format(Cr))
    print("Mn: {}".format(Mn))
    print("Fe: {}".format(Fe))
    print()

# Iterate over the spectrum names and process each one
for name in spectrum_names:
    if name in globals():
        process_spectrum(globals()[name], name)