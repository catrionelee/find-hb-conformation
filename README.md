# AlphaFold Hemoglobin State Finder Script

Small script to determine the conformational state of hemoglobin generated from predicted AlphaFold3 structures.

## Getting Prepared

### AlphaFold

You must create your structure prediction in the EXACT following way. It is important for later steps.

1. Peptide: ALPHA chain sequence, without Met (x2)
2. Peptide: BETA chain sequence, without Met (x2)
3. Ligand: HEM (x4)

You must save the 5 `.cif` structures somewhere you will remember. These will be named 0-4 as the suffix.

### Python and dependencies on your computer.

To use the script Catrione made, you must run the following in your shell/terminal.

1. ```
   pip install Bio
   ```

2.  ```
	pip install argparse
	```

<br>

## Running the State Script

You must supply the script 2 parameters, the input file `-i` , and the output file to store your results `-o`.

You may write the absolute path (`/a/path/to/a/file/like/this.cif`) or with a relative path (`file.cif`). If you write the relative path, it will only look in the current directory.

Example:
```
python hb_conform_finder.py -i /path/to/structure_0.cif -o my_structure_0.txt
```

This will create a file called `my_structure_0.txt` that will contain either `T-state`, `R-state`, `R2-state` or `ERROR`. If an error occurs, this was not a good Hb structure to determine its conformational state. Make sure to make a unique name for your output that you can recognize later (don't re-use the same filename).

If a large error occured, call Catrione... its a big fix.
