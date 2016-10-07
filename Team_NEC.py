def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if severely punished last time,
    else:
        return 'c' # otherwise collude. 