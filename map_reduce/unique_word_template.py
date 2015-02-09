###
# Author Info: 
#     The code is originally created by Jim Blomo for his course: Data Mining and Analytics in Intelligent Business Services.
#     The code is simplified and modified by Derek Kuo, TA for I206 Fall 14 Class.
##/



from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re

WORD_RE = re.compile(r"[\w']+")

class UniqueReview(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper1_extract_words(self, _, record):
        """Take in a record, yield <word, review_id>"""
            ###
            # TODO: for each word in the review, yield the correct key,value
            # pair:
            # for word in WORD_RE.findall(record['text']):
            #     yield [ ___ , ___ ]
            ##/

    def reducer1_count_reviews(self, word, review_ids):
        """Count the number of reviews a word has appeared in.  If it is a
        unique word (ie it has only been used in 1 review), output that review
        and 1 (the number of words that were unique)."""

        unique_reviews = set(review_ids)  # set() uniques an iterator
        ###
        # TODO: yield the correct pair when the desired condition is met:
        # if ___:
        #     yield [ ___ , ___ ]
        ##/

    def reducer2_count_unique_words(self, review_id, unique_word_counts):
        """Output the number of unique words for a given review_id"""
        ###
        # TODO: summarize unique_word_counts and output the result
        # 
        ##/

    def mapper3_aggregate_max(self, review_id, unique_word_count):
        """Group reviews/counts together by the MAX statistic."""
        ###
        # TODO: By yielding using the same keyword, all records will appear in
        # the same reducer:
        # yield ["MAX", [ ___ , ___]]
        ##/

    def reducer3_select_max(self, stat, count_review_ids):
        """Given a list of pairs: [count, review_id], select on the pair with
        the maximum count, and output the result."""
        ###
        # TODO: find the review with the highest count, yield the review_id and
        # the count. HINT: the max() function will compare pairs by the first
        # number
        #
        #/

    def steps(self):
        return [self.mr(self.mapper1_extract_words, self.reducer1_count_reviews),
                self.mr(reducer=self.reducer2_count_unique_words),
                self.mr(self.mapper3_aggregate_max, self.reducer3_select_max)]

if __name__ == '__main__':
    UniqueReview.run()