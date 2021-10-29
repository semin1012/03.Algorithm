import turtle

scale = 450

edge_line_color = 'green'
edge_weight_color = 'blue'
city_circle_color = 'gray'
city_anno_color = 'brown'
city_name_color = 'black'

def setup(cities):
  turtle.speed(0)
  turtle.shape('circle')
  turtle.hideturtle()

  global min_x, min_y, max_x, max_y
  min_x, max_x = float('inf'), float('-inf')
  min_y, max_y = float('inf'), float('-inf')
  for c in cities:
    if min_x > c.x: min_x = c.x
    if min_y > c.y: min_y = c.y
    if max_x < c.x: max_x = c.x
    if max_y < c.y: max_y = c.y
  print('min:', (min_x, min_y), 'max:', (max_x, max_y))
  global diff_x, diff_y
  diff_x = max_x - min_x
  diff_y = max_y - min_y

def xy_to_screen(x, y):
  dx, dy = x - min_x, y - min_y
  return dx / diff_x * scale * 2 - scale, dy / diff_y * scale * 2 - scale

def city_to_screen(city):
  return xy_to_screen(city.x, city.y)

def draw_city(city):
  # print(city.__dict__)
  x, y = city_to_screen(city)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  # turtle.circle(5)
  turtle.color(city_circle_color)
  turtle.stamp()
  turtle.color(city_name_color)
  turtle.write(city.name)

def draw_city_annotation(city, dx, dy, str):
  # print(city.__dict__)
  x, y = city_to_screen(city)
  turtle.penup()
  turtle.goto(x + dx, y + dy)
  turtle.pendown()
  turtle.color(city_anno_color)
  turtle.write(str)

def draw_title(title, dy = 0):
  turtle.penup()
  turtle.goto(-scale, scale + dy)
  turtle.pendown()
  turtle.color(city_name_color)
  turtle.write(title)

def draw_edge(c, t, dist = False):
  turtle.penup()
  turtle.goto(city_to_screen(c))
  turtle.pendown()
  turtle.color(edge_line_color)
  turtle.goto(city_to_screen(t))

  if not dist: return
  dx, dy = t.x - c.x, t.y - c.y
  turtle.penup()
  turtle.goto(xy_to_screen(c.x + dx/2, c.y + dy/2))
  turtle.pendown()
  turtle.color(edge_weight_color)
  turtle.write(str(dist))

def wait():
  turtle.exitonclick()

if __name__ == '__main__':
  from city import cities
  setup(cities)
  draw_title('All Cities')
  for city in cities:
    draw_city(city)
    draw_city_annotation(city, 20, -15, len(city.name))
  draw_edge(cities[20], cities[30])
  draw_edge(cities[10], cities[30], 1234)
  wait()

