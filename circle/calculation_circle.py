import math

def calculation_circle(diameter):
	try:
		diameter = int(diameter)
		#半径
		radius = diameter / 2
		#面積
		area = radius * radius * math.pi
		#円周
		circumference = diameter * math.pi
		
		return area, circumference
	except :
		return '数値を入力してください'
	
if __name__ == '__main__':
		input_num = input('input number : ')
		print(calculation_circle(input_num))