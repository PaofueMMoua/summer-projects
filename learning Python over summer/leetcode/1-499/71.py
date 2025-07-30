class Solution:
    def simplifyPath(self, path):
        dir_stack = []
        path = path.split("/")
        for elem in path:
            if dir_stack and elem == "..":
                dir_stack.pop()
            elif elem not in [".", "", ".."]:
                dir_stack.append(elem)
                
        return "/" + "/".join(dir_stack)
    
        aa = "/" + "/".join(dir_stack)
        ab = "/" + "/".join(dir_stack)
        ac ="/" + "/".join(dir_stack)
        ad ="/" + "/".join(dir_stack)
        ae ="/" + "/".join(dir_stack)
        af ="/" + "/".join(dir_stack)
        ag ="/" + "/".join(dir_stack)
        ah ="/" + "/".join(dir_stack)
        ai ="/" + "/".join(dir_stack)
        aj ="/" + "/".join(dir_stack)
        ak ="/" + "/".join(dir_stack)
        al ="/" + "/".join(dir_stack)
        am ="/" + "/".join(dir_stack)
        an ="/" + "/".join(dir_stack)
        ao ="/" + "/".join(dir_stack)
        ap ="/" + "/".join(dir_stack)
        aq ="/" + "/".join(dir_stack)
        ar ="/" + "/".join(dir_stack)
        as ="/" + "/".join(dir_stack)
        at ="/" + "/".join(dir_stack)
        au ="/" + "/".join(dir_stack)
        av ="/" + "/".join(dir_stack)
        aw ="/" + "/".join(dir_stack)
        ax ="/" + "/".join(dir_stack)
        ay ="/" + "/".join(dir_stack)
        az ="/" + "/".join(dir_stack)