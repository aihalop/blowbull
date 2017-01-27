# Probabilitic model of the blowbull game

def factorial(n):
    '''return n!
    '''
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


def combination(k, n):
    '''return C_n^k
    '''
    return factorial(n) / (factorial(k) * factorial(n - k))

    
def binomial(k, n, p):
    '''pdf of binomail
    '''
    return combination(k, n) * (p**k) * ((1 - p)**(n - k))


def distribution(probabilities):
    '''
    '''
    return [sum(probabilities[:k]) for k in range(len(probabilities))]


def posterior_binomail(k, n, m, t):
    '''return P(B = m|A = k)
    '''
    return combination(m, k) * combination(t - m, n - k) / combination(t, n)


def probability_statement(k, n, m, t, p=1/6):
    '''return the probability that a statement is true

    k is the number said by someone
    n is the total amount of dices
    m is the known amount of the number
    t is the number given to each player
    '''
    all_probability = [posterior_binomail(i, n, m, t) * binomial(i, n, p) for i in range(n + 1)]
    return all_probability[k] / sum(all_probability)


if __name__=="__main__":
    import matplotlib.pyplot as plt
    n = 30
    t = 6
    m = 3
    index = range(t, n + 1)
    probs_without_posterior = [binomial(k, n, 1/6) for k in index]
    probs_with_posterior = [probability_statement(k, n, m, t) for k in index]
    

    plt.plot(index, distribution(probs_without_posterior), '-ro')
    plt.plot(index, distribution(probs_with_posterior), '-go')
    plt.legend(['totally unknown', 'known {m}'.format(m=m)])
    plt.show()
