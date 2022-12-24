class WriteToTxt:
    def append_to_txt(self,submission):
        with open('wsbnew.txt','a', encoding='utf-8-sig') as fd:
            fd.write('\n'+submission)