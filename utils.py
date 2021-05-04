import openpyxl

def create_protein_seq_text_file(start, end, sheet, col_name, filename, option = 'a'):
  '''
  Creates a txt file for all protein sequences in FASTA format
  Input: Workbook sheet with FASTA Sequences in a column
  '''
    i = start
    blank = "\n"
    while(i<=end):
    try:
        txt = (sheet[col_name+str(i)].value)
        txt = txt.replace('"', '')
        with open(filename,option) as file:
            file.write(txt)
            file.write(blank)
    except:
        pass
    i+=1