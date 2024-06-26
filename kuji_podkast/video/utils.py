def pluralize_comments(count):
    if 11 <= count % 100 <= 19:
        return 'комментариев'
    elif count % 10 == 1:
        return 'комментарий'
    elif 2 <= count % 10 <= 4:
        return 'комментария'
    else:
        return 'комментариев'

