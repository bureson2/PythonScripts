def permutations(array):
    result = []
    if len(array) == 0: return [array]
    if len(array) == 1: return [array]
    for index in range(0,len(array)):
        leftFromIndex = array[:index]
        rightFromIndex = array[index+1:]
        withoutIndex = leftFromIndex + rightFromIndex
        for permutation in permutations(withoutIndex):
            preResult = [(array[index])]
            for i in permutation:
                preResult.append(i)
            result.append(preResult)
    return result
    
