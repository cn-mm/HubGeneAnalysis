'''
Conserved Domain Search Using NCBI
'''

def prettyprintCDD(query):
  '''
  query: Q#x->GeneID | function | .. | ..
  '''
  ls = query.split('\t')
  print("Query No. ", ls[0].split('- >')[0])
  print("Gene ID:\t ", ls[0].split('- >')[1].split('|')[0])
  print("Hit type:\t ", ls[1])
  print("PSSM-ID:\t ", ls[2])
  print("Range:\t \t ", ls[3], "-",ls[4])
  print("E-Value:\t ", ls[5])
  print("Bitscore:\t ", ls[6])
  print("Accession:\t ", ls[7])
  print("Short name:\t ", ls[8])
  print("Incomplete:\t ", ls[9])
  print("Superfamily:\t ", ls[10])


def parse_queries(filename):
  entry_id = 0
  with open(filename) as f:
    lines = f.readlines()
    for line in lines:
      ls = line.split('\t')
      if (int(ls[0].split('- >')[0].split('#')[-1]) + 2) == entry_id:
        print("{} {} \t".format(ls[7],ls[8]))
        continue
      entry_id = int(ls[0].split('- >')[0].split('#')[-1]) + 2
      print("#Q{}\t Gene ID: {},\n\t\t\t\t {} {}".format( int(ls[0].split('- >')[0].split('#')[-1]) + 2, ls[0].split('- >')[1].split('|')[0], ls[7],  ls[8]))
