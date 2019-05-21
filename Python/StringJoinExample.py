venom=('Knull', 'Toxin', "Carnage")
single='|'.join(venom)
print(single)

DC = ['WonderWoman', 'Aquaman', 'Batman', 'Superman']
movies='||'.join(DC)
print(movies)


trends = {
    1: 'AI',
    2: 'Machine Learning',
    3: 'Serverless',
    4: 'ARVR'
}

picks='/'.join(trends.values())
print(picks)


list1=['1','2','3','4']

final_list='-'.join(list1)
print(final_list)


num_list=['1','2','3','4']
separator=','
final_num_list=separator.join(num_list)
print(final_num_list)

numTuple=('1','2','3','4')
separator=','
final_num_list=separator.join(numTuple)
print(final_num_list)

numset={'1','2','3'}
separator=','
final_num_set=separator.join(numset)
print(final_num_set)

