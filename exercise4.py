class NameSpace:

    def __init__(self, name=None, parent=None):
        self.name = name
        self.parent = parent
        self.variable = []

    def add(self, var):
        self.variable.append(var)

    def get(self, var):
        if var in self.variable:
            return self.name
        return self.parent.get(var) if self.parent else "None"

l = []
scopes = {
    'global': NameSpace(name='global'),
}

for i in range(int(input())):
    command, namespace, scope = input().split()
    if command == "add":
        scopes[namespace].add(scope)
    elif command == "create":
        scopes[namespace] = NameSpace(name=namespace, parent=scopes[scope])
    elif command == "get":
        l.append(scopes[namespace].get(scope))

print(*l, sep='\n')
