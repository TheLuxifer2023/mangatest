'''
Main file
'''

from downloader import Downloader

settings = {
    # Manga urls, should be the same website
    'manga_url': [
        'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/7e61813d-31d3-48de-9d3e-402e3e7ae308/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F'
    ],
    # Your cookies
    'cookies': '[{"domain":".bookwalker.jp","expirationDate":1766515803.201998,"hostOnly":false,"httpOnly":false,"name":"bweternity","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"3v5u10pqzxa8c4oogcwcgc8s4k40ks000w0g440g8ggw44os","index":0,"isSearch":false},{"domain":".bookwalker.jp","expirationDate":1766515803.795939,"hostOnly":false,"httpOnly":true,"name":"myService","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"1","index":1,"isSearch":false},{"domain":".bookwalker.jp","expirationDate":1766515803.795979,"hostOnly":false,"httpOnly":true,"name":"myStore","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"0","index":2,"isSearch":false},{"domain":".bookwalker.jp","hostOnly":false,"httpOnly":true,"name":"bwsess","path":"/","sameSite":"no_restriction","secure":true,"session":true,"storeId":"0","value":"2q4o13rfr0tl7h0adflg336rpd","index":3,"isSearch":false},{"domain":".bookwalker.jp","expirationDate":1766515809.663313,"hostOnly":false,"httpOnly":false,"name":"showSlider","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"0","index":4,"isSearch":false},{"domain":".bookwalker.jp","expirationDate":1739732157,"hostOnly":false,"httpOnly":false,"name":"_fbp","path":"/","sameSite":"lax","secure":false,"session":false,"storeId":"0","value":"fb.1.1731955883227.835270173307929344","index":5,"isSearch":false},{"domain":"member.bookwalker.jp","hostOnly":true,"httpOnly":true,"name":"JSESSIONID","path":"/","sameSite":"unspecified","secure":true,"session":true,"storeId":"0","value":"YueRCWQtwDD9Fv67PkliPw__","index":6,"isSearch":false},{"domain":".bookwalker.jp","expirationDate":1763492119.52857,"hostOnly":false,"httpOnly":true,"name":"cm_kp_login_account","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"GL","index":7,"isSearch":false},{"domain":".bookwalker.jp","expirationDate":1766516120.172735,"hostOnly":false,"httpOnly":false,"name":"bwmember","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"U2FsdGVkX1%2Bsk8LW9LHfWXW4%2FcNKe8Aog%2Bz5JFwf%2FtI%3D","index":8,"isSearch":false},{"domain":".bookwalker.jp","expirationDate":1763492157.030331,"hostOnly":false,"httpOnly":false,"name":"cm_kp_lan","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"ja","index":9,"isSearch":false},{"domain":"member.bookwalker.jp","expirationDate":1732560958.295753,"hostOnly":true,"httpOnly":false,"name":"AWSALB","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"M0SIcqnbP3Pp9zqYYmthq9sDuO4RzLSK9BMjFTAnIAF8Ztgjjn813vimGx0D9nHcsUcP20UqQtkULU5j+zYBTAxZlVDd9nkKRjcOdwiwK09MjpgUx7PAvt4a09Bp","index":10,"isSearch":false},{"domain":"member.bookwalker.jp","expirationDate":1732560958.295816,"hostOnly":true,"httpOnly":false,"name":"AWSALBCORS","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"M0SIcqnbP3Pp9zqYYmthq9sDuO4RzLSK9BMjFTAnIAF8Ztgjjn813vimGx0D9nHcsUcP20UqQtkULU5j+zYBTAxZlVDd9nkKRjcOdwiwK09MjpgUx7PAvt4a09Bp","index":11,"isSearch":false}]',
    # Folder names to store the Manga, the same order with manga_url
    'imgdir': [
        'IMGDIR_FOR_URL_1'
    ],
    # Resolution, (Width, Height), For coma this doesn't matter.
    'res': (784, 1200),
    # Sleep time for each page (Second), normally no need to change.
    'sleep_time': 1,
    # Time wait for page loading (Second), if your network is good, you can reduce this parameter.
    'loading_wait_time': 20,
    # Cut image, (left, upper, right, lower) in pixel, None means do not cut the image. This often used to cut the edge.
    # Like (0, 0, 0, 3) means cut 3 pixel from bottom of the image.
    # or set dynamic to allow the scrypt to cut_images dynamictly (This work only correct if start_page is None)
    # this removed whitespace on the corners, initialised by the Cover.
    'cut_image': None,
    # File name prefix, if you want your file name like 'klk_v1_001.jpg', write 'klk_v1' here.
    'file_name_prefix': '',
    # File name digits count, if you want your file name like '001.jpg', write 3 here.
    'number_of_digits': 3,
    # Start page, if you want to download from 3 page, set this to 3, None means from 0
    'start_page': None,
    # End page, if you want to download until 10 page, set this to 10, None means until finished
    'end_page': None,
}

if __name__ == '__main__':
    downloader = Downloader(**settings)
    downloader.download()
