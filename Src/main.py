import function_1
import keyboard

if __name__ == '__main__':
    if function_1.hello():
        print('work')
    if keyboard.read_key() == 'down':
        function_1.down_move()
    elif keyboard.read_key() == 'left':
        function_1.left_move()
    elif keyboard.read_key() == 'right':
        function_1.right_move()
    elif keyboard.read_key() == 'up':
        function_1.up_move()
