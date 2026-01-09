#!/usr/bin/env python3

import Bio
from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.Residue import Residue
import argparse


# Define and fetch all arguments passed to the command line.
parser = argparse.ArgumentParser()
parser.add_argument("-i", type=str)
parser.add_argument("-o", type=str)
args = parser.parse_args()

# Create an MMCIFParser object
struc_parser = MMCIFParser(QUIET=True)

# Parse the mmCIF file. Using H_amp_01 model of HBA-T1 and HBB.
structure = struc_parser.get_structure("hemoglobin", args.i)


# Get distance between beta1-His146 and beta1-Asp94 acceptor and donor atoms.
b146His = structure[0]["C"][146]["NE2"]
b94Asp = structure[0]["C"][94]["OD1"]
b1_dist = float(b94Asp - b146His)


# Get distance between beta2-His146 and beta2-Asp94 acceptor and donor atoms.
b2_146His = structure[0]["D"][146]["NE2"]
b2_94Asp = structure[0]["D"][94]["OD1"]
b2_dist = float(b2_94Asp - b2_146His)




# Get distance between beta1-C-terminus and alpha2-Lys40 acceptor and donor atoms.
b_cterm = structure[0]["C"][146]["OXT"]
a40Lys = structure[0]["B"][40]["NZ"]
cterm_dist = float(b_cterm - a40Lys)

if cterm_dist > 30:
    a40Lys = structure[0]["A"][40]["NZ"]
    cterm_dist = float(b_cterm - a40Lys)


# Get distance between beta1-C-terminus and alpha2-Lys40 acceptor and donor atoms.
b2_cterm = structure[0]["D"][146]["OXT"]
a2_40Lys = structure[0]["A"][40]["NZ"]
cterm2_dist = float(b2_cterm - a2_40Lys)

if cterm2_dist > 30:
    a2_40Lys = structure[0]["B"][40]["NZ"]
    cterm2_dist = float(b2_cterm - a2_40Lys)



# Determine if salt bridges are present at beta1-His146 and beta1-Asp94.
if b1_dist < 6.1 or b2_dist < 6.1:
    beta_beta_bridge = True
else:
    beta_beta_bridge = False


# Determine if salt bridges are present at beta1-C-terminus and alpha2-Lys40.
if cterm_dist < 6.1 or cterm2_dist < 6.1:
    cterm_alpha_bridge = True
else:
    cterm_alpha_bridge = False



# Declare conformation state
if beta_beta_bridge:# and cterm_alpha_bridge:
    state = "T-state"
elif (beta_beta_bridge == False and cterm_alpha_bridge == False):
    if cterm_dist < 17.0 or cterm2_dist < 17.0:
        state = "R-state"
    elif cterm_dist >=17.0 or cterm2_dist >= 17.0:
        state = "R2-state"
else:
    "ERROR"


# Write state to txt file.
with open(args.o, "w") as outfile:
    outfile.write(str(state))
    outfile.close()