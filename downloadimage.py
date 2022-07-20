# ImageDownloader - Sample try


def ImageDownloader(url):
    import os, re, requests

    response = requests.get(url)
    text = response.text

    p = r'<img.*?src="(.*?)"[^\>]+>'
    img_addrs = re.findall(p, text)

    for i in img_addrs:
        os.system("wget {}".format(i))

    return "DONE"


# USAGE
# Change the URL from where you have to download the image
ImageDownloader(
    "https://cdn.pixabay.com/photo/2015/04/19/08/32/rose-729509_960_720.jpg"
)
