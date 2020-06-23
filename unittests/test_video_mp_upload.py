from aweme.video.video_mp_publish import VideoMPPublish

if __name__ == '__main__':
    hub = VideoMPPublish(access_token="act.a1afc59657287aae317c51b5a089921dVGHyehETdgZQMfWZQS8VfFmGfKdw",
                         open_id="236b48f1-a993-4c75-ba64-d1f810df0a73")
    upload_id = hub.init_upload()
    hub.upload_part('/Users/breakup/Desktop/out2.mov', upload_id)
    video_id = hub.complete_upload(upload_id)
    print("video_id=" + video_id)
