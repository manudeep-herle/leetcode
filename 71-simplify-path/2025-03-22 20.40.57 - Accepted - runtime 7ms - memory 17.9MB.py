class Solution:
    def simplifyPath(self, path: str) -> str:
        # use stack - add dir names
        # traverse path
        # while loop when "." or "/"
        # if ".." pop if stack not empty
        stack = []
        p = 0
        name = ""
        while p < len(path):
            if path[p] == ".":
                dots = ""
                while p < len(path) and path[p] == ".":
                    p += 1
                    dots += "."
                if (p < len(path) and path[p] != "/") or name:
                    name += dots
                elif len(dots) == 2:
                    if stack:
                        stack.pop()
                elif len(dots) > 2:
                    name = dots
            elif path[p] == "/":
                if name: stack.append(name)
                name = ""
                while p < len(path) and path[p] == "/":
                    p += 1
            else:
                name += path[p]
                p += 1
        if name:
            stack.append(name)

        if not stack:
            return "/"

        output = ""
        for dir in stack:
            output += "/"
            output += dir
        
        return output
            
        

        