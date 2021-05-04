'''
Open Plasmo DB for given gene from command line
Opens browser
Can also open sheets from an excel sheet
'''

import argparse
import webbrowser
import openpyxl
import re
import utils

def openPlasmoWeb(gene_name):
  '''
  Opens website
  '''
  webbrowser.open('https://plasmodb.org/plasmo/app/search?q=' + gene_name, new=2)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = 'Search PlasmoDB')
  parser.add_argument("--gene_name", metavar="G", required=True, type = str, help = "Please enter gene name")
  group = parser.add_argument_group('Using data from excel')
  group.add_argument("--sheets", metavar="S", default = False, type = bool, help = "Is the data from a sheet")
  group.add_argument("--workbook", metavar="WB", type = str, help = "Enter workbook path")
  group.add_argument("--sheet_name", metavar="SN", type = str, help = "Enter sheet name")
  group.add_argument("--column", metavar="C", default = "B", type = str, help = "Enter column name having gene names")
  group.add_argument("--lo", metavar="L", default = 1, type = int, help = "Gene count range low")
  group.add_argument("--hi", metavar="H", default = 11, type = int, help = "Gene count range high")
  args = parser.parse_args()

  gene_name = args.gene_name
  sheets = args.sheets

  if sheets == False:
    print("Opening plasmoDB for geneID " + gene_name)
    openPlasmoWeb(gene_name)
    exit(0)
  else:
    workbook_path = args.workbook
    sheet_name = args.sheet_name
    column = args.column
    low = args.lo
    high = args.hi

    # sheet = get_sheet(workbook_path, sheet_name)

    wb = openpyxl.load_workbook(workbook_path)
    sheet = wb[sheet_name]

    while (sheet[column+str(low)].value and lo<high):
      gene_name = sheet[column+str(low)].value
      openPlasmoWeb(gene_name)
      low +=1
    








