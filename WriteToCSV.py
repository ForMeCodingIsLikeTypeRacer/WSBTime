class WriteToCSV:
    def append_to_csv(self,submission):
        with open('wsbnew.csv','a') as fd:
            fd.write('\n'+submission)