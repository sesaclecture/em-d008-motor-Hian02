# 문제 1.
#
# 서보모터 각도를 PWM pulse width 값으로 변환하세요.
#
# 0도   -> 500
# 90도  -> 1500
# 180도 -> 2500
def servo_angle_to_pulse_width(angle):
    angle = max(0, min(180, angle))
    pulse_width = 500 + (angle / 180) * (2500 - 500)
    return int(pulse_width)


# 문제 2.
#
# 부저로 출력할 음계 이름을 주파수 값으로 변환하세요.
#
# C4, D4, E4, F4, G4, A4, B4, C5 음계를 지원해야 합니다.
def note_to_frequency(note):
    frequencies = {
        "C4": 262,
        "D4": 294,
        "E4": 330,
        "F4": 349,
        "G4": 392,
        "A4": 440,
        "B4": 494,
        "C5": 523,
    }
    return frequencies.get(note, 0)


# 문제 3.
#
# 여러 개의 음계를 부저 주파수 리스트로 변환하세요.
def melody_to_frequencies(notes):
    frequencies = []
    for note in notes:
        frequencies.append(note_to_frequency(note))
    return frequencies


# 문제 4.
#
# 로봇 이동 방향 문자열을 ROS2 Twist 값으로 변환하세요.
#
# 반환값은 (linear_x, angular_z) 튜플입니다.
def direction_to_twist(direction):
    if direction == "forward":
        return (1.0, 0.0)
    elif direction == "backward":
        return (-1.0, 0.0)
    elif direction == "left":
        return (0.0, 1.0)
    elif direction == "right":
        return (0.0, -1.0)
    elif direction == "stop":
        return (0.0, 0.0)
    else:
        return (0.0, 0.0)


# 문제 5.
#
# ROS2 Twist 값을 좌우 바퀴 속도로 변환하세요.
#
# 반환값은 (left_speed, right_speed) 튜플입니다.
def twist_to_wheel_speed(linear_x, angular_z):
    left_speed = linear_x - angular_z
    right_speed = linear_x + angular_z
    left_speed *= 100
    right_speed *= 100
    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))
    return (int(left_speed), int(right_speed))