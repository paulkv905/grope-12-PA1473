import time
import pygame
import datetime
pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res, pygame.RESIZABLE)


# Load your background image
def button(buton_x_start, buton_x_stop, buton_y_start, buton_y_stop, r=0, g=0, b=0, text=" ", presed=False):
    mouse = pygame.mouse.get_pos()
    if (buton_x_start <= mouse[0] <= buton_x_start+buton_x_stop and
            buton_y_start <= mouse[1] <= buton_y_start + buton_y_stop) or presed:
        pygame.draw.rect(screen, (r//2, g//2, b//2),
                         [buton_x_start, buton_y_start, buton_x_stop, buton_y_stop],
                         border_radius=10)
    else:
        pygame.draw.rect(screen, (r, g, b),
                         [buton_x_start, buton_y_start, buton_x_stop, buton_y_stop])

    max_width = buton_x_stop - 10  # Adjust for padding
    max_height = buton_y_stop - 10  # Adjust for padding

    font_size_standard = min(max_width // len(text), max_height)  # Adjust font size to fit within button
    if font_size_standard <= 0:
        font_size_standard = 2

    font = pygame.font.SysFont('helvetica', font_size_standard)
    buton_text = font.render(text, True, (0, 0, 0))

    text_width, text_height = font.size(text)
    text_x = buton_x_start + (buton_x_stop - text_width) // 2
    text_y = buton_y_start + (buton_y_stop - text_height) // 2

    screen.blit(buton_text, (text_x, text_y))


def screen_funktion():
    background_image = pygame.image.load(
        "C:\\Users\\paulk\\Desktop\\images\\21303.png")  # Replace "background.jpg" with your image path
    width = screen.get_width()
    height = screen.get_height()
    background_image = pygame.transform.scale(background_image, (width, height))
    mouse = pygame.mouse.get_pos()
    times_tring = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    font = pygame.font.SysFont('helvetica', 32)
    time_text = font.render(times_tring, True, (0, 0, 0))


    quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop = (
        (width - (width // 8)),
        (width // 8),
        (height - (height // 20)),
        height // 20)

    senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop = (
        ((width//2) - (width // 8)//2),
        (width // 8),
        ((height//2) - (height // 8)//2),
        height // 8)

    up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop = (
        ((width//2) - (width // 8)//2),
        (width // 8),
        ((height // 2) - (height // 8) // 2) - (height // 8) - 5,
        height // 8)

    down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop = (
        ((width // 2) - (width // 8) // 2),
        (width // 8),
        ((height//2) + (height // 8)//2) + 5,
        (height // 8))

    left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop = (
        ((width // 2) - (width // 8) // 2) - (width // 8) - 5,
        (width // 8),
        ((height // 2) - (height // 8) // 2),
        height // 8)

    right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop = (
        ((width // 2) + (width // 8) // 2) + 5,
        (width // 8),
        ((height // 2) - (height // 8) // 2),
        height // 8)

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if (quit_buton_x_start <= mouse[0] <= width and
                    quit_buton_y_start <= mouse[1] <= height):
                pygame.quit()
                exit()

            elif (senter_buton_x_start <= mouse[0] <= senter_buton_x_start+senter_buton_x_stop and
                  senter_buton_y_start <= mouse[1] <= senter_buton_y_start + senter_buton_y_stop):
                print("centerbuton presed")

            elif (up_buton_x_start <= mouse[0] <= up_buton_x_start+up_buton_x_stop and
                  up_buton_y_start <= mouse[1] <= up_buton_y_start + up_buton_y_stop):
                print("up")
            elif (down_buton_x_start <= mouse[0] <= down_buton_x_start+down_buton_x_stop and
                  down_buton_y_start <= mouse[1] <= down_buton_y_start + down_buton_y_stop):
                print("down")
            elif (left_buton_x_start <= mouse[0] <= left_buton_x_start+left_buton_x_stop and
                  left_buton_y_start <= mouse[1] <= left_buton_y_start + left_buton_y_stop):
                print("left")
            elif (right_buton_x_start <= mouse[0] <= right_buton_x_start+right_buton_x_stop and
                  right_buton_y_start <= mouse[1] <= right_buton_y_start + right_buton_y_stop):
                print("right")

        if ev.type == pygame.KEYDOWN:
            screen.blit(background_image, (0, 0))
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif ev.key == pygame.K_RETURN:
                button(quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop,
                       255, 0, 0, "QUIT")

                button(senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop,
                       175, 175, 175, presed=True)

                button(up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop,
                       175, 175, 175, text="▲")

                button(down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop,
                       175, 175, 175,
                       text="▼")

                button(left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop,
                       175, 175, 175,
                       text="◄")

                button(right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop,
                       175, 175, 175,
                       text="►")
                print("centerbuton presed")
            elif ev.key == pygame.K_w or ev.key == pygame.K_UP:
                button(quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop,
                       255, 0, 0, "QUIT")

                button(senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop,
                       175, 175, 175)

                button(up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop,
                       175, 175, 175, text="▲", presed=True)

                button(down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop,
                       175, 175, 175,
                       text="▼")

                button(left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop,
                       175, 175, 175,
                       text="◄")

                button(right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop,
                       175, 175, 175,
                       text="►")
                print("up")
            elif ev.key == pygame.K_s or ev.key == pygame.K_DOWN:
                button(quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop,
                       255, 0, 0, "QUIT")

                button(senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop,
                       175, 175, 175)

                button(up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop,
                       175, 175, 175, text="▲")

                button(down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop,
                       175, 175, 175,
                       text="▼", presed=True)

                button(left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop,
                       175, 175, 175,
                       text="◄")

                button(right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop,
                       175, 175, 175,
                       text="►")
                print("down")
            elif ev.key == pygame.K_a or ev.key == pygame.K_LEFT:
                button(quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop,
                       255, 0, 0, "QUIT")

                button(senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop,
                       175, 175, 175)

                button(up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop,
                       175, 175, 175, text="▲")

                button(down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop,
                       175, 175, 175,
                       text="▼")

                button(left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop,
                       175, 175, 175,
                       text="◄", presed=True)

                button(right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop,
                       175, 175, 175,
                       text="►")
                print("left")
            elif ev.key == pygame.K_d or ev.key == pygame.K_RIGHT:
                button(quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop,
                       255, 0, 0, "QUIT")

                button(senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop,
                       175, 175, 175)

                button(up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop,
                       175, 175, 175, text="▲")

                button(down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop,
                       175, 175, 175,
                       text="▼")

                button(left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop,
                       175, 175, 175,
                       text="◄")

                button(right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop,
                       175, 175, 175,
                       text="►", presed=True)
                print("right")
            else:
                button(quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop,
                       255, 0, 0, "QUIT")

                button(senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop,
                       175, 175, 175)

                button(up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop,
                       175, 175, 175, text="▲")

                button(down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop,
                       175, 175, 175,
                       text="▼")

                button(left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop,
                       175, 175, 175,
                       text="◄")

                button(right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop,
                       175, 175, 175,
                       text="►")

            pygame.display.update()
            time.sleep(0.1)

    # Blit the background image onto the screen
    screen.blit(background_image, (0, 0))
    screen.blit(time_text, (0, height-50))
    button(quit_buton_x_start, quit_buton_x_stop, quit_buton_y_start, quit_buton_y_stop, 255, 0, 0, "QUIT")
    button(senter_buton_x_start, senter_buton_x_stop, senter_buton_y_start, senter_buton_y_stop, 175, 175, 175)
    button(up_buton_x_start, up_buton_x_stop, up_buton_y_start, up_buton_y_stop, 175, 175, 175, text="▲")
    button(down_buton_x_start, down_buton_x_stop, down_buton_y_start, down_buton_y_stop, 175, 175, 175, text="▼")
    button(left_buton_x_start, left_buton_x_stop, left_buton_y_start, left_buton_y_stop, 175, 175, 175, text="◄")
    button(right_buton_x_start, right_buton_x_stop, right_buton_y_start, right_buton_y_stop, 175, 175, 175, text="►")

    # updates the frames of the game
    pygame.display.update()


while True:
    screen_funktion()
