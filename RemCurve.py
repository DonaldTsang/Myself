rem266(n): # 256-bit
	m = n
	while n > ((1 << 266) - 1):
		m = 0
		while n != 0:
			m += n & ((1 << 266) - 1)
			n >>= a
			n *= 3
		n = m
	if m + 3 >= (1 << 266):
		return m + 3 - (1 << 266)
	return m

rem336(n): # 320-bit
	m = n
	while n > ((1 << 336) - 1):
		m = 0
		while n != 0:
			m += n & ((1 << 336) - 1)
			n >>= a
			n *= 3
		n = m
	if m + 3 >= (1 << 336):
		return m + 3 - (1 << 336)

rem452(n): # 448-bit
	m = n
	while n > ((1 << 452) - 1):
		m = 0
		while n != 0:
			m += n & ((1 << 452) - 1)
			n >>= a
			n *= 3
		n = m
	if m + 3 >= (1 << 452):
		return m + 3 - (1 << 452)
	return m

rem521(n): # 512-bit
	m = n
	while n > ((1 << 521) - 1):
		m = 0
		while n != 0:
			m += n & ((1 << 521) - 1)
			n >>= 521
			n *= 1
		n = m
	if m + 1 >= (1 << 521):
		return m + 1 - (1 << 521)
	return m

"""
unsigned int n;                      // numerator
const unsigned int s;                // s > 0
const unsigned int d = (1 << s) - 1; // so d is either 1, 3, 7, 15, 31, ...).
unsigned int m;                      // n % d goes here.

for (m = n; n > d; n = m)
{
  for (m = 0; n; n >>= s)
  {
    m += n & d;
  }
}
// Now m is a value from 0 to d, but since with modulus division
// we want m to be 0 when it is d.
m = m == d ? 0 : m;
"""
"""
322 - 11
324 - 23
336 - 3
338 - 15
369 - 25
379 - 19
383 - 31

389 - 21
401 - 31
413 - 21
414 - 17
444 - 17
"""
