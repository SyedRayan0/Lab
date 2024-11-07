import turtle

# 1. Get the color based on the given character
def get_color(char):
    '''This function returns the the color corresponding to the given digit
    '''
    if char == '0':
        return 'black'
    elif char == '1':
        return 'white'
    elif char == '2':
        return 'red'
    elif char == '3':
        return 'yellow'
    elif char == '4':
        return 'orange'
    elif char == '5':
        return 'green'
    elif char == '6':
        return 'yellowgreen'
    elif char == '7':
        return 'sienna'
    elif char == '8':
        return 'tan'
    elif char == '9':
        return 'gray'
    elif char == 'A':
        return 'darkgray'
    else:
        return None

# 2. Draw a single colored pixel (square)
def draw_color_pixel(color_string, turta):
    '''This function draws a square of size 20 pixels and fills it with the given color
    '''
    if color_string:  # Check for valid color
        turta.fillcolor(color_string)
        turta.begin_fill()
        for i in range(4):
            turta.forward(20)
            turta.right(90)
        turta.end_fill()
        turta.forward(20)  # Move to the next position

# 3. Draw a pixel based on a character, using get_color
def draw_pixel(char, turta):
    '''This function gets a digit and finds the color corresponding to it through get_color() function
    and based on its validity it uses the draw_color_pixel() to draw the squares of that color
    '''
    color = get_color(char)
    if color:
        draw_color_pixel(color, turta)
    else:
        print("Invalid color code",char)

# 4. Draw a line of pixels from a string
def draw_line_from_string(color_string, turta):
    '''This function iterates over each character in the color string and checks if there is a color
    corresponding to that character
    '''
    for char in color_string:
        if get_color(char) is None:
            print("Stopping due to invalid color", char)
            return False  # Stop if invalid color encountered
        draw_pixel(char, turta)
    return True

# 5. Continuously draw shape from user input
def draw_shape_from_string(color_string,turta):
    '''This function ensures that they continuously ask input from the user and if
    an empty string is given then the loop should break
    '''
    while True:
        if color_string == "":
            break
        if not draw_line_from_string(color_string, turta):
            break

# 6. To draw a checkerboard
def draw_grid(turta):
    '''This function is for drawing a 20x20 checkerboard of black and red squares
    '''
    even_row = '02' * 10 
    odd_row = '20' * 10

    for row in range(20):
        if row % 2 == 0:
            draw_line_from_string(even_row,turta)
        else:
            draw_line_from_string(odd_row,turta)
        
        turta.penup()
        turta.goto(-200,turta.ycor()-20)
        turta.pendown

# 7. Filepath
def draw_shape_from_file(turta):
    '''This function asks the user for the filepath and draws colored squares based on the content 
    of the file
    '''
    filepath = input("Enter the path of the file: ")
    
    try:
        with open(filepath, 'r') as f:
            for line in f:
                color_string = line.strip()
                if not color_string:
                    continue

                if not draw_line_from_string(color_string, turta):  
                    print("Error drawing line:", color_string)
                    break

                # Move the turtle to the next line (new row)
                turta.penup()
                turta.goto(-200,turta.ycor() - 20)
                turta.pendown()

    except FileNotFoundError:
        print("File not found", filepath)


   