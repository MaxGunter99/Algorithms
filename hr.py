def shortestSubstring(s):
    x = list(s)

    answer = [ ]

    for i in range( len( x ) ):

        if x[i] not in answer:
            answer.append( x[i] )

    print( answer )

    for i in range( len( x ) - 1 ):

        print( '------' )
        print( x[i] )
        print( x[i + 1:] )
    
shortestSubstring( 'aaabcce' )
shortestSubstring( 'bab' )