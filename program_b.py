import turtle

# -------------------------------------------------------------------------


def get_coords_and_check(name):
    x = int(input('enter x:'))
    y = int(input('enter y:'))

    if x > (500 - 420) or x < -500:
        print("WARNING: x-coordinate will place picture:" + name + " off of canvas.")
    if y > (400 - 324) or y < -400:
        print("WARNING: y-coordinate will place picture:" + name + " off of canvas.")

    return x, y


# Remove this
def draw_axis():
    turtle.goto(0, 400)
    turtle.pendown()
    turtle.goto(0, -400)
    turtle.penup()

    turtle.goto(500, 0)
    turtle.pendown()
    turtle.goto(-500, 0)
    turtle.penup()

# -------------------------------------------------------------------------

t = turtle.Screen()
t.setup(width=1000, height=800)
draw_axis()
turtle.penup()
turtle.speed(200)

# -------------------------------------------------------------------------

img_list = [
    {
        'img_name': 'sepia',
        'img_x_size': 360,
        'img_y_size': 298,
        'img_path': 'sepia.gif',
    },
    {
        'img_name': 'fRed',
        'img_x_size': 360,
        'img_y_size': 298,
        'img_path': 'fRed.gif',
    },
    {
        'img_name': 'fBlue',
        'img_x_size': 420,
        'img_y_size': 324,
        'img_path': 'fBlue.gif',
    },
    {
        'img_name': 'negated',
        'img_x_size': 420,
        'img_y_size': 324,
        'img_path': 'negated.gif',
    },
]

# -------------------------------------------------------------------------

for img_dict in img_list:
    img_path = img_dict['img_path']
    imgW = img_dict['img_x_size']
    imgH = img_dict['img_y_size']
    img_name = img_dict['img_name']

    x, y = get_coords_and_check(img_name)

    turtle.goto((x + (imgW // 2)), (y + (imgH // 2)))
    t.addshape(img_path)
    turtle.shape(img_path)
    turtle.write(img_path)
    turtle.stamp()    


# imgW = 360
# imgH = 298

# x, y = get_coords_and_check()

# turtle.goto((x + (imgW // 2)), (y + (imgH // 2)))
# t.addshape('sepia.gif')
# turtle.shape('sepia.gif')
# turtle.stamp()

# # -------------------------------------------------------------------------

# imgW = 360
# imgH = 298

# x, y = get_coords_and_check()

# turtle.goto((x + (imgW // 2)), (y + (imgH // 2)))
# t.addshape('fRed.gif')
# turtle.shape('fRed.gif')
# turtle.stamp()

# # -------------------------------------------------------------------------

# imgW = 420
# imgH = 324

# x, y = get_coords_and_check()

# turtle.goto((x + (imgW // 2)), (y + (imgH // 2)))
# t.addshape('fBlue.gif')
# turtle.shape('fBlue.gif')
# turtle.stamp()

# # -------------------------------------------------------------------------
# imgW = 420
# imgH = 324

# x, y = get_coords_and_check()

# turtle.goto((x + (imgW // 2)), (y + (imgH // 2)))
# t.addshape('negated.gif')
# turtle.shape('negated.gif')
# turtle.stamp()

# # -------------------------------------------------------------------------

print('DONE')

t.exitonclick()
