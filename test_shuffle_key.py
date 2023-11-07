'''
Реализуйте базовую задачу, реализуйте в отдельном файле test_*.py тесты на каждую
функцию базовой задачи: проверку простоты, генерацию списка (проверьте длину!),
расчёт контрольной суммы, полная обработка. (main проверять не нужно)
Скрипт-тест должен завершаться успешно, если все тесты пройдены и неуспешно,
если в какой-то из функций возникает ошибка.
'''
from shuffle_key import *

def test_is_prime():
	assert is_prime(7) == True
	assert is_prime(8) != True
	
def test_primes():
	assert len(primes(1000)) == 1000

	
def test_checksum():
	assert checksum(primes(1000)) == 7785816

def test_pipeline():
	assert pipeline() == 	7785816





test_is_prime()
test_primes()
test_checksum()
test_pipeline()
