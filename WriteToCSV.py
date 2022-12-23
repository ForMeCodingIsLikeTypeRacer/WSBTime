class WriteToCSV:
    def append_to_csv(self,submission):
        with open('wsbnew.csv','a', encoding='utf-8-sig') as fd:
            fd.write('\n'+submission)