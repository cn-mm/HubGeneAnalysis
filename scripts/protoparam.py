'''
Runs expasy protoparam for files
# TODO: Add code for sheet
'''

import utils
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def expasy(filename):
    '''
    filename: txt file containing fasta sequences 
    Returns:
        list with:
        molecular weight (mol_wt)
        Isoelectric point (pI)
        Negative amino acid count (neg_aa_count)
        Positive amino acid count (pos_aa_count)
        Instability (instability)
        Aromaticity (aromaticity)
        Gravy (gravy)
        Secondary Structure Fractions (sec_str_frac)
    '''
    fin_list = []
    for i,seq_record in enumerate(SeqIO.parse(filename, "fasta")):
        my_seq = str(seq_record.seq)
        analysed_seq = ProteinAnalysis(my_seq)
        
        mol_wt = analysed_seq.molecular_weight() 
        pI= analysed_seq.isoelectric_point() 
        aa_dict = analysed_seq.count_amino_acids()
        neg_aa_count = aa_dict['D'] + aa_dict['E'] # (Asp + Glu)
        pos_aa_count = aa_dict['R'] + aa_dict['K']# (Arg + Lys)
        instability = analysed_seq.instability_index() 
        aromaticity = analysed_seq.aromaticity()
        flexibility = analysed_seq.flexibility()
        gravy = analysed_seq.gravy()
        sec_str_frac = analysed_seq.secondary_structure_fraction()
        ls = [seq_record.id, mol_wt, pI, neg_aa_count, pos_aa_count, instability, aromaticity, gravy, (sec_str_frac)]
        fin_list.append(ls)
        
    return fin_list

def prettyPrintExpasy(fin_list):
    '''
    Pretty preint Expasy protopram results
    '''
    for ls in fin_list:
        print("Sequence ID:", ls[0])
        print("Molecular Weight: {:.4f}".format(ls[1]))
        print("Isoelectric point: {:.4f}".format(ls[2]))
        print("Negative AA count: ", ls[3])
        print("Positive AA count: ", ls[4])
        print("Instability: {:.4f}".format(ls[5]))
        print("Aromaticity: {:.4f}".format(ls[6]))
        print("Gravy: {:.4f}".format(ls[7]))
        print("Secondary Structure Fraction: Helix {:.4f}; Turn {:.4f}; Sheet {:.4f}".format(ls[8][0], ls[8][1], ls[8][2]))
        print()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = 'Expasy Protoparam')
  parser.add_argument("--seq_file", metavar="F", required=True, type = str, help = "Enter file with FASTA sequences")
  args = parser.parse_args()

  seq_file = args.seq_file

  proto_list = expasy(seq_file)
  prettyPrintExpasy(proto_list)