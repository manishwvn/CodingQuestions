class Solution:
    def checkIP4(self, add):
        ip = add.split(".")
        
        print(ip)
        
        for count in ip:
            
            if len(count) == 0 or len(count) > 3:
                return "Neither"
            
            if count[0] == "0" and len(count) != 1 or not count.isdigit() or int(count) > 255:
                return "Neither"
            
        return "IPv4"
        
        
    def checkIP6(self, add):
        ip = add.split(":")
        
        hexa = "0123456789abcdefABCDEF"
        
        for count in ip:
            if len(count) == 0 or len(count) > 4:
                return "Neither"
            
            for char in count:
                if char not in hexa: return "Neither"
                
        return "IPv6"
            
    def validIPAddress(self, queryIP: str) -> str:
    
        if queryIP.count('.') == 3:
            print("checking IP4")
            return self.checkIP4(queryIP)
            
        elif queryIP.count(':') == 7:
            print("checking IP6")
            return self.checkIP6(queryIP)
        
        else:
            return "Neither"