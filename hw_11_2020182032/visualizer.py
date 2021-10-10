import turtle

scale = 450   # 새로 1080 모니터일 때 -450~450 값 나오도록

def setup(cities):  # 최대, 최소 값을 각각 구한다.
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
  diff_x = max_x - min_x  # 최대와 최솟값이 얼마나 차이나는지
  diff_y = max_y - min_y

def xy_to_screen(x, y):   # 화면 적당한 곳에 표시되도록. -450~450 사이 좌표로 변환
  dx, dy = x - min_x, y - min_y
  return dx / diff_x * scale * 2 - scale, dy / diff_y * scale * 2 - scale

def city_to_screen(city):
  return xy_to_screen(city.x, city.y)

def draw_city(city):    # 그림 그린다
  # print(city.__dict__)
  x, y = city_to_screen(city)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  # turtle.circle(5)
  turtle.color('gray')
  turtle.stamp()
  turtle.color('black') 
  turtle.write(city.name)

def draw_title(title, dy = 0):
  turtle.penup()
  turtle.goto(-scale, scale + dy)
  turtle.pendown()
  turtle.color('black')
  turtle.write(title)

def draw_edge(c, t, dist = False):
  turtle.penup()
  turtle.goto(city_to_screen(c))
  turtle.pendown()
  turtle.color('green')
  turtle.goto(city_to_screen(t))

  if not dist : return 
  dx, dy = t.x - c.x, t.y - c.y
  turtle.penup()
  turtle.goto(xy_to_screen(c.x + dx/2, c.y + dy/2))
  turtle.pendown()
  turtle.color('blue')
  turtle.write(str(dist))

def wait():
  turtle.exitonclick()

if __name__ == '__main__':
  from city import cities
  setup(cities)
  draw_title('All Cities')
  for city in cities:
    draw_city(city)
  draw_edge(cities[20], cities[30])
  draw_edge(cities[10], cities[30], 1234)
  wait()

