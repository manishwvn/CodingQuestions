class Codec:
    
    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}
        self.base_url = "http://tinyurl.com/"
    
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encode_map:
            tinyUrl = self.base_url + str(len(self.encode_map) + 1)
            self.encode_map[longUrl] = tinyUrl
            self.decode_map[tinyUrl] = longUrl
        
        return self.encode_map[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.decode_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))