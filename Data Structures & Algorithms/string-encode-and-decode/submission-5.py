class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''
            
        encoded = ""
        for s in strs:
            length = len(s)
            encoded = encoded + str(length) + '#' + s
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        if s == '':
            return []

        decoded = []
        i = 0

        while i < len(s):
            length = []
            while s[i].isdigit():
                length.append(s[i])
                i += 1
            length = int("".join(length))

            decoded.append(s[i+1:i+length+1])
            i += length + 1

        return decoded
