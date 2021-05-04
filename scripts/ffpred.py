'''
Uses REST API for FFPRED
Results on mail
'''

URL = 'http://bioinf.cs.ucl.ac.uk/psipred/api/submission.json'
def start_job(input_file, sub_name, email, selection = 'human'):    
    payload = {'input_data': input_file}
    data = {'job': 'ffpred',
            'submission_name': sub_name,
            'email': email,
           'ffpred_selection': selection}
    r = requests.post(URL, data=data, files=payload)
    print(r.text)

#NOTE: Once posted you will need to use the GET submission endpoint
#to retrieve your results. Polling the server about once every 2 or 5 mins
#should be sufficient.
#
# Full details at http://bioinf.cs.ucl.ac.uk/web_servers/web_services/

def process(inp):
    '''
    Helper function for getting sequence from fasta format
    '''
    inp = inp.strip()
    job_name = inp.split('|')[0][1:]
    inp = "".join(inp.split('\n')[1:])
    return inp, job_name

# i = 44
# while(sheet['B'+str(i)].value):
#     if sheet['F'+str(i)].value == 1:
#         inp = sheet['I'+str(i)].value
#         inp = inp.strip()
#         inp = "".join(inp.split('\n')[1:])
#         job_name = sheet['B'+str(i)].value
#         start_job(inp,job_name)
#     i+=1  