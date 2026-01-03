#design an algorithm to encode a list of strings to a single string and decode the single string back to the original list of strings.
# The encoded string is then sent over the network and is decoded back to the original list of strings.
# Example:
# Input: strs = ["hello","world"]
# Output: ["hello","world"]

class Codec:
 
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        #strs = ['bat', 'ball']
        res = ""
        for s in strs:
           res += str(len(s)) + "#" + s
        return res
    
    def decode(self, strs):
        #strs = 3#bat4#ball
        decoded_str = []
        i = 0

        while i < len(strs):
            j = i
            while strs[j] != '#':
                j+=1
            length = int(strs[i:j]) # it will only read the value of 'i' as the pound was right after it, and since it is a char, int will convert it to int. i.e. '3#'
            j +=1 # move past the '#' to the start of the string
            decoded_str.append(strs[j: j+length])  # extract the string of given length  from j while not including j+length i.e. bat in this case and ball in next iteration
            i = j + length # move i to the next length position
        return decoded_str
    
codec = Codec()
strs = ['bat', 'ball']
print(codec.encode(strs))
print(codec.decode(codec.encode(strs)))