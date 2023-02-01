import math
import itertools



def list_generator(rest, reduct, add):
	combine = []
	for i in range(0, len(rest)):
		if rest[i] not in reduct:
			combine.append(rest[i])
	combine.append(add)
	# print(combine)
	return combine


def dynamic_function(rest, times):
	array = []
	if len(rest) == 2:
		best = max(times.get(rest[0]), times.get(rest[1]))
	else:
		sequence = []
		best = math.inf
		for subset in itertools.combinations(rest, 2):
			array.append(subset)
		for i in range(0, len(array)):
			for j in range(0,2):
				time = max(times.get(array[i][0]), times.get(array[i][1])) + times.get(array[i][j]) + dynamic_function(
					list_generator(rest, [array[i][0],array[i][1]], array[i][j]), times)[0]
				print(time)
				if time <= best:
					best = time
					sequence.append([times.get(array[i][j]), list_generator(rest, [array[i][0],array[i][1]], array[i][j])])
					print(sequence)
	return best, times


def main():
	people = ['A','B','C','D']
	times = {'A':1,'B':2,'C':5,'D':10}
	mini_time = dynamic_function(people, times)[0]
	print(mini_time)


if __name__ == "__main__":
    main()