class Command:
    def __init__(self, line):
        self._title = line.split(":")[0].strip()
        self._link = []
        self._connection = ""
        for elem in line.split(":")[1].split():
            elem = elem.strip()
            if not elem:
                continue
            self._link.append(elem)

    def is_linked(self, dep):
        return (1 if dep in self._link else 0)

    def __repr__(self):
        return (self._title + ": " + " ".join(self._link))

    def __eq__(self, other):
        return (other == self._title)

    def set_connection(self, line):
        self._connection = line
    
    def get_connection(self):
        return (self._connection)