import os

import pygame

w, h = 600, 300
run = True

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((w, h))
bg = pygame.image.load("bg.png")
clock = pygame.time.Clock()
end = pygame.USEREVENT + 1
# font = pygame.font.Font(None, 24)
font = pygame.font.SysFont("Comfortaa", 69)
font_sub_title = pygame.font.SysFont("Comfortaa", 24)


class MyMixerSongsEpta:
    _current = 0
    _is_pause = False
    _songs = []

    def __init__(self) -> None:
        self._songs = os.listdir("musics")
        pygame.mixer.music.set_endevent(end)

    def play(self) -> None:

        if pygame.mixer.music.get_busy():
            print("Pause")
            self._is_pause = True
            pygame.mixer.music.pause()

        else:

            if self._is_pause:
                print("Unpause")
                self._is_pause = False
                pygame.mixer.music.unpause()

            else:
                print("Play")
                self._is_pause = False
                pygame.mixer.music.load("musics/" + self._songs[self._current])
                pygame.mixer.music.play()

    def stop(self) -> None:
        print("STOP")
        self._is_pause = False
        pygame.mixer.music.set_endevent(end - 1)
        pygame.mixer.music.stop()
        pygame.mixer.music.set_endevent(end)

    def next(self) -> None:
        print("Next")
        self._current += 1
        if self._current >= self._songs.__len__():
            self._current = 0
        self._is_pause = False
        pygame.mixer.music.load("musics/" + self._songs[self._current])
        pygame.mixer.music.play()

    def previous(self) -> None:
        print("Previous")
        self._current -= 1
        if self._current < 0:
            self._current = self._songs.__len__() - 1
        self._is_pause = False
        pygame.mixer.music.load("musics/" + self._songs[self._current])
        pygame.mixer.music.play()

    def get_current_song_name(self) -> str:
        return self._songs[self._current]


mixer = MyMixerSongsEpta()

title = font.render("MUSIC PLAYER", True, (0, 0, 0))
sub_title = font_sub_title.render("for control use", True, (0, 0, 0))
text_one = font_sub_title.render(
    "<F8>: stop <F9>: prev <F10>: play <F11>: next", True, (0, 0, 0)
)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("BYE BYE !")
            run = False
        if event.type == end:
            print("Music end, turn next on")
            mixer.next()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F9:
                mixer.stop()
            if event.key == pygame.K_F10:
                mixer.play()
            if event.key == pygame.K_F11:
                mixer.next()
            if event.key == pygame.K_F8:
                mixer.previous()

    screen.fill((255, 255, 255))
    screen.blit(bg,(0,0))
    # screen.blit(title, (w // 2 - title.get_width() // 2, 42))
    # screen.blit(
    #     sub_title, (w // 2 - sub_title.get_width() // 2, 69 + title.get_height())
    # )
    # screen.blit(
    #     text_one, (w // 2 - text_one.get_width() // 2, 110 + title.get_height())
    # )
    screen.blit(
        font_sub_title.render(mixer.get_current_song_name(), True, (255, 255, 255)),
        (w // 2 - 142, 150 + title.get_height() + 10),
    )

    pygame.display.flip()
    clock.tick(60)
