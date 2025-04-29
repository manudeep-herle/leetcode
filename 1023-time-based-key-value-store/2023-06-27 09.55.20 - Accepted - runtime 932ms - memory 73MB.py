class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key] = {"timestamps":[]}

        self.ds[key]["timestamps"].append(timestamp)
        self.ds[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.ds:
            return ""
            
        # Do binary search to find the correct prev timestamp
        timestamps = self.ds[key]["timestamps"]
        l,r = 0, len(timestamps) - 1
        def check(mid):
            if timestamps[mid] <= timestamp:
                if (mid + 1) < len(timestamps):
                    if timestamps[mid + 1] > timestamp:
                        return  True
                else: 
                    return  True
            
            return False

        while l <= r:
            mid = (l+r) // 2

            if check(mid):
                return self.ds[key][timestamps[mid]]

            if timestamps[mid] > timestamp:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)