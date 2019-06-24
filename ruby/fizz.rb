def fizzer(div:, str:)
  return lambda { |i| return str if (i % div).zero? }
end

fizzers = [
  fizzer(div: 3,  str: 'Fizz'),
  fizzer(div: 5,  str: 'Buzz'),
  fizzer(div: 10, str: 'Rezz'),
]

puts (1..30).map { |n|
  fizzers.map { |c| c.call(n) }.compact.reduce(:+) || n
}
