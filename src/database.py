class DB():
    def __init__(self, href):
        self.__href = href
        

    def Check_DB(self):
        db_file = "img.txt"
        try:
            open(db_file, 'r')
        except IOError:
            open(db_file, 'w')
        
        with open(db_file,'r') as reader:
            for line in reader.readlines():
                if line.strip()in[self.__href]:
                    print("Img in DB")
                    return False
        with open(db_file,'a') as a_writer:
            a_writer.write('\n'+self.__href)
            print("Img has been added to DB")
            return True
                
        
