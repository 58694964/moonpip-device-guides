# Moonpip device guides

This directory is the root of the standalone public GitHub Pages repository. Publish only this directory, never the full app project.

1. Set the repository default branch to `main`; enable Settings → Pages → Source: GitHub Actions.
2. Push this directory. The workflow validates JSON before deploying `public/`.
3. The endpoint is `https://58694964.github.io/moonpip-device-guides/v1/guides.json`.
4. Set the app Info.plist `GuideCatalogURL` to the verified HTTPS endpoint. No token belongs in the app.

Edit `public/v1/guides.json`, increment `contentVersion` for every content change, and update `updatedAt`. Keep schemaVersion 1; incompatible formats require a new path and app support. To revert content, publish it with a NEW, higher contentVersion. Never decrement a version. Preserve stable brand and section IDs. Provide both en and zh-Hans for every visible string. The client does not execute HTML, Markdown, shell commands or remote code.

Run `pip install -r requirements.txt` then `python scripts/validate.py`. Before an app release, copy the validated catalog to `../iOS/Moonpip/Moonpip/Resources/Brands.json` to update its bundled fallback.

GitHub Pages is public and CDN-cached. Verify deployment with a GET, save ETag, then GET again with If-None-Match; expect 304 when supported. The client falls back to Last-Modified or a normal GET plus content comparison. Publishing may take time; do not promise instant propagation.

Published at https://58694964.github.io/moonpip-device-guides/v1/guides.json . Verified GET 200 and conditional GET 304 on 2026-11-15; client simulator cached the catalog and observed an unchanged response.
