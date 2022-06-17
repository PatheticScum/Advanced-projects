from pytube import YouTube

try:
    yt_link = input('Enter a link of a video from YouTube to download.')

    if yt_link.startswith('https://youtu.be/'):

        yt_obj = YouTube(yt_link)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

        filters.get_highest_resolution().download('Videos/')
        print('Video Downloaded Successfully')
    else:
        print('Enter link only from YouTube.')
except Exception as e:
    print("Video is not downloaded")
