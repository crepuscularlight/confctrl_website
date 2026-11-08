# ConfCtrl project website

Open index.html in a browser. No build, install, or internet connection is needed for local assets. External Paper and author links require internet.

Optional local server (run from this folder):

    python -m http.server 8000

Then open http://localhost:8000.

The page follows the supplied CoVAR academic-page layout, with verified ConfCtrl authors and affiliations, introduction video, abstract, method, result tabs, sample videos, poster, and BibTeX. Paper links to the DOI printed in the supplied author proof; no unpublished code or arXiv link was invented.

The original video is unchanged. static/videos/confctrl-introduction.mp4 is an H.264/AAC, 1280 x 720, CRF 25 copy with faststart. Original: 564,222,343 bytes. Compressed: 43,471,268 bytes (92.3% smaller). Audio is retained. Recreate it with python compress_video.py (requires imageio-ffmpeg).

Images derive from ../pdf and ../poster.png. The poster PDF comes from ../3568_Yang_1400x1000mm.pdf. Additional video examples come from ../eccv. prepare_assets.py reproduces assets with Pillow and imageio-ffmpeg.

Validation: python validate.py checks all local asset references, anchors, duplicate IDs, full video decoding, and MP4 faststart. Browser layout and interaction verification could not run because the browser runtime failed with Windows logon error 1385.

Deployable files: index.html, static/, and .nojekyll. This task did not publish the site.

Correction: the teddy bear and DL3DV clips sourced from eccv/teddybear.mp4 and eccv/dl3dv.mp4 were removed from the gallery because they are not ConfCtrl results. The gallery retains eccv/inference_video_000.mp4. The asset script no longer imports the two incorrect clips. Their unused generated copies remain on disk, but are not referenced by the website.

Verified replacements: video_content/video_4_gif/Media69.mp4 (CO3D teddy bear, slide 8 Ours column, image85.gif) and Media97.mp4 (CO3D to DL3DV zero-shot playground, slide 10 Ours column, image120.gif). Verified by midpoint-frame comparison against the labeled presentation assets. Both are remuxed with faststart without recompression. The third video is unchanged.

Current gallery selection: Media67.mp4 (white teddy bear, back-to-front orbit; slide 8 image83.gif, Ours) and Media93.mp4 (classroom, CO3D to DL3DV zero-shot; slide 10 image124.gif, Ours). These supersede Media69 and Media97. Selected after reviewing five frames across each candidate clip; provenance checked against presentation frame content and Ours-column positions. New filenames prevent cached old clips from appearing.

Latest selection (supersedes the earlier selections): the user explicitly chose Media76.mp4 and Media58.mp4 from video_content/video_4_gif, in that order. The gallery labels these Teddy bear and Fire hydrant. Copies use selected-media76 and selected-media58 filenames and faststart without recompression. The third clip remains unchanged.
