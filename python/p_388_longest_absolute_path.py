class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        split_input = input.splitlines()
        depth = 0
        max_length = 0
        depth_length = {0:0}
       
        for i in split_input:
            length = 0

            depth = i.count("\t")
            stripped_i = i.strip("\t")
        
            if "." in i:
                length = depth_length[depth] + len(stripped_i) + depth
                if length > max_length:
                    max_length = length
            else:
                length = depth_length[depth] + len(stripped_i)
                depth_length[depth+1] = length
                
        return max_length

def run_test_cases():
    test_cases = [
        "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
        "dir\n    file.txt",
        "dir\n        file.txt",
    ]

    s = Solution()
    for test in test_cases:
        print(s.lengthLongestPath(test))