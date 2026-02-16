class RandomizedSet(object): 
    

    def __init__(self):
        self.data_list=[]
        self.pos_dict={}
     

    def search(self,val):
        return val in self.pos_dict


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.search(val):
            return False

        
        self.pos_dict[val]=len(self.data_list)
        self.data_list.append(val)
        return True
        


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if  not self.search(val):
            return False

        index_of_element_to_remove=self.pos_dict[val]
        last_element=self.data_list[-1]
        self.data_list[index_of_element_to_remove]=last_element
        #r=self.data_list[item]=self.data_list[m]
        self.data_list.pop()

        self.pos_dict[last_element]=index_of_element_to_remove
        del self.pos_dict[val]
        return True

        
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
