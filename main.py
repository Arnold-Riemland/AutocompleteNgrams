from AutocompleteNgrams import AutocompleteNgrams

an = AutocompleteNgrams('1_gram.csv')

f = open('out.txt', 'w')
f.write(an.avl_tree.__repr__())
f.close()

find = an.get_k_possible_suggestions('color', 100)
print(*find[0], sep='\n')