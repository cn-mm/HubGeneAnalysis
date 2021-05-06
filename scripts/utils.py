import openpyxl
from matplotlib import pyplot as plt
import numpy as np

'''
WORKBOOK UTILITIES
'''
def get_sheet(workbook_path, sheet_name):
    '''
    Returns sheet
    '''
    wb = openpyxl.load_workbook(workbook_path)
    sheet = wb[sheet_name]
    return sheet

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

'''
DATA PLOTTING UTILITIES
'''

def plot_pie(categories, counts):
  '''
  Plots pie chart for categories and corresponding counts
  categories: list of fields
  counts: occurence corresponding to each field 
  '''
  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format
  plt.pie(counts, labels = categories, autopct = autopct_format(counts))  
  plt.show()