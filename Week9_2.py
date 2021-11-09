import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import imageio

text = open(r'6.txt', 'r', encoding='utf-8').read()
cut_text = jieba.cut(text)
result = " ".join(cut_text)
mk = imageio.imread('pic.png')
wc = WordCloud(
    font_path='./fonts/simhei.ttf',
    background_color='white',
    width=500,
    height=350,
    max_font_size=100,
    min_font_size=10,
    mode='RGBA',
    mask=mk
)

wc.generate(result)
wc.to_file(r'wordcloud.png')
plt.figure("Python")
plt.imshow(wc)
plt.axis('off')
plt.show()
