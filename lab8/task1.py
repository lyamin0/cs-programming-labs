def is_valid_command(command):
    return command in ['0', '1', '2', 'exit']

def can_burn(power, fuel):
    return power <= fuel

def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    fuel -= power
    speed = speed + gravity - thrust_step * power
    height -= speed
    if speed < 0:
        speed = 0
    if height < 0:
        height = 0
    return height, speed, fuel

def get_status(height, speed, safe_speed=2):
    if height > 0:
        return 'В полете'
    elif height == 0 and speed <= safe_speed:
        return 'Посадка успешна'
    else:
        return 'Авария'

def format_state(height, speed, fuel):
    return f'Высота: {height} | Скорость: {speed} | Топливо: {fuel}'

def main():
    height = 40
    speed = 4
    fuel = 14
    gravity = 4
    thrust_step = 3
    print(format_state(height, speed, fuel))
    while True:
        command = input()
        if not is_valid_command(command):
            print('Ошибка команды')
            continue
        if command == 'exit':
            print('Полет прерван')
            break
        power = int(command)
        if not can_burn(power, fuel):
            print('Недостаточно топлива')
            continue
        height, speed, fuel = simulate_step(height, speed, fuel, power, gravity, thrust_step)
        print(format_state(height, speed, fuel))
        status = get_status(height, speed)
        if status != 'В полете':
            print(status)
            break

main()