dict = {'Name':  'Charlie', 'Age': '11', 'Classe': '5 Otaries'}
print("Name :",dict['Name'])

for a in ('Name','Age','Classe'):
	print(dict[a])

for k,v in dict.items():
	print(k,":",v)

print(dict)
print(dict.items())

dict['School']='Marie Clear'
print(dict['School'])

#del dict
