secretTalent = {'Jeff':'Is afraid of dogs.', 'David':'Plays the Piano.', 'Jason':'Can fly an airplane.'}
for keys in secretTalent:
    print(keys, ':', secretTalent[keys])

print(end='\n\n')

secretTalent['David'] = 'Plays the Harpsichord.'
secretTalent['Timotheé'] = 'Has amazing jawline.'

for keys in secretTalent:
    print(keys, ':', secretTalent[keys])

