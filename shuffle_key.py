# 1. Функция проверки простоты: is_prime(x: int) -> bool
def is_prime(x):
	not_prime = 0
	for j in (range(2,x//2)):
		if x%j == 0:
			not_prime=1
			break
	if 	not_prime == 0:	
		return True	
	
# 2. Функция генерации списка простых чисел: primes(count: int) -> List[int]
def primes(count: int):
	simple_list=[2]
	i=3
	while len(simple_list)<count:
		if is_prime(i):
			simple_list.append(i)
		i+=2
	return simple_list

#print(primes(1000))

# 3. Функция расчёта контрольной суммы: checksum(x: List[int]) -> int
def checksum(x):
	import random 
	random.seed(100)
	random.shuffle(x)
	check_sum=0
	for num in x:
		check_sum += num
		check_sum*=113
		check_sum%=10000007	
	return check_sum	

# 4. Функция, которая выполняет все требуемые действия и возвращает контрольную сумму результата pipeline() -> int
def pipeline():
	return checksum(primes(1000))


# 5. Основной блок, который печатает результат (можно оставить на верхнем уровне или разместить в main())
def main():
	print(pipeline())


if __name__ == 'main':
	main()

