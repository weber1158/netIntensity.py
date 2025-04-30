# `netIntensity.py` - A Jython Script for DTSA-II

## About
[DTSA-II](https://www.cstl.nist.gov/div837/837.02/epq/dtsa2/index.html) is a GUI developed by NIST for analyzing x-ray spectra. The GUI is equipped with a command prompt that uses an implementation of Python 2 in Java (Jython) for scripting purposes.

`netIntensity.py` is a script written for DTSA-II that can bulk processes multiple spectra at a time and print the net intensities for the following mineral-forming elements: F, Na, Mg, Al, Si, P, S, Cl, K, Ca, Ti, Cr, Mn, and Fe. 

## How to use [(PDF)](https://github.com/user-attachments/files/19899223/How-to-Use.pdf)

You can run `netIntensity.py` on your computer by downloading the script and doing the following:
1. Open DTSA-II
2. Import one or more EDS spectral data files (.msa extension)
3. In the Command tab, type `ls()` and then execute the command with <kbd>CTRL+Enter</kbd>
    - This will print a table of all the loaded spectra. The table will have two columns: *Name* and *Spectrum*. The values in the *Name* column will be "s1", "s2", "s3", etc.
4. Click the Open button and navigate to the `netIntensity.py` file. Select the file and it should run automatically.

## Limitations
* Jython uses the depreciated Python 2 language, so be warned that if you want to make modifications to the script you will most likely need to consult some very old resources.
* Running `netIntensity.py` will print the results in the DTSA-II command window, but the results are not automatically saved as a delimited file. You will need to copy-paste the printed results into a spreadsheet and adjust the columns as needed, but this method is still **significantly** faster than manually typing the `peakIntegral` command for each element individually and for each spectrum individually.
* `netIntensity.py` always integrates the peaks for F, Na, Mg, Al, Si, P, S, Cl, K, Ca, Ti, Cr, Mn, and Fe. Therefore, the resulting net intensity for an element may be negative if the element itself is not present as a major peak in the spectrum. Unfortunately, you will need to manually set these values to zero whenever you transfer the results to a delimited spreadsheet file. 

## How to cite

**APA-like**

```tex
Weber, A. M. (2025). netIntensity.py (Version 0.1) [Software]. GitHub. https://github.com/weber1158/netIntensity.py
```

**BibTex**

```tex
@misc{weberNetIntensity2025,
    author = {Austin M. Weber},
    title = {netIntensity.py ({Version} 0.1) [{Software}]},
    year = {2025},
    url = {https://github.com/weber1158/netIntensity.py}
}
```