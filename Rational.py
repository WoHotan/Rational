class Rational:
	def __init__(self, num, den=1):
		if not isinstance(num, int) or not isinstance(den, int):
			raise TypeError
		if den == 0:
			raise ZeroDivisionError
		sign = 1
		if num < 0:
			num, sign = -num, -sign
		if den < 0:
			den, sign = -den, -sign
		g = Rational._gcd(num, den)
		self._num = sign * (num//g)
		self._den = den//g
	
	def num(self): return self._num

	def den(self): return self._den

	def plus(self, another):
		den = self.den * another.den
		num = (self.num * another.den
				+ self.den * another.num)
		return Rational(num, den)

	def print(self):
		print(str(self._num) + '/' + str(self._den))

	@staticmethod
	def _gcd(m, n):
		if n == 0:
			m, n = n, m
		while m != 0:
			m, n = n % m, m
		return n

	def __add__(self, another):
		den = self._den * another.den()
		num = (self._num  * another.den() + 
				self._den * another.num())
		return Rational(num, den)

	def __mul__(self, another):
		return Rational(self._num * another.den(), self._den * another.den())

	def __floordic__(self, another):
		if another.num() == 0:
			raise ZeroDivisionError
		return Rational(self._num * another.den(), self.den * another.num())

	def __str__(self):
		return str(self._num) + '/' + str(self._den)