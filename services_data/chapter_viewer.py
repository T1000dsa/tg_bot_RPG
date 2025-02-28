global_count = {'now':1}
def chapter_view(current:int=global_count.get('now')):
    return 'chapter_{key_0}'.format(key_0=current)