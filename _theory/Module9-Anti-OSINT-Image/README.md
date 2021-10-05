
Image Analysis
- Find all metadata, exif associated
- Find if that image has anything encoded / secrative about it => Stego analysis

All of that was done even before the image was even opened / viewed
* https://hackernoon.com/your-digital-photos-can-reveal-information-about-you-732783dd857b
- Using different masks & filters to find any cryptic details
- Reverse search on the images / component images
- | - Crop out the face to perform facial search
- | - Geo Location finding (based upon the surrounding)
- | - OCR to gather any exciting data. eg: Uploaded image of your winning lottery ticket, now that ticket number was copid by a bad person and they went on to redeem the lottery prize for themselves
- | - Last resort: Let the big hitters do it for us. Use reverse image search options like Yandex / Bing / Google

-- Can't destroy all trace of online existence, but can make things difficult for the trackers
- Destory metadata, exif data
- Add ambient noise to the image (adversial samples) and then upload to the internet. This will ensure that the image stays as it is, but when it is analyzed, it doesn't exactly give the correct outputs to the searcher (would not work every time, but worth a try nonetheless)
- Intentionally have pattern in the images like a filter, so that a basic neural network would associate the pattern or the filter as the identity of the social media account handler, rather than the actual user
