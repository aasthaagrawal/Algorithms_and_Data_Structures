#https://leetcode.com/problems/validate-ip-address/
#Complexity = O(N) time and O(1) space

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.isIPv4(IP):
            return "IPv4"
        elif self.isIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
    
    def isIPv4(self, IP):
        ip = IP.split(".")
        if len(ip) != 4:
            return False
        for i in ip:
            if not i.isdigit():
                return False
            int_i = int(i)
            if int_i < 0 or int_i >255:
                return False
            if len(i) > 1 and i[0] == "0":
                return False
        return True
    
    def isIPv6(self, IP):
        ip = IP.split(":")
        if len(ip) != 8:
            return False
        for i in ip:
            if len(i)<1 or len(i)>4:
                return False
            for c in i:
                c = ord(c)
                if c<48 or (57<c and c<65) or (70<c and c<97) or c>102:
                    return False
        return True
