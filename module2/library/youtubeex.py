from pytubefix import YouTube
url="https://www.youtube.com/watch?v=XV-lIaO00H8&pp=ygUMcHl0aG9uIHN0YXJ0"
YouTube(url).streams.first().download()







# from pytubefix import YouTube

# url = "https://www.youtube.com/watch?v=fr1f84rg4Nw&pp=ygUMcHl0aG9uIHN0YXJ0"

# yt = YouTube(url)

# stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

# stream.download()






























'''for first stream:from pytubefix import YouTube
YouTube class import કરે છે.
YouTube video access અને download કરવા માટે.
url="..."
Download કરવાની video ની link store કરે છે.
YouTube(url)
URL પરથી YouTube object બનાવે છે.
.streams
Video ના બધા available streams (qualities) મેળવે છે.
.first()
ઉપલબ્ધ streams માંથી પહેલી stream પસંદ કરે છે.
.download()
પસંદ કરેલી stream download કરે છે.'''

'''for second:.first?
.first() શું કરે છે?
stream = yt.streams.filter(
    progressive=True,
    file_extension='mp4'
).first()
filter() પછી ઘણી streams મળી શકે.
.first() એ list માંથી પહેલી stream પસંદ કરે છે.
Example

ધારો filter પછી આ streams મળે:

144p
360p
720p
.first()

➡️ 144p stream પસંદ કરશે (સૌથી પહેલી
progressive=True શું છે?

YouTube video માં સામાન્ય રીતે 2 પ્રકારના streams હોય છે:

Progressive Stream
Audio + Video બંને એક જ file માં હોય. ✅
Adaptive Stream
Audio અને Video અલગ-અલગ files માં હોય. ❌
Example
yt.streams.filter(progressive=True)

➡️ એવી streams શોધે છે જેમાં Audio + Video સાથે હો

'''