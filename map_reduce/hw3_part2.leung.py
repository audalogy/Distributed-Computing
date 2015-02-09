#Audrey Leung
#HW3 - Part 2
#Info 206

###
# Author Info: 
#     The code is originally created by Jim Blomo for his course: Data Mining and Analytics in Intelligent Business Services.
#     The code is simplified and modified by Derek Kuo, TA for I206 Fall 14 Class.
##/


from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper1_extract_user_business(self,_,record):
        """Taken a record, yield <user_id, business_id>"""
        yield [record['user_id'], record['business_id']]

    def reducer1_compile_businesses_under_user(self,user_id,business_ids):
        ###
        # TODO_1: compile businesses as a list of array under given user_id,
        # after remove duplicate business, yield <user_id, [business_ids]>
        ##/
        unique_businesses = list(set(business_ids))
        yield [user_id,unique_businesses]
    
    def mapper2_collect_businesses_under_user(self, user_id, business_ids):
        ###
        # TODO_2: collect all <user_id, business_ids> pair, map into the same 
        # Keyword LIST, yield <'LIST',[user_id, [business_ids]]>
        ##/     
        yield["LIST",[user_id,business_ids]]
    
    def reducer2_calculate_similarity(self,stat,user_business_ids):
        def jaccard_similarity(business_list1, business_list2):
            ###
            # TODO_3: Implement Jaccard Similarity here, output score should between 0 to 1
            ##/
            #numerator = words that appear in both lists
            in_common = len(list(set(business_list1).intersection(business_list2)))
            #denominator = all unique words
            whole_business_list = business_list1 + business_list2
            unique_business_list = len(list(set(whole_business_list)))
            #calculate ratio 
            jaccard_similarity = float(in_common) / float(unique_business_list)
            return jaccard_similarity
   
        ###
        # TODO_4: Calulate Jaccard, output the pair of users that have similarity over 0.5, 
        # yield <[user1,user2], similarity>
        ##/
        user_business_list = []   # declare a list object
        for user_id,business_ids in user_business_ids: # append all user_id, business_ids into the list
            user_business_list.append([user_id,business_ids])
        for pair in range(0, len(user_business_list)-1):
            for next_pair in range(pair+1, len(user_business_list)):
                business_list1 = user_business_list[pair][1]
                business_list2 = user_business_list[next_pair][1]
                score = jaccard_similarity(business_list1, business_list2)
                if score >= 0.5:
                    yield [[user_business_list[pair][0], user_business_list[next_pair][0]], score]


    def steps(self):
        return [
            self.mr(mapper=self.mapper1_extract_user_business, reducer=self.reducer1_compile_businesses_under_user),
            self.mr(mapper=self.mapper2_collect_businesses_under_user, reducer= self.reducer2_calculate_similarity),
        ]


if __name__ == '__main__':
    UserSimilarity.run()