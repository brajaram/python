from timer import Timer


if __name__ == '__main__':
    """
    simple program to find elapsed time of join and native concatenation
    """
    ingredients="Orange,Ginger,Honey"    

    with Timer() as t:
        s1 = ','.join([ '(ings' + str(idx) + ":ingredient{name:'" + ing + "'})" for idx,ing in enumerate(ingredients.split(','))])
        s2 = ' and '.join([ '(ings' + str(idx) + ") <- [:CONTAINS] - (d)" for idx,_ in enumerate(ingredients.split(','))])
    t1 = t.secs
        
    with Timer() as t:
        s1 = s2 = ""
        for idx,ing in enumerate(ingredients.split(',')):
            s1 += '(ings' + str(idx) + ":ingredient{name:'" + ing + "'}) , "
            s2 += '(ings' + str(idx) + ") <- [:CONTAINS] - (d) and "
        s1 = s1[:-2]
        s2 = s2[:-4]
    t2 = t.secs

    print(t1,t2)
    print(t1>t2)

        

