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
