import pygame
import glob

pygame.init()
windows = pygame.display.set_mode((200, 100))

im = pygame.image.load("1_result_test.bmp")
print(im.get_size())
# Create an array of the pixels
pix = pygame.PixelArray(im)

# Open all bmp, average their pixel values and save the result
for file in sorted(glob.glob("./*_result_test.bmp")):
    im = pygame.image.load(file)
    pix2 = pygame.PixelArray(im)
    pix = (pix + pix2) / 2

# Save the result
pygame.image.save(pix.make_surface(), "result.bmp")

