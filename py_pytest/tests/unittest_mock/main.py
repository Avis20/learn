from unittest.mock import Mock

mock = Mock()
print(mock)
# <Mock id='140132775981360'>

print(mock.some_attribute)
print(mock.some_method())
# <Mock name='mock.some_attribute' id='140132775981504'>
# <Mock name='mock.some_method()' id='140132774461840'>

json = Mock()

json.loads({"key": "value"})

# Кол-во вызовов
print(json.loads.call_count)
# 1

# Последние аргументы вызова
print(json.loads.call_args)
# call({'key': 'value'})

# Список аргументов
print(json.loads.call_args_list)
# [call({'key': 'value'})]

