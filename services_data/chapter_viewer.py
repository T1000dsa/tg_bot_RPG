class New:
    data:int = 1
    def __init__(self):
        self.data = self.data

    def data_setter(self):
        self.data+=1
obj = New()
global_count = {'now':obj}
def chapter_view(current:New=global_count.get('now')):
    return 'chapter_{key_0}'.format(key_0=current.data)