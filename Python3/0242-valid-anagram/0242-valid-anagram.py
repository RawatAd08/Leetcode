class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds={}
        for key in s:
            ds[key]=ds.get(key,0)+1
        dt={}
        for key in t:
            dt[key]=dt.get(key,0)+1

        for key in dt:
            if key  not in ds or dt[key]!=ds[key]:
                return False

        if len(ds)!=len(dt):
            return False
        return True