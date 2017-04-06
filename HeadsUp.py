import random
import turtle

def main():
	
	head_count = 0
	tail_count = 0
	

	wn = turtle.Screen()

	for i in range(10000):
		number = random.randrange(0,2)
		Heads = turtle.Turtle()
		if number == 0:
			head_count +=.1
			Heads.speed(0)
			Heads.left(90)
			Heads.forward(head_count)
			Heads.left(90)
			Heads.forward(50)
			Heads.left(90)
			Heads.forward(head_count)
			Heads.left(90)
			Heads.forward(50)

		if number == 1:
			tail_count += .1
			Tails = turtle.Turtle()
			Tails.penup()
			Tails.goto(-50,0)
			Tails.pendown()
			Tails.speed(0)
			Tails.left(90)
			Tails.forward(tail_count)
			Tails.left(90)
			Tails.forward(50)
			Tails.left(90)
			Tails.forward(tail_count)
			Tails.left(90)
			Tails.forward(50)
	wn.exitonclick()
		


			

	print head_count
	print tail_count


main()