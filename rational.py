"""
					CSCI 503 - Assignment 4 - Spring 2019
					Progammer: Manoj Veluru
					Z-ID: Z1840907
					Section: 1
					Date Due: April 16, 2019
					Purpose: Rational Numbers
"""
import sys

''' A Simple RecursionMethod to calculate GCD of two numbers '''
def gcd(num,den):
		if den==0:
			return num
		else:
			return gcd(den, num%den)

''' Implementing a class for Rational Numbers'''			
class Rational:
	'''A Constructor method which creates a Rational number with numerator and denominator'''
	def __init__(self, num=0, den=1):
		GCD = gcd(num,den)
		num//=GCD
		den//=GCD
		self.num = num
		self.den = den
		self.value = num/den
	
	'''Overloading Arithmetic Operator add (+)'''
	def __add__(self,other):
		return Rational(self.num * other.den + self.den * other.num, self.den * other.den)
	
	'''Overloading Arithmetic Operator sub (-)'''
	def __sub__(self,other):
		return Rational(self.num * other.den - self.den * other.num, self.den * other.den)
	
	'''Overloading Arithmetic Operator mul (*)'''
	def __mul__(self,other):
		return Rational(self.num * other.num , self.den * other.den)
		
	'''Overloading Arithmetic Operator div (/)'''
	def __truediv__(self,other):
		return Rational(self.num * other.den , self.den * other.num)
		
	'''Overloading Negate Operator (-)'''
	def __neg__(self):
		return Rational(-self.num,self.den)
		
	'''Overloading Relational Operator equal (=)'''
	def __eq__(self,other):
		return self.num == other.num and self.den == other.den
	
	'''Overloading Relational Operator not equal (!=)'''
	def __ne__(self,other):
		return not self.num == other.num
	
	'''Overloading Relational Operator lessthan (<)'''
	def __lt__(self,other):
		return self.num * other.den < self.den*other.num
	
	'''Overloading Relational Operator lessthan or equal (<=)'''
	def __le__(self,other):
		return self.num * other.den <= self.den*other.num
	
	'''Overloading Relational Operator greater (>)'''
	def __gt__(self,other):
		return self.num * other.den > self.den*other.num
	
	'''Overloading Relational Operator greaterthan or equal (>=)'''
	def __ge__(self,other):
		return self.num * other.den >= self.den*other.num
	
	'''Overloading float operator'''
	def __float__(self):
		return self.num/self.den
	
	'''overloading str operator'''
	def __str__(self):
		if self.den == 1:
			return str(self.num)
		else:
			return str(self.num)+"/"+str(self.den)
	
	'''Overloading Operator (+=)'''
	def __iadd__(self,other):
		return Rational(self.num * other.den + self.den * other.num, self.den * other.den)
		
	'''Overloading Operator (-=)'''
	def __isub__(self,other):
		return Rational(self.num * other.den - self.den * other.num, self.den * other.den)
		
	'''Overloading Operator (*=)'''
	def __imul__(self,other):
		return Rational(self.num * other.num , self.den * other.den)
		
	'''Overloading Operator (/=)'''	
	def __idiv__(self,other):
		return Rational(self.num * other.den , self.den * other.num)
	
	'''Overloading readline function from sys'''
	def read():
		for line in sys.stdin:
			line = line.strip()
			l=line.split() 
			'''Splitting every line and checking the given number is a rational number or not'''
			if len(l) ==3:
				if l[1] == '/':
					return Rational(int(l[0]),int(l[2]))
				else:
					sys.stderr.write ( "Error: invalid rational number: "+line+" \n" ) #if not rationalnumber printing error message to stderr
					return " "
			elif len(l)==1:
				if l[0].find('/') == 1:
					i = l[0].split('/')
					return Rational(int(i[0]),int(i[1]))						
				else:
					try:
						return Rational(int(l[0]))
					except:
						sys.stderr.write ( "Error: invalid rational number: "+line+"\n" )
						return " "
			else:	#if not rationalnumber printing error message to stderr
				try:
					r = Rational (line)
				except:
					sys.stderr.write ( "Error: invalid rational number: "+line+"\n" )
				return " "
				
		
