import io
import base64
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
def build_word_cloud(word_list, mask, color_func):
    font_path = 'static/font/msjh.ttc'
    img = io.BytesIO()

    wc = WordCloud(font_path=font_path, max_words=2000, mask=mask, max_font_size=300, random_state=1)
    wc.generate_from_text(word_list)
    wc.recolor(color_func=color_func, random_state=2)

    #plt.rcParams["figure.figsize"] = (25, 25)
    plt.rcParams["figure.figsize"] = (6, 6)
    plt.imshow(wc)
    plt.axis("off")

    plt.savefig(img, format='png')
    img.seek(0)
    cloud_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(cloud_url)
