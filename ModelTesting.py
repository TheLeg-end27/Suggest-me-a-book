from fastai.vision.all import *

is_cat,_,probs = learn.predict(PILImage.create('cat000001.png'))
im = Image.open("cat000001.png")

im.to_thumb(256,256)
print(f"This is a: {is_cat}.")
print(f"Probability it's a cat: {probs[0]:.4f}")
is_dog,_,probs = learn.predict(PILImage.create('dog000001.png'))
im = Image.open("dog000001.png")
im.to_thumb(256,256)
print(f"This is a: {is_dog}.")
print(f"Probability it's a dog: {probs[1]:.4f}")