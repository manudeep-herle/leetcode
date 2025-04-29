class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # sort the folder list
        folder.sort()

        # is path2 subfolder of path1
        def isSubFolder(path1, path2):
            if len(path1) < len(path2):
                i = 0
                while i < len(path1) and path1[i] == path2[i]:
                    i += 1
                if path2[i] == "/":
                    return True
            return False

        res = ["/"]
        for path in folder:
            # compare path with res[-1]
            # if common prefix, skip path else add path to res
            if isSubFolder(res[-1], path):
                continue
            else:
                res.append(path)
        
        return res[1:]