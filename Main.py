from PIL import Image, ImageFont, ImageDraw

print("Генератор мемов запущен!")
top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")
print(top_text, bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
print("3. Кот (стоит и смотрит)")
print("4. Симпсон уходит в кусты")
print("5. Губка Боб приносит мир")
print("6. Чилл Гай")
print("7. Все правда посмеялись")

image_number = input("Введите нужный номер картинки: ")
image_name = ""

if image_number == "1":
    image_name = "Кот в ресторане.png"
elif image_number == "2":
    image_name = "Кот в очках.png"
elif image_number == "3":
    image_name = "Cute-Cat.jpg"
elif image_number == "4":
    image_name = "simpson_goes_in_bush.jpg"
elif image_number == "5":
    image_name = "spongebob_rainbow.jpg"
elif image_number == "6":
    image_name = "chill_guy.jpg"
elif image_number == "7":
    image_name = "whole_squad.png"
else:
    print("Данной картинки нет.")

print(image_name)

image = Image.open(image_name)

draw = ImageDraw.Draw(image)
width, height = image.size

font = ImageFont.truetype("calibri.ttf", size=40)

text = draw.textbbox((0,0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="white")

text = draw.textbbox((0,0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="black")

image.save("new_meme.png")

print("Ваш мем готов!")
