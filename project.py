from itertools import combinations
# using itetools
import codewars_test as test

def lcs(x, y):
	x1 = x.replace("", " ")
	y1 = y.replace("", " ")
	l1 = x1.split()
	l2 = y1.split()
	powerset1 = []
	powerset2 = []
	answer = ""
	#getting power set for 1st string
	for i in range(len(l1)+1):
		for e in combinations(l1,i):
			powerset1.append(e)

	for i in range(len(l2)+1):
		for e in combinations(l2,i):
			powerset2.append(e)

	# now comparing the power sets
	comman_list = []
	for i in powerset1:
		for e in powerset2:
			if(i == e):
				comman_list.append(e)

	for i in comman_list[-1]:
		answer += i

	return answer
#print(lcs("anothertest", "notatest"))


def test_case():
	test.assert_equals(lcs("", ""), "")
	test.assert_equals(lcs("abc", ""), "")
	test.assert_equals(lcs("", "abc"), "")
	test.assert_equals(lcs("a", "b"), "")
	test.assert_equals(lcs("a", "a"), "a")
	test.assert_equals(lcs("abc", "a"), "a")
	test.assert_equals(lcs("abc", "ac"), "ac")
	test.assert_equals(lcs("abcdef", "abc"), "abc")
	test.assert_equals(lcs("abcdef", "acf"), "acf")
	test.assert_equals(lcs("anothertest", "notatest"), "nottest")
	test.assert_equals(lcs("132535365", "123456789"), "12356")
	test.assert_equals(lcs("nothardlythefinaltest", "zzzfinallyzzz"), "final")
	test.assert_equals(lcs("abcdefghijklmnopq", "apcdefghijklmnobq"), "acdefghijklmnoq")



